# Generated by Django 4.2.5 on 2023-12-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0003_teaching_resources_etc"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="format_other",
            field=models.CharField(
                blank=True,
                help_text="Use this if you chose 'other'",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="format_type",
            field=models.CharField(
                choices=[
                    (9.5, "9.5 mm"),
                    (16, "16 mm"),
                    (35, "35 mm"),
                    (70, "70 mm"),
                    ("other", "Other"),
                ],
                default=35,
                max_length=5,
                verbose_name="format",
            ),
        ),
    ]
