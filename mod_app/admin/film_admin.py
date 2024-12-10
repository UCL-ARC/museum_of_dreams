from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models
from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html
import html

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
from mod_app.admin.note_admin import VWIInline
from mod_app.utils.mixins import EmailMixin

from ..models import Analysis, TeachingResources, Film


class FilmAnalysisInline(admin.TabularInline):
    model = Analysis.films.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]
    verbose_name = "Analysis"
    verbose_name_plural = "Analyses"


class TRInline(admin.TabularInline):
    model = TeachingResources.films.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]
    verbose_name = "Teaching Resources"
    verbose_name_plural = "Teaching Resources"


@admin.register(Film)
class FilmAdmin(EmailMixin, admin.ModelAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }
        js = ("admin/js/mentionsPluginConfig.js",)

    autocomplete_fields = ["genre"]
    search_fields = [
        "bfi_identifier",
        "title",
        "alt_titles",
        "production_company",
        "production_country",
        "release_date",
    ]
    formfield_overrides = {
        models.TextField: {
            "widget": CKEditorWidget(),
        },
    }

    inlines = [
        FilmAnalysisInline,
        TRInline,
        VWIInline,
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
        "bfi_identifier",
        "safe_temporary_images",
        "preview_video",
        "safe_alt_titles",
        "release_date",
        "production_country",
        "production_company",
        "safe_synopsis",
        "safe_comments",
    ]

    # these fields show html tags from the ckeditor otherwise
    def safe_synopsis(self, obj):
        truncated_synopsis = truncatechars_html(obj.synopsis, 200)
        modified_synopsis = truncated_synopsis.replace("{", "(").replace("}", ")")
        return format_html(modified_synopsis)

    safe_synopsis.allow_tags = True
    safe_synopsis.short_description = "Synopsis"

    def safe_comments(self, obj):
        truncated_comments = truncatechars_html(obj.comments, 200)
        modified_comments = truncated_comments.replace("{", "(").replace("}", ")")
        return format_html(modified_comments)

    safe_comments.allow_tags = True
    safe_comments.short_description = "Comments"

    def safe_alt_titles(self, obj):
        return format_html(str(obj.alt_titles))

    safe_alt_titles.allow_tags = True
    safe_alt_titles.short_description = "Alt Titles"

    def safe_temporary_images(self, obj):
        return format_html(obj.temporary_images)

    safe_temporary_images.allow_tags = True
    safe_temporary_images.short_description = "List Images"

    def safe_bibliography(self, obj):
        bib_items = obj.bibliography.all()
        formatted_items = [
            format_html(
                "<li>{}</li>", format_html(html.unescape(bib_item.full_citation))
            )
            for bib_item in bib_items
        ]
        return format_html("<ul>{}</ul>", format_html("".join(formatted_items)))

    safe_bibliography.short_description = "Bibliography"
    safe_bibliography.allow_tags = True

    def preview_video(self, obj):
        if obj.videos.first():
            # format for working with mediacentral embeds and youtube embeds
            return format_html(
                '<div"><iframe src="{}" frameborder="0"  scrolling="no" allowfullscreen></iframe></div>',
                obj.videos.first(),
            )
        else:
            return "-"

    readonly_fields = ("safe_bibliography",)
    fieldsets = (
        (
            "Main Information (Filmic Section)",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    "title",
                    "alt_titles",
                    (
                        "bfi_identifier",
                        "release_date",
                    ),
                    ("production_country", "production_company"),
                    "synopsis",
                    ("cast", "crew"),
                    ("genre", "bfi_category"),
                ),
            },
        ),
        (None, {"classes": ("placeholder Source_film-group",), "fields": ()}),
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
            None,
            {
                "classes": ("placeholder VisualWrittenInfluences_films-group",),
                "fields": (),
            },
        ),
        (
            "Comments and List Images",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    "comments",
                    "temporary_images",
                ),
                "description": "Mentions are available here and will contibute to the bibliography.",
            },
        ),
        (
            "Bibliography",
            {
                "classes": ("grp-collapse",),
                "fields": ("safe_bibliography",),
                "description": "Note: This section updates on save, and some items may not be visible immediately.",
            },
        ),
    )
