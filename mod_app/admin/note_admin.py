from django.contrib import admin
from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html


from mod_app.models import ProjectNote, Feedback, VisualInfluences, WrittenInfluences
from mod_app.utils.mixins import s3BrowserButtonMixin


@admin.register(ProjectNote)
class ProjectNoteAdmin(admin.ModelAdmin):
    class Media:
        js = ("admin/js/mentionsPluginConfig.js",)

    search_fields = ["title"]
    list_display = ["title", "safe_content"]
    readonly_fields = ("bibliography",)

    def safe_content(self, obj):
        truncated_content = truncatechars_html(obj.content, 200)
        modified_content = truncated_content.replace("{", "(").replace("}", ")")
        return format_html(modified_content)

    safe_content.allow_tags = True
    safe_content.short_description = "Content"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    class Media:
        js = ("admin/js/mentionsPluginConfig.js",)

    search_fields = ["title"]
    list_display = ["title", "safe_content"]
    readonly_fields = ("bibliography",)

    def safe_content(self, obj):
        truncated_content = truncatechars_html(obj.content, 200)
        modified_content = truncated_content.replace("{", "(").replace("}", ")")
        return format_html(modified_content)

    safe_content.allow_tags = True
    safe_content.short_description = "Content"


class VisInline(s3BrowserButtonMixin, admin.TabularInline):
    model = VisualInfluences.films.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]
    verbose_name = "Visual Influences"
    verbose_name_plural = "Visual Influences"


class WritInline(s3BrowserButtonMixin, admin.TabularInline):
    model = WrittenInfluences.films.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]
    verbose_name = "Written Influences"
    verbose_name_plural = "Written Influences"


@admin.register(VisualInfluences)
class VisualInfluencesAdmin(admin.ModelAdmin):
    class Media:
        js = ("admin/js/mentionsPluginConfig.js",)

    search_fields = ["title"]
    list_display = ["title", "safe_content"]
    readonly_fields = ("bibliography",)
    filter_horizontal = ("films",)

    def safe_content(self, obj):
        truncated_content = truncatechars_html(obj.content, 200)
        modified_content = truncated_content.replace("{", "(").replace("}", ")")
        return format_html(modified_content)

    safe_content.allow_tags = True
    safe_content.short_description = "Content"


@admin.register(WrittenInfluences)
class WrittenInfluencesAdmin(admin.ModelAdmin):
    class Media:
        js = ("admin/js/mentionsPluginConfig.js",)

    search_fields = ["title"]
    list_display = ["title", "safe_content"]
    readonly_fields = ("bibliography",)
    filter_horizontal = ("films",)

    def safe_content(self, obj):
        truncated_content = truncatechars_html(obj.content, 200)
        modified_content = truncated_content.replace("{", "(").replace("}", ")")
        return format_html(modified_content)

    safe_content.allow_tags = True
    safe_content.short_description = "Content"
