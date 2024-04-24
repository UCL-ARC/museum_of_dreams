from django.template.loader import get_template
from django.utils.html import format_html


class PreviewMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)

    def preview(self, obj):
        if hasattr(obj, "file") and obj.file:
            return self.file_preview(obj)
        elif hasattr(obj, "url") and obj.url:
            return self.link_preview(obj)
        else:
            return "-"

    def file_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-width: 15rem;" />',
            obj.file.url,
        )

    def link_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-width: 15rem;" />',
            obj.url,
        )


class s3BrowserButtonMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("s3_browser_button",)

    def s3_browser_button(self, obj):
        button_html = get_template("components/s3_browse_button.html")
        return button_html.render()
