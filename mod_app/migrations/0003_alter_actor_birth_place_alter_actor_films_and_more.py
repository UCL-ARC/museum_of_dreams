# Generated by Django 4.2.5 on 2023-10-30 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mod_app", "0002_actor_films_actor_tags_film_tags_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="birth_place",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="mod_app.location",
            ),
        ),
        migrations.AlterField(
            model_name="actor",
            name="films",
            field=models.ManyToManyField(blank=True, to="mod_app.film"),
        ),
        migrations.AlterField(
            model_name="film",
            name="actors",
            field=models.ManyToManyField(blank=True, to="mod_app.actor"),
        ),
        migrations.AlterField(
            model_name="film",
            name="locations",
            field=models.ManyToManyField(blank=True, to="mod_app.location"),
        ),
        migrations.AlterField(
            model_name="location",
            name="associated_actors",
            field=models.ManyToManyField(blank=True, to="mod_app.actor"),
        ),
        migrations.AlterField(
            model_name="location",
            name="associated_films",
            field=models.ManyToManyField(blank=True, to="mod_app.film"),
        ),
    ]
