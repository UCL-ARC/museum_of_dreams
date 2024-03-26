# Generated by Django 4.2.5 on 2024-03-21 14:50

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0019_alter_duration_run_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="film",
            name="temporary_images",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, verbose_name="List images"
            ),
        ),
    ]
