from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from ..utils.extract_citations import update_bibliography

from mod_app.models import Tag, Keyword, BibliographyItem


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
        return self.title

    def default_title():
        return f"Analysis {Analysis.objects.count() + 1}"

    title = models.CharField(max_length=255, default=default_title)

    content = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here and will contibute to the bibliography.",
    )

    films = models.ManyToManyField("Film", related_name="analyses", blank=True)

    topics = models.ManyToManyField(Tag, related_name="analysis_topics", blank=True)

    keywords = models.ManyToManyField(
        Keyword, related_name="analysis_keywords", blank=True
    )

    genre = models.ManyToManyField(Tag, related_name="analysis_genres", blank=True)

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

        update_bibliography(self, [self.content])


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

    topics = models.ManyToManyField(Tag, related_name="tr_topics", blank=True)

    keywords = models.ManyToManyField(Keyword, related_name="tr_keywords", blank=True)

    tags = models.ManyToManyField(Tag, related_name="tr_tags", blank=True)

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
