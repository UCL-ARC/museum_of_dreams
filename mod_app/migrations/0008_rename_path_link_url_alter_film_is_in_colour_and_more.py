# Generated by Django 4.2.5 on 2023-12-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0007_filelink_alter_film_intertitle_photo_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="link",
            old_name="path",
            new_name="url",
        ),
        migrations.AlterField(
            model_name="film",
            name="is_in_colour",
            field=models.BooleanField(
                default=False,
                help_text="Check box in colour and leave blank if black and white (default)",
                verbose_name="in colour?",
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="rollers",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Number of rollers"
            ),
        ),
    ]