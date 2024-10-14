from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from mod_app.models import BibliographyItem
from ..utils.extract_citations import update_bibliography


class Feedback(models.Model):
    class Meta:
        verbose_name = "Feedback on non-academic Activities"
        verbose_name_plural = "Feedbacks on non-academic Activities"

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
        related_name="feedback",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, [self.content])
