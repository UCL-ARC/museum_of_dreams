from ckeditor.fields import RichTextField
from django.db import models


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)


class Link(models.Model):
    def __str__(self):
        if self.url:
            return self.url
        else:
            return self.description

    url = models.URLField(blank=True, help_text="url to the item you'd like to link")
    description = models.CharField(
        max_length=250,
        help_text="short description of what the link is to (optional)",
        blank=True,
        null=True,
    )


class Source(Link):
    class Meta:
        verbose_name = "Source"

    is_source = models.BooleanField(default=True)


class FileLink(Link):
    def upload_to(instance, filename):
        return f"files/{instance.__class__.__name__}/{filename}"

    file = models.FileField(upload_to=upload_to, blank=True, null=True)


class Script(FileLink):
    class Meta:
        verbose_name = "Script"


class PressBook(FileLink):
    class Meta:
        verbose_name = "Press Book"


class Programme(FileLink):
    class Meta:
        verbose_name = "Programme"


class Publicity(FileLink):
    class Meta:
        verbose_name = "Publicity Material"


class Still(FileLink):
    class Meta:
        verbose_name = "Still"


class Postcard(FileLink):
    class Meta:
        verbose_name = "Postcard"


class Poster(FileLink):
    class Meta:
        verbose_name = "Poster"


class Drawing(FileLink):
    class Meta:
        verbose_name = "Drawing"


class Analysis(models.Model):
    class Meta:
        verbose_name_plural = "Analyses"

    def __str__(self):
        return f"Analysis of {self.film}"

    content = RichTextField(null=True)

    film = models.ManyToManyField("Film", related_name="films", blank=True)

    topics = models.ManyToManyField(Tag, related_name="topics", blank=True)

    tags = models.ManyToManyField(Tag, related_name="analysis_tags", blank=True)


class Location(models.Model):
    def __str__(self):
        return f"{self.address}"

    address = models.CharField(max_length=200)
    # could use a geo package for more specific stuff, might help with google maps
    associated_films = models.ManyToManyField("Film", blank=True)

    is_setting = models.BooleanField(default=False)
