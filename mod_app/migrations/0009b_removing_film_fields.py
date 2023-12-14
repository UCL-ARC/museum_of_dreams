from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0009_remove_models"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="film",
            name="collection",
        ),
        migrations.RemoveField(
            model_name="film",
            name="element",
        ),
        migrations.RemoveField(
            model_name="film",
            name="entry_date",
        ),
        migrations.RemoveField(
            model_name="film",
            name="intertitle_photo",
        ),
        migrations.RemoveField(
            model_name="film",
            name="intertitle_text",
        ),
        migrations.RemoveField(
            model_name="film",
            name="rollers",
        ),
        migrations.RemoveField(
            model_name="film",
            name="source_material",
        ),
    ]
