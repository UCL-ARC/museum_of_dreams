from django.conf import settings
from django.template.loader import get_template
from django.utils.html import format_html


from .shared_functions import build_and_send_email


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
        print("link preview:", obj.__class__.__name__)
        if obj.__class__.__name__ == "Video":
            return format_html(
                '<div><iframe src="{}" frameborder="0"  scrolling="no" allowfullscreen></iframe></div>',
                obj.url,
            )
        elif obj.__class__.__name__ == "Source":
            return format_html(
                '<a href="{}">{}</a>',
                obj.url,
                obj.url,
            )
        else:
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


class EmailMixin:
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if settings.ENVIRONMENT != "local":
            # Check if it's a new instance or an update
            if change:
                build_and_send_email(request, obj, "updated")
            else:
                # new instance
                build_and_send_email(request, obj, "added")

    def delete_model(self, request, obj):
        if settings.ENVIRONMENT != "local":
            build_and_send_email(request, obj, "deleted")
            super().delete_model(request, obj)
