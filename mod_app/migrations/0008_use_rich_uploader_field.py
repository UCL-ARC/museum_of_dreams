# Generated by Django 4.2.5 on 2024-01-03 15:13

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0007_bibliographyitem_alter_film_format_other"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysis",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="comments",
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name="film",
            name="temporary_images",
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name="teachingresources",
            name="material",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]