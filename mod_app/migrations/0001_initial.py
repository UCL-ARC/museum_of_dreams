# Generated by Django 4.2.5 on 2023-12-14 14:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mod_app.models.support_models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Film",
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
                ("title", models.CharField(max_length=100)),
                (
                    "alt_titles",
                    models.CharField(
                        blank=True,
                        help_text="Comma separated values, can be 'Original: Filmname,' or 'Filmname (Original),'",
                        max_length=200,
                        null=True,
                    ),
                ),
                ("release_date", models.IntegerField()),
                (
                    "production_country",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "production_company",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("synopsis", models.TextField(blank=True)),
                (
                    "bfi_category",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("cast", models.TextField(blank=True, null=True)),
                (
                    "crew",
                    models.TextField(blank=True, null=True, verbose_name="Credits"),
                ),
                (
                    "duration",
                    models.IntegerField(
                        blank=True,
                        help_text="Enter the original run time in minutes.",
                        null=True,
                    ),
                ),
                (
                    "current_length",
                    models.IntegerField(
                        blank=True,
                        help_text="Enter the run time of the BFI copy in minutes.",
                        null=True,
                    ),
                ),
                (
                    "support",
                    models.CharField(
                        choices=[("V", "Viewable"), ("M", "Master")],
                        default="V",
                        max_length=1,
                    ),
                ),
                (
                    "format_type",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="format"
                    ),
                ),
                (
                    "is_in_colour",
                    models.BooleanField(
                        default=False,
                        help_text="Check box in colour and leave blank if black and white (default)",
                        verbose_name="in colour?",
                    ),
                ),
                (
                    "print_comments",
                    models.TextField(
                        blank=True,
                        help_text="Optional notes about the print/s",
                        verbose_name="Notes on Prints",
                    ),
                ),
                ("comments", models.TextField(blank=True)),
                ("temporary_images", models.ImageField(blank=True, upload_to="temp/")),
            ],
        ),
        migrations.CreateModel(
            name="Link",
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
                (
                    "url",
                    models.URLField(
                        blank=True, help_text="url to the item you'd like to link"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="short description of what the link is to (optional)",
                        max_length=250,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="FileLink",
            fields=[
                (
                    "link_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.link",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=mod_app.models.support_models.FileLink.upload_to,
                    ),
                ),
            ],
            bases=("mod_app.link",),
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "link_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.link",
                    ),
                ),
                ("is_source", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Source",
            },
            bases=("mod_app.link",),
        ),
        migrations.CreateModel(
            name="Location",
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
                ("address", models.CharField(max_length=200)),
                ("is_setting", models.BooleanField(default=False)),
                (
                    "associated_films",
                    models.ManyToManyField(blank=True, to="mod_app.film"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="film",
            name="genre",
            field=models.ManyToManyField(
                blank=True, related_name="genres", to="mod_app.tag"
            ),
        ),
        migrations.CreateModel(
            name="Analysis",
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
                ("content", ckeditor.fields.RichTextField(null=True)),
                (
                    "film",
                    models.ManyToManyField(
                        blank=True, related_name="films", to="mod_app.film"
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="analysis_tags", to="mod_app.tag"
                    ),
                ),
                (
                    "topics",
                    models.ManyToManyField(
                        blank=True, related_name="topics", to="mod_app.tag"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Analyses",
            },
        ),
        migrations.CreateModel(
            name="Drawing",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Drawing",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Postcard",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Postcard",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Poster",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Poster",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="PressBook",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Press Book",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Programme",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Programme",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Publicity",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Publicity Material",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Script",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Script",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Still",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Still",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.AddField(
            model_name="film",
            name="source",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to the source material",
                limit_choices_to={"is_source": True},
                related_name="source_link",
                to="mod_app.source",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="drawings",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload drawings",
                related_name="drawings",
                to="mod_app.drawing",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="postcards",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload postcards",
                related_name="postcards",
                to="mod_app.postcard",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="posters",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload posters",
                related_name="posters",
                to="mod_app.poster",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="press_books",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload press book file(s)",
                related_name="press_books",
                to="mod_app.pressbook",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="programmes",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload programme file(s)",
                related_name="programmes",
                to="mod_app.programme",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="pub_mat",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload publicity material file(s)",
                related_name="pub_material",
                to="mod_app.publicity",
                verbose_name="Publicity Materials",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="scripts",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload script file(s)",
                related_name="scripts",
                to="mod_app.script",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="stills",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload stills",
                related_name="stills",
                to="mod_app.still",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="additional_links",
            field=models.ManyToManyField(
                blank=True,
                help_text="Links to other things",
                related_name="other_links",
                to="mod_app.link",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="video",
            field=models.ForeignKey(
                blank=True,
                help_text="Link or upload the video file",
                limit_choices_to={"video_link__isnull": False},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="video_link",
                to="mod_app.filelink",
            ),
        ),
    ]
