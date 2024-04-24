import boto3
import re

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.template.defaultfilters import striptags
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.utils.decorators import method_decorator


from museum_of_dreams_project.settings.aws import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    BUCKET_NAME,
)
from .models import Film, BibliographyItem, Analysis, TeachingResources


class HomeView(TemplateView):
    template_name = "home.html"


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


class AnalysisDetailView(DetailView):
    model = Analysis
    template_name = "analysis_detail.html"
    context_object_name = "analysis"


class TRListView(ListView):
    model = TeachingResources
    template_name = "tr_list.html"
    paginate_by = 20


class TRDetailView(DetailView):
    model = TeachingResources
    template_name = "tr_detail.html"
    context_object_name = "tr"


class BibliographyListView(ListView):
    model = BibliographyItem
    template_name = "bibliography.html"
    paginate_by = 20


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
        bucket = s3.Bucket(BUCKET_NAME)
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
        # should we use another session id for passing info back
        request.session["selected_item"] = None

        context = {
            "item_data": item_data,
            "not_ckeditor_browser": not_ckeditor_browser,
            "ckeditor_func_num": ckeditor_func_num,
        }

        return render(request, "bucket_items.html", context)
