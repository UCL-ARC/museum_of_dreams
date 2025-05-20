from django.contrib import admin


from mod_app.admin.utils import safe_content
from mod_app.models import (
    ProjectNote,
    Feedback,
    VisualInfluences,
    WrittenInfluences,
    Archive,
)
from mod_app.utils.mixins import s3BrowserButtonMixin


@admin.register(ProjectNote)
class ProjectNoteAdmin(admin.ModelAdmin):
    class Media:
        js = ("admin/js/mentionsPluginConfig.js",)

    search_fields = ["title"]
    list_display = ["title", "safe_content_display"]
    readonly_fields = ("bibliography",)

    def safe_content_display(self, obj):
        return safe_content(obj)

    safe_content_display.short_description = "Content"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    class Media:
        js = ("admin/js/mentionsPluginConfig.js",)

    search_fields = ["title"]
    list_display = ["title", "safe_content_display"]
    readonly_fields = ("bibliography",)

    def safe_content_display(self, obj):
        return safe_content(obj)

    safe_content_display.short_description = "Content"


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
    list_display = ["title", "safe_content_display"]
    autocomplete_fields = ["archive"]
    readonly_fields = ("bibliography",)
    filter_horizontal = ("films",)

    def safe_content_display(self, obj):
        return safe_content(obj)

    safe_content_display.short_description = "Content"


@admin.register(WrittenInfluences)
class WrittenInfluencesAdmin(admin.ModelAdmin):
    class Media:
        js = ("admin/js/mentionsPluginConfig.js",)

    search_fields = ["title"]
    list_display = ["title", "safe_content_display"]
    autocomplete_fields = ["archive"]
    readonly_fields = ("bibliography",)
    filter_horizontal = ("films",)

    def safe_content_display(self, obj):
        return safe_content(obj)

    safe_content_display.short_description = "Content"


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    search_fields = ["name"]
