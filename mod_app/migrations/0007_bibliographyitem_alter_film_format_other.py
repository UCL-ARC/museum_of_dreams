# Generated by Django 4.2.5 on 2023-12-21 14:41

import ckeditor.fields
from django.db import migrations, models
import mod_app.models.film_model


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0006_related_name_changes"),
    ]

    operations = [
        migrations.CreateModel(
            name="BibliographyItem",
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
                ("short_citation", models.CharField(max_length=200, null=True)),
                ("full_citation", ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]
