from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.db import models

from .models import *


class FilmAdmin(admin.ModelAdmin):
    search_fields = [""]
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
                    "source_material",
                    "genre",
                    "bfi_category",
                    "actors",
                    "crew",
                    "video",
                ),
            },
        ),
        (
            "Technical Section",
            {
                "fields": (
                    "duration",
                    "current_length",
                    "element",
                    "support",
                    "format_type",
                    "rollers",
                    "is_in_colour",
                    "collection",
                    "print_status",
                    "print_status_comments",
                    "entry_date",
                ),
            },
        ),
        (
            "Additional Information (non filmic)",
            {
                "fields": (
                    "intertitle_text",
                    "intertitle_photo",
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


class AnalysisAdminForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"class": "ckeditor"}),
        }


class AnalysisAdmin(admin.ModelAdmin):
    form = AnalysisAdminForm


admin.site.register([Location, Tag, FileLink])

# Customised
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(Film, FilmAdmin)
