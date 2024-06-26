# Generated by Django 4.2.5 on 2024-07-01 13:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mod_app", "0023_add_feedback_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bibliographyitem",
            name="full_citation",
            field=ckeditor.fields.RichTextField(
                help_text="Please use Harvard reference list style. Examples: Author surname, initial. (year). 'Title of article/book/website/photograph'. Available at: URL or DOI where applicable (date accessed). Please note that the website or photo title should be italicised. For more detailed information and examples visit: https://www5.open.ac.uk/library/referencing-and-plagiarism/quick-guide-to-harvard-referencing-cite-them-right",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="bibliographyitem",
            name="short_citation",
            field=models.CharField(
                help_text="Please use Harvard in-text citation style. Examples: (Author surname, year), or in the case of up to 3 authors: (Author 1 surname, Author 2 surname, Author 3 surname, year), or in the case or more than 3 authors: (Author 1 surname, et al., year) ",
                max_length=200,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="format_type",
            field=models.CharField(
                choices=[
                    ("9.5", "9.5 mm"),
                    ("16", "16 mm"),
                    ("35", "35 mm"),
                    ("70", "70 mm"),
                    ("other", "Other"),
                ],
                default="35",
                max_length=5,
                verbose_name="format",
            ),
        ),
        migrations.AlterField(
            model_name="projectnote",
            name="bibliography",
            field=models.ManyToManyField(
                blank=True,
                help_text="This field updates on save, and some items may not be visible immediately",
                related_name="project_notes",
                to="mod_app.bibliographyitem",
            ),
        ),
    ]
