# Generated by Django 4.2.5 on 2023-12-14 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0012_make_models_m2m"),
    ]

    operations = [
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
            ],
            options={
                "verbose_name": "Source",
            },
            bases=("mod_app.link",),
        ),
        migrations.AddField(
            model_name="Source",
            name="is_source",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="film",
            name="additional_links",
            field=models.ManyToManyField(
                blank=True,
                help_text="Links to other things",
                related_name="other_links",
                to="mod_app.link",
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="source",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"is_source": True},
                help_text="Link to the source material",
                related_name="source_link",
                to="mod_app.source",
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
    ]
