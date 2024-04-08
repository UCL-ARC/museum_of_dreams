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
            updated_by = request.user.username
            researchers = User.objects.filter(groups__name="Researchers").exclude(
                username=updated_by
            )
            # recipients = [user.email for user in researchers]
            recipients = ["a.ho-lyn@ucl.ac.uk"]
            subject = f"A {obj.__class__.__name__} has been updated! || MOD"

            instance_url = request.build_absolute_uri()
            html_message = render_to_string(
                "email_template.html",
                {
                    "updated_by": updated_by,
                    "instance": obj,
                    "instance_url": instance_url,
                },
            )
            send_mail(
                subject,
                "",
                "notifications@mail.museumofdreamworlds.org",
                recipients,
                html_message=html_message,
            )
