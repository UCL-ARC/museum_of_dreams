# Generated by Django 4.2.5 on 2023-12-14 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0010a_creating_models"),
    ]

    operations = [
        # migrations.AddField(
        #     model_name="analysis",
        #     name="tags",
        #     field=models.ManyToManyField(
        #         blank=True, related_name="analysis_tags", to="mod_app.tag"
        #     ),
        # ),
        # migrations.AddField(
        #     model_name="analysis",
        #     name="topics",
        #     field=models.ManyToManyField(
        #         blank=True, related_name="topics", to="mod_app.tag"
        #     ),
        # ),
        # migrations.AddField(
        #     model_name="film",
        #     name="cast",
        #     field=models.TextField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name="film",
        #     name="print_comments",
        #     field=models.TextField(
        #         blank=True,
        #         help_text="Optional notes about the print/s",
        #         verbose_name="Notes on Prints",
        #     ),
        # ),
        # migrations.AddField(
        #     model_name="film",
        #     name="temporary_images",
        #     field=models.ImageField(blank=True, upload_to="temp/"),
        # ),
        migrations.RemoveField(
            model_name="analysis",
            name="film",
        ),
        # migrations.RemoveField(
        #     model_name="film",
        #     name="crew",
        # ),
        migrations.AlterField(
            model_name="film",
            name="current_length",
            field=models.IntegerField(
                blank=True,
                help_text="Enter the run time of the BFI copy in minutes.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="duration",
            field=models.IntegerField(
                blank=True,
                help_text="Enter the original run time in minutes.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="genre",
            field=models.ManyToManyField(
                blank=True, related_name="genres", to="mod_app.tag"
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="support",
            field=models.CharField(
                choices=[("V", "Viewable"), ("M", "Master")], default="V", max_length=1
            ),
        ),
        migrations.AlterField(
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
        migrations.AlterField(
            model_name="link",
            name="url",
            field=models.URLField(
                blank=True, help_text="url to the item you'd like to link"
            ),
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
            model_name="analysis",
            name="film",
            field=models.ManyToManyField(
                blank=True, related_name="films", to="mod_app.film"
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="crew",
            field=models.TextField(blank=True, null=True, verbose_name="Credits"),
        ),
        migrations.AlterField(
            model_name="film",
            name="drawings",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload drawings",
                related_name="drawings",
                to="mod_app.drawing",
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="postcards",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload postcards",
                related_name="postcards",
                to="mod_app.postcard",
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="posters",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload posters",
                related_name="posters",
                to="mod_app.poster",
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="press_books",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload press book file(s)",
                related_name="press_books",
                to="mod_app.pressbook",
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="programmes",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload programme file(s)",
                related_name="programmes",
                to="mod_app.programme",
            ),
        ),
        migrations.AlterField(
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
        migrations.AlterField(
            model_name="film",
            name="scripts",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload script file(s)",
                related_name="scripts",
                to="mod_app.script",
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="stills",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload stills",
                related_name="stills",
                to="mod_app.still",
            ),
        ),
    ]
