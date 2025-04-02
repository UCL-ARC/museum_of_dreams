from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from ..models import Analysis, TeachingResources
from mod_app.admin.utils import (
    list_genres,
    list_keywords,
    list_tags,
    safe_bibliography,
    safe_content,
)


class AnalysisAdminForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = "__all__"
        widgets = {
            "content": CKEditorWidget(),
        }


class TRAnalysisInline(admin.TabularInline):
    model = Analysis.teaching_resources.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]
    verbose_name = "Analysis"
    verbose_name_plural = "Analyses"


class TRAdminForm(forms.ModelForm):
    class Meta:
        model = TeachingResources
        fields = "__all__"
        widgets = {
            "material": CKEditorWidget(),
        }


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }
        js = ("admin/js/mentionsPluginConfig.js",)

    form = AnalysisAdminForm
    autocomplete_fields = ["films", "keywords", "genre", "teaching_resources", "topics"]
    readonly_fields = ("safe_bib",)
    exclude = ["bibliography"]
    list_display = [
        "dynamic_title",
        "related_films",
        "list_keywords_display",
        "list_genres_display",
        "safe_content_display",
    ]
    filter_horizontal = ("films",)

    def dynamic_title(self, obj):
        return obj.__str__()

    dynamic_title.short_description = "Title"
    dynamic_title.admin_order_field = "title"

    def related_films(self, obj):
        films = obj.films.all()[:3]
        return ", ".join(str(f) for f in films)

    related_films.short_description = "Films"

    def list_keywords_display(self, obj):
        return list_keywords(obj)

    list_keywords_display.short_description = "Keywords"

    def list_genres_display(self, obj):
        return list_genres(obj)

    list_genres_display.short_description = "Genres"

    def safe_content_display(self, obj):
        return safe_content(obj)

    safe_content_display.short_description = "Content"

    def safe_bib(self, obj):
        return safe_bibliography(obj)

    safe_bib.short_description = "Bibliography"


@admin.register(TeachingResources)
class TeachingResourcesAdmin(AnalysisAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }
        js = ("admin/js/mentionsPluginConfig.js",)

    form = TRAdminForm
    inlines = [TRAnalysisInline]
    autocomplete_fields = ["films", "keywords", "tags", "clips", "topics"]
    readonly_fields = ("safe_bib",)
    exclude = ["bibliography"]
    filter_horizontal = ("films",)

    list_display = [
        "dynamic_title",
        "related_films",
        "list_keywords_display",
        "list_tags_display",
    ]
    search_fields = ["title", "tags", "keywords"]

    def safe_bib(self, obj):
        return safe_bibliography(obj)

    safe_bib.short_description = "Bibliography"

    def list_keywords_display(self, obj):
        return list_keywords(obj)

    list_keywords_display.short_description = "Keywords"

    def list_tags_display(self, obj):
        return list_tags(obj)

    list_tags_display.short_description = "Tags"
