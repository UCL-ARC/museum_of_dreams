from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from .bibliography_model import BibliographyItem
from ..utils.extract_citations import update_bibliography


class ProjectNote(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=255, null=False)

    content = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here.",
    )

    bibliography = models.ManyToManyField(
        BibliographyItem,
        blank=True,
        related_name="project_notes",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, self.content)
