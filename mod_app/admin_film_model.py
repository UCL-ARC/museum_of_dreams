from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models
from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html

from .models import *


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "temporary_images",
        "video",
        "alt_titles",
        "release_date",
        "production_country",
        "production_company",
        "safe_synopsis",
        "safe_comments",
    ]

    # these fields show html tags from the ckeditor otherwise
    def safe_synopsis(self, obj):
        truncated_synopsis = truncatechars_html(obj.synopsis, 200)
        return format_html(truncated_synopsis)

    safe_synopsis.allow_tags = True
    safe_synopsis.short_description = "Synopsis"

    def safe_comments(self, obj):
        truncated_comments = truncatechars_html(obj.comments, 200)
        return format_html(truncated_comments)

    safe_comments.allow_tags = True
    safe_comments.short_description = "Comments"

    autocomplete_fields = [
        "genre",
        "source",
        "additional_links",
        "scripts",
        "press_books",
        "programmes",
        "pub_mat",
        "stills",
        "postcards",
        "posters",
        "drawings",
        "video",
    ]
    search_fields = ["title", "alt_titles"]
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }
    fieldsets = (
        (
            "Main Information (Filmic Section)",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    "title",
                    "alt_titles",
                    "release_date",
                    ("production_country", "production_company"),
                    "synopsis",
                    ("source", "genre"),
                    ("cast", "crew"),
                    "video",
                ),
            },
        ),
        (
            "Technical Section",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    ("duration", "current_length"),
                    ("support", "is_in_colour"),
                    ("format_type", "format_other"),
                    "print_comments",
                ),
            },
        ),
        (
            "Additional Information (non filmic)",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": ("additional_links",),
            },
        ),
        (
            "Printed Materials",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    ("scripts", "press_books"),
                    ("programmes", "pub_mat"),
                ),
            },
        ),
        (
            "Visual Resources",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    ("stills", "postcards"),
                    ("posters", "drawings"),
                ),
            },
        ),
        (
            "Comments and Temporary Images",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    "comments",
                    "temporary_images",
                ),
            },
        ),
    )
