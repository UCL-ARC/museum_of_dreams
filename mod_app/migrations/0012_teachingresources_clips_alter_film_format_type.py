# Generated by Django 4.2.5 on 2024-01-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0011_make_descriptions_required"),
    ]

    operations = [
        migrations.AddField(
            model_name="teachingresources",
            name="clips",
            field=models.ManyToManyField(
                null=True, related_name="tr_clips", to="mod_app.video"
            ),
        ),
    ]
