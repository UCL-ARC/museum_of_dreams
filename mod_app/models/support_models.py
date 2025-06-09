from django.db import models


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=255, unique=True
    )  # this unique constrain is shared between tags and all of its child classes
    is_genre = models.BooleanField(default=True)


class Keyword(Tag):
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.is_genre = False
        super().save(*args, **kwargs)


class Topic(Tag):
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.is_genre = False
        super().save(*args, **kwargs)


class Archive(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)


class Location(models.Model):
    def __str__(self):
        return f"{self.address}"

    address = models.CharField(max_length=200)
    # could use a geo package for more specific stuff, might help with google maps
    associated_films = models.ManyToManyField(
        "Film", blank=True, related_name="locations"
    )

    is_setting = models.BooleanField(default=False)
