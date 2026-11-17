from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from mod_app.admin.analysis_admin import AnalysisAdmin, TRAnalysisInline

from ..models import TeachingResources, EditedCollection, ExhibitionResources

from mod_app.admin.utils import (
    list_topics,
    safe_bibliography,
    safe_material,
)


class TRAdminForm(forms.ModelForm):
    class Meta:
        model = TeachingResources
        fields = "__all__"
        widgets = {
            "material": CKEditorWidget(),
        }


@admin.register(TeachingResources)
class TeachingResourcesAdmin(AnalysisAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }
        js = ("admin/js/mentionsPluginConfig.js",)

    form = TRAdminForm
    inlines = [TRAnalysisInline]
    autocomplete_fields = ["films", "clips"]
    readonly_fields = ("safe_bib",)
    exclude = ["bibliography", "tags"]
    filter_horizontal = ("films",)

    list_display = [
        "dynamic_title",
        "related_films",
        "list_topics_display",
        "safe_material_display",
    ]
    search_fields = ["title", "tags"]

    def safe_bib(self, obj):
        return safe_bibliography(obj)

    safe_bib.short_description = "Bibliography"

    def list_topics_display(self, obj):
        return list_topics(obj)

    list_topics_display.short_description = "Topics"

    def safe_material_display(self, obj):
        return safe_material(obj)

    safe_material_display.short_description = "Content"


@admin.register(ExhibitionResources)
class ExhibitionResourcesAdmin(AnalysisAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }
        js = ("admin/js/mentionsPluginConfig.js",)

    form = TRAdminForm
    autocomplete_fields = ["films"]
    readonly_fields = ("safe_bib",)
    exclude = ["bibliography", "tags"]
    filter_horizontal = ("films",)

    list_display = [
        "dynamic_title",
        "related_films",
        "list_topics_display",
        "safe_material_display",
    ]
    search_fields = ["title", "tags"]

    def safe_bib(self, obj):
        return safe_bibliography(obj)

    safe_bib.short_description = "Bibliography"

    def list_topics_display(self, obj):
        return list_topics(obj)

    list_topics_display.short_description = "Topics"

    def safe_material_display(self, obj):
        return safe_material(obj)

    safe_material_display.short_description = "Content"


@admin.register(EditedCollection)
class EditedCollectionAdmin(AnalysisAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }
        js = ("admin/js/mentionsPluginConfig.js",)

    form = TRAdminForm
    autocomplete_fields = ["films"]
    readonly_fields = ("safe_bib",)
    exclude = ["bibliography", "tags"]
    filter_horizontal = ("films",)

    list_display = [
        "dynamic_title",
        "related_films",
        "list_topics_display",
        "safe_material_display",
    ]
    search_fields = ["title", "tags"]

    def safe_bib(self, obj):
        return safe_bibliography(obj)

    safe_bib.short_description = "Bibliography"

    def list_topics_display(self, obj):
        return list_topics(obj)

    list_topics_display.short_description = "Topics"

    def safe_material_display(self, obj):
        return safe_material(obj)

    safe_material_display.short_description = "Content"
