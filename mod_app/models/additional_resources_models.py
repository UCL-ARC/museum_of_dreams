from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from ..utils.extract_citations import update_bibliography

from mod_app.models import Topic, BibliographyItem


class TeachingResources(models.Model):
    class Meta:
        verbose_name_plural = "Teaching Resources"

    def __str__(self):
        return self.title

    def default_title():
        return f"Teaching Resources bundle{TeachingResources.objects.count() + 1}"

    title = models.CharField(max_length=255, default=default_title)
    material = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here and will contibute to the bibliography.",
    )

    films = models.ManyToManyField("Film", related_name="trs", blank=True)

    topics = models.ManyToManyField(
        Topic, related_name="teaching_resources", blank=True
    )

    bibliography = models.ManyToManyField(
        BibliographyItem,
        related_name="teaching_resources",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    clips = models.ManyToManyField(
        "Video",
        related_name="tr_clips",
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, [self.material])


class ExhibitionResources(models.Model):
    class Meta:
        verbose_name_plural = "Exhibition Resources"

    def __str__(self):
        return self.title

    def default_title():
        return f"Exhibition Resources {ExhibitionResources.objects.count() + 1}"

    title = models.CharField(max_length=255, default=default_title)
    material = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here and will contibute to the bibliography.",
    )

    films = models.ManyToManyField(
        "Film", related_name="exhibition_resources", blank=True
    )

    topics = models.ManyToManyField(
        Topic, related_name="exhibition_resources", blank=True
    )

    bibliography = models.ManyToManyField(
        BibliographyItem,
        related_name="exhibition_resources",
        help_text="This field updates on save, and some items may not be visible immediately",
    )


class EditedCollection(models.Model):
    def __str__(self):
        return self.title

    def default_title():
        return f"Edited Collection {EditedCollection.objects.count() + 1}"

    title = models.CharField(max_length=255, default=default_title)
    material = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here and will contibute to the bibliography.",
    )
    films = models.ManyToManyField(
        "Film", related_name="edited_collections", blank=True
    )

    topics = models.ManyToManyField(
        Topic, related_name="edited_collections", blank=True
    )

    bibliography = models.ManyToManyField(
        BibliographyItem,
        related_name="edited_collections",
        help_text="This field updates on save, and some items may not be visible immediately",
    )
