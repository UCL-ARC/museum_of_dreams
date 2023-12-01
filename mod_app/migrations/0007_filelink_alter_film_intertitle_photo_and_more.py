# Generated by Django 4.2.5 on 2023-12-01 11:13

from django.db import migrations, models
import django.db.models.deletion
import mod_app.models.support_models


class Migration(migrations.Migration):

    dependencies = [
        (
            "mod_app",
            "0006_film_element_film_support_alter_film_current_length_and_more",
        ),
    ]

    operations = [
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
        migrations.AlterField(
            model_name="film",
            name="intertitle_photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/intertitles/"
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="is_in_colour",
            field=models.BooleanField(
                default=False,
                help_text="Select true if in colour and false if black and white (default)",
                verbose_name="in colour?",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="drawings",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload drawings",
                related_name="drawings",
                to="mod_app.filelink",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="postcards",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload postcards",
                related_name="postcards",
                to="mod_app.filelink",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="posters",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload posters",
                related_name="posters",
                to="mod_app.filelink",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="press_books",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload press book file(s)",
                related_name="press_books",
                to="mod_app.filelink",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="programmes",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload programme file(s)",
                related_name="programmes",
                to="mod_app.filelink",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="pub_mat",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload publicity material file(s)",
                related_name="pub_material",
                to="mod_app.filelink",
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
                to="mod_app.filelink",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="stills",
            field=models.ManyToManyField(
                blank=True,
                help_text="Link to or upload stills",
                related_name="stills",
                to="mod_app.filelink",
            ),
        ),
    ]
