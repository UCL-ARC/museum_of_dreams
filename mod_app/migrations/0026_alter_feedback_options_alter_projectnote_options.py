# Generated by Django 4.2.5 on 2024-11-11 11:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0025_increase_url_length_make_sources_m2m"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="feedback",
            options={
                "verbose_name": "Feedback on non-academic Activities",
                "verbose_name_plural": "Feedbacks on non-academic Activities",
            },
        ),
        migrations.AlterModelOptions(
            name="projectnote",
            options={"verbose_name": "Research Framework"},
        ),
    ]
