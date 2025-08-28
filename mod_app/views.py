import re

import boto3
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.defaultfilters import striptags
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from xhtml2pdf import pisa

# you may need to comment out the bwlow import when running locally if you get a socket error
from museum_of_dreams_project.settings.aws import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME,
)

from .models import Analysis, BibliographyItem, Film, Tag, TeachingResources


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        films_with_images = Film.objects.filter(cardimages__isnull=False)
        random_films = films_with_images.order_by("?")[:5]

        slides = []
        if random_films:
            for film in random_films:
                if film.cardimages.first().url:
                    slides.append(film.cardimages.first().url)
                else:
                    slides.append(film.cardimages.first().file.url)

        context["slides"] = slides
        context["slide_images"] = True
        return context


class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"
    paginate_by = 20

    def get_paginate_by(self, queryset):
        page = self.request.GET.get(self.page_kwarg)
        if page:
            return self.paginate_by
        else:
            return None


class FilmDetailView(DetailView):
    model = Film
    template_name = "film_detail.html"
    context_object_name = "film"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.object

        printed_material_slides = (
            list(film.scripts.all())
            + list(film.pressbooks.all())
            + list(film.programmes.all())
            + list(film.publicitys.all())
        )

        visual_resources_slides = (
            list(film.stills.all())
            + list(film.drawings.all())
            + list(film.posters.all())
            + list(film.postcards.all())
        )

        context["pm_slides"] = printed_material_slides
        context["vr_slides"] = visual_resources_slides

        context["video_slides"] = film.videos.all()
        return context


class MentionsApiView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("query", "")
        # search by full citation but return short one
        queryset = BibliographyItem.objects.filter(full_citation__icontains=query)
        mentions_data = [
            {
                "id": item.id,
                "short_citation": item.short_citation,
                "full_citation": striptags(item.full_citation)
                .replace("&nbsp;", " ")
                .replace("&amp;", "&"),  # making plain text
            }
            for item in queryset
        ]
        return JsonResponse(mentions_data, safe=False)


class AnalysisListView(ListView):
    model = Analysis
    template_name = "analysis_list.html"
    paginate_by = 20

    def get_paginate_by(self, queryset):
        page = self.request.GET.get(self.page_kwarg)
        if page:
            return self.paginate_by
        else:
            return None


class AnalysisDetailView(DetailView):
    model = Analysis
    template_name = "analysis_detail.html"
    context_object_name = "analysis"


class TRListView(ListView):
    model = TeachingResources
    template_name = "tr_list.html"
    paginate_by = 20

    def get_paginate_by(self, queryset):
        page = self.request.GET.get(self.page_kwarg)
        if page:
            return self.paginate_by
        else:
            return None


class TRDetailView(DetailView):
    model = TeachingResources
    template_name = "tr_detail.html"
    context_object_name = "tr"


class TagListView(ListView):
    model = Tag
    template_name = "tag_list.html"
    context_object_name = "tags"


class TagDetailView(DetailView):
    model = Tag
    template_name = "tag_detail.html"
    context_object_name = "tag"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["analyses"] = self.object.analysis_genres.all()
        context["films"] = self.object.films.all()
        context["teaching_resources"] = self.object.tr_tags.all()
        return context


class BibliographyListView(ListView):
    model = BibliographyItem
    template_name = "bibliography.html"


class BucketItemsView(View):
    @method_decorator(login_required)
    def get(self, request):
        not_ckeditor_browser = request.GET.get("not_ckeditor_browser")
        ckeditor_func_num = request.GET.get("CKEditorFuncNum")

        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        s3 = session.resource("s3")
        bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
        bucket_url = f"https://{bucket.name}.s3.eu-west-2.amazonaws.com/"

        response = bucket.objects.filter(Prefix="media/")
        items = [obj.key for obj in response]
        item_data = {"items": {}}
        for item in items:
            item_url = bucket_url + item
            match = re.search(r"media/(files|editor)/(.+)", item)
            if match:
                item_name = match.group(2)

            item_data["items"][item] = {"url": item_url, "name": item_name}

        context = {
            "item_data": item_data,
            "not_ckeditor_browser": not_ckeditor_browser,
            "ckeditor_func_num": ckeditor_func_num,
        }

        return render(request, "bucket_items.html", context)


class SearchView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["films"] = Film.object.all()
        context["analyses"] = Analysis.object.all()
        return context


def custom_404(request, exception=None):
    return render(request, "404.html", {}, status=404)


def downloadAnalysis(request, pk):
    analysis = Analysis.objects.get(pk=pk)
    template_name = "downloads/analysis.html"

    # Render the template with the context data
    html = render_to_string(template_name, {"analysis": analysis})

    # Create an HTTP response with the PDF file
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{analysis.title}.pdf"'

    status = pisa.CreatePDF(html, dest=response)

    if not status.err:
        return response
