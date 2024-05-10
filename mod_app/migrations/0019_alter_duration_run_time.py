# Generated by Django 4.2.5 on 2024-03-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0018_alter_alt_titles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="film",
            name="current_length",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Enter the run time of the BFI copy in minutes. Please use a period (.) to denote fractions, eg. 10.5 meaning 10 mins 30 seconds",
                max_digits=5,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="duration",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Enter the original run time in minutes. Please use a period (.) to denote fractions, eg. 10.5 meaning 10 mins 30 seconds",
                max_digits=5,
                null=True,
            ),
        ),
    ]
