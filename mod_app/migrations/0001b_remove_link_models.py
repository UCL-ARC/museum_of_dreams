# Generated by Django 4.2.5 on 2023-12-18 14:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="film",
            name="additional_links",
        ),
        migrations.RemoveField(
            model_name="film",
            name="drawings",
        ),
        migrations.RemoveField(
            model_name="film",
            name="postcards",
        ),
        migrations.RemoveField(
            model_name="film",
            name="posters",
        ),
        migrations.RemoveField(
            model_name="film",
            name="press_books",
        ),
        migrations.RemoveField(
            model_name="film",
            name="programmes",
        ),
        migrations.RemoveField(
            model_name="film",
            name="pub_mat",
        ),
        migrations.RemoveField(
            model_name="film",
            name="scripts",
        ),
        migrations.RemoveField(
            model_name="film",
            name="source",
        ),
        migrations.RemoveField(
            model_name="film",
            name="stills",
        ),
        migrations.RemoveField(
            model_name="film",
            name="video",
        ),
        migrations.DeleteModel(name="Link"),
        migrations.DeleteModel(name="Drawing"),
        migrations.DeleteModel(name="Postcard"),
        migrations.DeleteModel(name="Poster"),
        migrations.DeleteModel(name="PressBook"),
        migrations.DeleteModel(name="Programme"),
        migrations.DeleteModel(name="Publicity"),
        migrations.DeleteModel(name="Script"),
        migrations.DeleteModel(name="Still"),
        migrations.DeleteModel(name="Source"),
        migrations.DeleteModel(name="FileLink"),
    ]
