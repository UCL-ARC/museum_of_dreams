# Generated by Django 4.2.5 on 2024-11-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0026_alter_feedback_options_alter_projectnote_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="bfi_identifier",
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
