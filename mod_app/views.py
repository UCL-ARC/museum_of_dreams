from typing import Any
from django.views.generic import DetailView, ListView, TemplateView
from django.http import JsonResponse
from django.views import View
from django.template.defaultfilters import striptags


from .models import Film, BibliographyItem, Analysis, TeachingResources


class HomeView(TemplateView):
    template_name = "home.html"


class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get("list")

        if page == "all":
            context["object_list"] = context["film_list"] = self.model.objects.all()
            context["is_paginated"] = False
        elif page:
            try:
                self.paginate_by = int(page)
            except ValueError:
                pass
        return context

    #     for film in context["object_list"]:
    #         # themes = list(film.themes.all())
    #         # film.themes = themes
    #         # starring = list(film.cast)
    #         # film.starring = ", ".join(str(actor) for actor in starring)
    #         # print(starring, "film.actors", film.actors.all())
    #     return context


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
