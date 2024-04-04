from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
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


class EmailMixin:
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Check if it's a new instance or an update
        if change:
            print(
                "changed:", obj.__class__.__name__, request.path, obj.get_absolute_url()
            )
            researchers = User.objects.filter(groups__name="Researchers")
            recipients = [user.email for user in researchers]
            subject = "A Film has been updated! || MOD"
            updated_by = request.user.username
            for researcher in researchers:
                html_message = render_to_string(
                    "email_template.html", {"updated_by": updated_by, "instance": obj}
                )
                print(html_message)
            # Send email notification for update
            # send_mail(
            #     f"{obj} Updated",
            #     f'"{obj}" has been updated by {request.user}. Click ',
            #     "sender@example.com",
            #     ["recipient@example.com"],
            #     fail_silently=False,
            # )
