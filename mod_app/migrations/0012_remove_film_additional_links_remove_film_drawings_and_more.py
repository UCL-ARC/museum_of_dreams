# # Generated by Django 4.2.5 on 2023-12-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0011_filelink_link_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filelink",
            name="link_type",
            field=models.CharField(
                choices=[
                    ("scripts", "Scripts"),
                    ("press_books", "Press Books"),
                    ("programmes", "Programmes"),
                    ("pub_mat", "Publicity Materials"),
                    ("stills", "Stills"),
                    ("postcards", "Postcards"),
                    ("posters", "Posters"),
                    ("drawings", "Drawings"),
                    ("other", "Other"),
                ],
                default="other",
                max_length=50,
            ),
        ),
    ]
