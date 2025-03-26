# Generated by Django 4.2.5 on 2025-03-19 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0032_publicvisualinfluence_cardimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Keyword",
            fields=[
                (
                    "tag_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.tag",
                    ),
                ),
            ],
            bases=("mod_app.tag",),
        ),
        migrations.AddField(
            model_name="analysis",
            name="genre",
            field=models.ManyToManyField(
                blank=True, related_name="analysis_genres", to="mod_app.tag"
            ),
        ),
        migrations.AddField(
            model_name="tag",
            name="is_genre",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="analysis",
            name="keywords",
            field=models.ManyToManyField(
                blank=True, related_name="analysis_keywords", to="mod_app.keyword"
            ),
        ),
        migrations.AddField(
            model_name="teachingresources",
            name="keywords",
            field=models.ManyToManyField(
                blank=True, related_name="tr_keywords", to="mod_app.keyword"
            ),
        ),
    ]
