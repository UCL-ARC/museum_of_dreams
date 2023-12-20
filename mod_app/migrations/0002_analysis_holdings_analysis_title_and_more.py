# Generated by Django 4.2.5 on 2023-12-15 12:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0001c_new_link_models"),
    ]

    operations = [
        migrations.AddField(
            model_name="analysis",
            name="holdings",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name="analysis",
            name="title",
            field=models.CharField(
                blank=True,
                help_text="Optional title for the analysis if you don't want it to be 'Analysis of (film)'",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="analysis",
            name="work_history",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.RenameField(
            model_name="analysis",
            old_name="film",
            new_name="films",
        ),
    ]