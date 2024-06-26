# Generated by Django 4.2.5 on 2024-06-27 13:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0022_bibliographyitem_annotation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, help_text="Mentions are available here.", null=True
                    ),
                ),
                (
                    "bibliography",
                    models.ManyToManyField(
                        blank=True,
                        help_text="This field updates on save, and some items may not be visible immediately",
                        related_name="feedback",
                        to="mod_app.bibliographyitem",
                    ),
                ),
            ],
            options={
                "verbose_name": "Feedback",
            },
        ),
    ]
