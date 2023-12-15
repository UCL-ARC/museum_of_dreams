from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.db import models
from django.template.defaultfilters import truncatechars_html


from .models import *


class SourceAdminForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = "__all__"


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]
    form = SourceAdminForm
    readonly_fields = ("is_source",)


@admin.register(FileLink)
class FileLinkAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


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
                "fields": ("additional_links",),
            },
        ),
        (
            "Printed Materials",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    "scripts",
                    "press_books",
                    "programmes",
                    "pub_mat",
                ),
            },
        ),
        (
            "Visual Resources",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (
                    "stills",
                    "postcards",
                    "posters",
                    "drawings",
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


class AnalysisAdminForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"class": "ckeditor"}),
        }


class TRAdminForm(forms.ModelForm):
    class Meta:
        model = TeachingResources
        fields = "__all__"
        widgets = {
            "material": forms.Textarea(attrs={"class": "ckeditor"}),
        }


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    form = AnalysisAdminForm
    autocomplete_fields = ["films", "topics", "tags", "teaching_resources"]
    list_display = [
        "dynamic_title",
        "related_films",
        "list_topics",
        "list_tags",
        "safe_content",
    ]

    def dynamic_title(self, obj):
        return obj.__str__()

    dynamic_title.short_description = "Title"
    dynamic_title.admin_order_field = "title"

    def related_films(self, obj):
        films = obj.films.all()[:3]
        return ", ".join(str(f) for f in films)

    related_films.short_description = "Films"

    def list_topics(self, obj):
        topics = obj.topics.all()
        return ", ".join(str(t) for t in topics)

    list_topics.short_description = "Topics"

    def list_tags(self, obj):
        tags = obj.tags.all()
        return ", ".join(str(t) for t in tags)

    list_tags.short_description = "Tags"

    def safe_content(self, obj):
        truncated_content = truncatechars_html(obj.content, 200)
        return format_html(truncated_content)

    safe_content.allow_tags = True
    safe_content.short_description = "Content"


@admin.register(TeachingResources)
class TeachingResourcesAdmin(AnalysisAdmin):
    form = TRAdminForm
    autocomplete_fields = ["films", "topics", "tags"]
    list_display = [
        "related_films",
        "list_topics",
        "list_tags",
    ]
    search_fields = ["title", "tags", "topics"]
