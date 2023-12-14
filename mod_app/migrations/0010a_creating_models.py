from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0009b_removing_film_fields"),
    ]

    operations = [
        migrations.CreateModel(
            name="Drawing",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Drawing",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Postcard",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Postcard",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Poster",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Poster",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="PressBook",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Press Book",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Programme",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Programme",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Publicity",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Publicity Material",
            },
            bases=("mod_app.filelink",),
        ),
        migrations.CreateModel(
            name="Script",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Script",
            },
            bases=("mod_app.filelink",),
        ),
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
                ("is_source", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Source",
            },
            bases=("mod_app.link",),
        ),
        migrations.CreateModel(
            name="Still",
            fields=[
                (
                    "filelink_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mod_app.filelink",
                    ),
                ),
            ],
            options={
                "verbose_name": "Still",
            },
            bases=("mod_app.filelink",),
        ),
    ]
