from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.db import models

from .models import *


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


from django.utils.html import format_html


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "alt_titles",
        "release_date",
        "safe_synopsis",
        "safe_comments",
    ]

    # these fields show html tags from the ckeditor otherwise
    def safe_synopsis(self, obj):
        return format_html(obj.synopsis)

    safe_synopsis.allow_tags = True
    safe_synopsis.short_description = "Synopsis"

    def safe_comments(self, obj):
        return format_html(obj.comments)

    safe_comments.allow_tags = True
    safe_comments.short_description = "Comments"

    autocomplete_fields = [
        "genre",
        "additional_links",
        # "scripts",
        # "press_books",
        # "programmes",
        # "pub_mat",
        # "stills",
        # "postcards",
        # "posters",
        # "drawings",
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

    # def handle_related_model(self, db_field, request, model_name, instance_id):
    #     related_model = globals()[model_name]
    #     print(Programme.objects.filter(film__id=instance_id))
    #     if instance_id:
    #         if related_model.objects.all().exists():
    #             queryset = related_model.objects.filter(film__id=instance_id)

    #             return queryset
    #         else:
    #             return related_model.objects.none()
    #     else:
    #         return db_field.related_model.objects.none()

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     filelink_fields = {
    #         # "scripts": "Script",
    #         # "press_books": "PressBook",
    #         "programmes": "Programme",
    #         "pub_mat": "Publicity",
    #         "stills": "Still",
    #         "postcards": "Postcard",
    #         "posters": "Poster",
    #         "drawings": "Drawing",
    #     }
    #     instance_id = request.resolver_match.kwargs.get("object_id")
    #     for fl in filelink_fields:
    #         if db_field.name == fl:
    #             print(fl)
    #             kwargs["queryset"] = self.handle_related_model(
    #                 db_field, request, filelink_fields[fl], instance_id
    #             )

    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


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
