from django.utils.html import format_html
from django.core.mail import send_mail


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


class EmailMixin:
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Check if it's a new instance or an update
        if change:
            print(
                "changed:", obj.__class__.__name__, request.path, obj.get_absolute_url()
            )
            # Send email notification for update
            # send_mail(
            #     f"{obj} Updated",
            #     f'"{obj}" has been updated by {request.user}. Click ',
            #     "sender@example.com",
            #     ["recipient@example.com"],
            #     fail_silently=False,
            # )
