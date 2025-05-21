from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from mod_app.models import BibliographyItem
from ..utils.extract_citations import update_bibliography


class VisualInfluences(models.Model):
    class Meta:
        verbose_name = "Visual Influence"
        verbose_name_plural = "Visual Influences"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255, null=False)
    films = models.ManyToManyField("Film", related_name="visual_influences", blank=True)
    archive = models.ManyToManyField(
        "Archive", related_name="visual_influence_archives", blank=True
    )

    content = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here.",
    )

    bibliography = models.ManyToManyField(
        BibliographyItem,
        blank=True,
        related_name="visual_influences",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, [self.content])


class WrittenInfluences(models.Model):
    class Meta:
        verbose_name = "Written Influence"
        verbose_name_plural = "Written Influences"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255, null=False)
    films = models.ManyToManyField(
        "Film", related_name="written_influences", blank=True
    )
    archive = models.ManyToManyField(
        "Archive", related_name="written_influence_archives", blank=True
    )

    content = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here.",
    )

    bibliography = models.ManyToManyField(
        BibliographyItem,
        blank=True,
        related_name="written_influences",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, [self.content])
