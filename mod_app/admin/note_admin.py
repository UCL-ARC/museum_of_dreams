from django.contrib import admin
from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html


from mod_app.models import ProjectNote, Feedback


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
