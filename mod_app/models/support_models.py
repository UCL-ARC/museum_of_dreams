from ckeditor.fields import RichTextField
from django.db import models


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)


class Link(models.Model):
    def __str__(self):
        return self.url

    url = models.URLField(blank=True, help_text="url to the item you'd like to link")
    description = models.CharField(
        max_length=250,
        help_text="short description of what the link is to (optional)",
        blank=True,
        null=True,
    )


class FileLink(Link):
    def upload_to(instance, filename):
        return f"files/{instance.related_name}/{filename}"

    file = models.FileField(upload_to=upload_to, blank=True, null=True)


class Analysis(models.Model):
    class Meta:
        verbose_name_plural = "Analyses"

    def __str__(self):
        return f"Analysis of {self.film}"

    content = RichTextField(null=True)

    film = models.ManyToManyField("Film", related_name="films", blank=True, null=True)

    topics = models.ManyToManyField(Tag, related_name="topics", blank=True, null=True)

    tags = models.ManyToManyField(
        Tag, related_name="analysis_tags", blank=True, null=True
    )


class Location(models.Model):
    def __str__(self):
        return f"{self.address}"

    address = models.CharField(max_length=200)
    # could use a geo package for more specific stuff, might help with google maps
    associated_films = models.ManyToManyField("Film", blank=True)

    is_setting = models.BooleanField(default=False)
