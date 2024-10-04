# Generated by Django 4.2.5 on 2024-10-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0024_fix_migrations"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drawing",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="otherlink",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="postcard",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="poster",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="pressbook",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="publicity",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="script",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.RemoveField(
            model_name="source",
            name="film",
        ),
        migrations.AlterField(
            model_name="source",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="still",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="url to the item you'd like to link",
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name="source",
            name="film",
            field=models.ManyToManyField(
                blank=True, related_name="sources", to="mod_app.film"
            ),
        ),
    ]
