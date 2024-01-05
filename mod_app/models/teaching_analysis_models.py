from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from ..utils.extract_citations import update_bibliography

from .support_models import Tag
from .bibliography_model import BibliographyItem


def display_list(list):
    if len(list) > 1:
        display_list = ", ".join(str(f) for f in list[:-1]) + f", and {list[-1]}"
    else:
        display_list = str(list[0])
    return display_list


class Analysis(models.Model):
    class Meta:
        verbose_name_plural = "Analyses"

    def __str__(self):
        if self.title:
            return self.title
        else:
            films = self.films.all()
            flist = display_list(films)
            return f"Analysis of {flist}"

    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional title for the analysis if you don't want it to be 'Analysis of (film)'",
    )

    content = RichTextUploadingField(null=True, blank=True)

    films = models.ManyToManyField("Film", related_name="analyses", blank=True)

    topics = models.ManyToManyField(Tag, related_name="analysis_topics", blank=True)

    tags = models.ManyToManyField(Tag, related_name="analysis_tags", blank=True)

    holdings = models.CharField(max_length=400, blank=True, null=True)

    work_history = models.TextField(blank=True)

    teaching_resources = models.ManyToManyField(
        "TeachingResources", related_name="analyses", blank=True
    )
    bibliography = models.ManyToManyField(
        BibliographyItem,
        related_name="analyses",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, self.content)


class TeachingResources(models.Model):
    class Meta:
        verbose_name_plural = "Teaching Resources"

    def __str__(self):
        if self.title:
            return self.title
        elif self.films:
            films = self.films.all()
            flist = display_list(films)
            return f"Teaching Resources for {flist}"
        else:
            return f"Teaching Resource {self.pk}"

    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional title",
    )
    material = RichTextUploadingField(null=True, blank=True)

    films = models.ManyToManyField("Film", related_name="trs", blank=True)

    topics = models.ManyToManyField(Tag, related_name="tr_topics", blank=True)

    tags = models.ManyToManyField(Tag, related_name="tr_tags", blank=True)

    bibliography = models.ManyToManyField(
        BibliographyItem,
        related_name="teaching_resources",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, self.material)
