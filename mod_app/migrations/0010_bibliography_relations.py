# Generated by Django 4.2.5 on 2024-01-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0009_alter_film_format_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="analysis",
            name="bibliography",
            field=models.ManyToManyField(
                related_name="analyses",
                to="mod_app.bibliographyitem",
                help_text="This field updates on save, and some items may not be visible immediately",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="bibliography",
            field=models.ManyToManyField(
                related_name="films", to="mod_app.bibliographyitem"
            ),
        ),
        migrations.AddField(
            model_name="teachingresources",
            name="bibliography",
            field=models.ManyToManyField(
                related_name="teaching_resources",
                to="mod_app.bibliographyitem",
                help_text="This field updates on save, and some items may not be visible immediately",
            ),
        ),
    ]
