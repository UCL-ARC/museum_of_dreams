from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def build_and_send_email(request, obj, verb):
    updated_by = request.user.username

    devs = [user.username for user in User.objects.filter(groups__name="devs")]

    if updated_by in devs:
        return

    researchers = User.objects.filter(
        groups__name="Researchers", is_active=True
    ).exclude(username=updated_by)
    recipients = [user.email for user in researchers]

    instance_admin_url = request.build_absolute_uri()
    instance_url = request.build_absolute_uri(obj.get_absolute_url())

    website = settings.ENVIRONMENT

    subject = f"A {obj.__class__.__name__} has been {verb}! || MOD"

    html_message = render_to_string(
        "email_template_update.html",
        {
            "updated_by": updated_by,
            "instance": obj,
            "instance_admin_url": instance_admin_url,
            "instance_url": instance_url,
            "website": website,
        },
    )

    return send_mail(
        subject,
        "",
        "notifications@museumofdreamworlds.org",
        recipients,
        html_message=html_message,
        fail_silently=False,
    )
