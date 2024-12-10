from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html
import html

from ..models import Analysis, TeachingResources


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
    autocomplete_fields = ["films", "topics", "tags", "teaching_resources"]
    readonly_fields = ("safe_bibliography",)
    exclude = ["bibliography"]
    list_display = [
        "dynamic_title",
        "related_films",
        "list_topics",
        "list_tags",
        "safe_content",
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
        modified_content = truncated_content.replace("{", "(").replace("}", ")")
        return format_html(modified_content)

    safe_content.allow_tags = True
    safe_content.short_description = "Content"

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


@admin.register(TeachingResources)
class TeachingResourcesAdmin(AnalysisAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }
        js = ("admin/js/mentionsPluginConfig.js",)

    form = TRAdminForm
    inlines = [TRAnalysisInline]
    autocomplete_fields = ["films", "topics", "tags", "clips"]
    readonly_fields = ("safe_bibliography",)
    exclude = ["bibliography"]
    filter_horizontal = ("films",)

    list_display = [
        "dynamic_title",
        "related_films",
        "list_topics",
        "list_tags",
    ]
    search_fields = ["title", "tags", "topics"]

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
