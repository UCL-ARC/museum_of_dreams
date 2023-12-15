from django import forms
from django.contrib import admin
from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html

from .models import *
from .admin_minor_models import *
from .admin_film_model import *


class AnalysisAdminForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"class": "ckeditor"}),
        }


class TRAnalysisInline(admin.TabularInline):
    model = Analysis.teaching_resources.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


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
    inlines = [TRAnalysisInline]
    autocomplete_fields = ["films", "topics", "tags"]
    list_display = [
        "dynamic_title",
        "related_films",
        "list_topics",
        "list_tags",
    ]
    search_fields = ["title", "tags", "topics"]
