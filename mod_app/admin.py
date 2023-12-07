from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.db import models

from .models import *


# class FilmInline(admin.StackedInline):
#     model = Film.actors.through
#     extra = 1

#     def __str__(self):
#         return self.film.title


# class ActorAdmin(admin.ModelAdmin):
#     inlines = (FilmInline,)


class LinkAdminForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = "__all__"


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]
    form = LinkAdminForm


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(PressBook)
class PressBookAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Publicity)
class PublicityAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Still)
class StillAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Postcard)
class PostcardAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "release_date", "synopsis", "comments"]
    autocomplete_fields = [
        "genre",
        "additional_links",
        "scripts",
        "press_books",
        "programmes",
        "pub_mat",
        "stills",
        "postcards",
        "posters",
        "drawings",
    ]
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }
    fieldsets = (
        (
            "Main Information (Filmic Section)",
            {
                "fields": (
                    "title",
                    "release_date",
                    "alt_titles",
                    "production_country",
                    "production_company",
                    "synopsis",
                    "source",
                    "genre",
                    "cast",
                    "crew",
                    "video",
                ),
            },
        ),
        (
            "Technical Section",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    "duration",
                    "current_length",
                    "support",
                    "format_type",
                    "is_in_colour",
                    "print_comments",
                ),
            },
        ),
        (
            "Additional Information (non filmic)",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    "additional_links",
                    "scripts",
                    "press_books",
                    "programmes",
                    "pub_mat",
                    "stills",
                    "postcards",
                    "posters",
                    "drawings",
                    "comments",
                ),
            },
        ),
    )

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     film_id = request.resolver_match.kwargs.get("object_id")

    #     fields_to_filter = [
    #         "additional_links",
    #         "scripts",
    #         "press_books",
    #         "programmes",
    #         "pub_mat",
    #         "stills",
    #         "postcards",
    #         "posters",
    #         "drawings",
    #     ]
    #     # filter so only for this film instance shows
    #     if db_field.name in fields_to_filter:
    #         kwargs["queryset"] = FileLink.objects.filter(
    #             **{f"{db_field.related_query_name()}__id": film_id}
    #         )

    #     return super().formfield_for_manytomany(db_field, request, **kwargs)


class AnalysisAdminForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"class": "ckeditor"}),
        }


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    form = AnalysisAdminForm
