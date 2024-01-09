from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models
from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html

from mod_app.admin.link_admin import (
    DrawingInline,
    OtherLinkInline,
    PostcardInline,
    PosterInline,
    PressBookInline,
    ProgrammeInline,
    PublicityInline,
    ScriptInline,
    SourceInline,
    StillInline,
    VideoInline,
)


from ..models import Analysis, TeachingResources, Film


class FilmAnalysisInline(admin.TabularInline):
    model = Analysis.films.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


class TRInline(admin.TabularInline):
    model = TeachingResources.films.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }
        js = ("admin/js/mentionsPluginConfig.js",)

    autocomplete_fields = ["genre"]
    search_fields = ["title", "alt_titles"]
    formfield_overrides = {
        models.TextField: {
            "widget": CKEditorWidget(),
        },
    }

    inlines = [
        FilmAnalysisInline,
        TRInline,
        SourceInline,
        OtherLinkInline,
        VideoInline,
        ScriptInline,
        PressBookInline,
        ProgrammeInline,
        PublicityInline,
        StillInline,
        PostcardInline,
        PosterInline,
        DrawingInline,
    ]
    list_display = [
        "title",
        "temporary_images",
        "preview_video",
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

    def preview_video(self, obj):
        if obj.videos.first():
            if obj.videos.first().file:
                return format_html(
                    '<video width="150" height="120" controls><source src="{}" type="video/mp4"></video>',
                    obj.videos.first().file.url,
                )
            else:
                return format_html(
                    '<video width="150" height="120" controls ><source src="{}" type="video/mp4"></video>',
                    obj.videos.first(),
                )
            # previously tried to use youtube but that seems to be more tricky than expected and may not be used
        else:
            return "-"

    readonly_fields = ("bibliography",)
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
                    ("cast", "crew"),
                    ("genre", "bfi_category"),
                ),
            },
        ),
        (None, {"classes": ("placeholder sources-group",), "fields": ()}),
        (None, {"classes": ("placeholder videos-group",), "fields": ()}),
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
            "Printed Materials",
            {"fields": []},
        ),
        (None, {"classes": ("placeholder scripts-group",), "fields": ()}),
        (None, {"classes": ("placeholder pressbooks-group",), "fields": ()}),
        (None, {"classes": ("placeholder programmes-group",), "fields": ()}),
        (None, {"classes": ("placeholder publicitys-group",), "fields": ()}),
        (
            "Visual Resources",
            {"fields": []},
        ),
        (None, {"classes": ("placeholder stills-group",), "fields": ()}),
        (None, {"classes": ("placeholder postcards-group",), "fields": ()}),
        (None, {"classes": ("placeholder posters-group",), "fields": ()}),
        (None, {"classes": ("placeholder drawings-group",), "fields": ()}),
        (
            "Additional Information (non filmic)",
            {"fields": []},
        ),
        (None, {"classes": ("placeholder otherlinks-group",), "fields": ()}),
        (None, {"classes": ("placeholder Analysis_films-group",), "fields": ()}),
        (
            None,
            {"classes": ("placeholder TeachingResources_films-group",), "fields": ()},
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
        (
            "Bibliography",
            {
                "classes": ("grp-collapse",),
                "fields": ("bibliography",),
                "description": "Note: This section updates on save, and some items may not be visible immediately.",
            },
        ),
    )
