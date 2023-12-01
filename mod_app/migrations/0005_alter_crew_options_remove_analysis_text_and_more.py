# Generated by Django 4.2.5 on 2023-11-30 15:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mod_app", "0004_crew_rename_run_time_film_duration_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="crew",
            options={"verbose_name_plural": "Crew Members"},
        ),
        migrations.RemoveField(
            model_name="analysis",
            name="text",
        ),
        migrations.AddField(
            model_name="analysis",
            name="content",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="film",
            name="collection",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="film",
            name="current_length",
            field=models.IntegerField(
                blank=True,
                help_text="Enter the run time in minutes.",
                null=True,
                verbose_name="Run time in Minutes",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="entry_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="film",
            name="format_type",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="format"
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="is_in_colour",
            field=models.BooleanField(
                default=False,
                help_text="Select true if in colour and false if black and white (default)",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="rollers",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Number of  rollers"
            ),
        ),
    ]
