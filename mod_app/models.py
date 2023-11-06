from django.db import models
from taggit.managers import TaggableManager


class Actor(models.Model):
    def __str__(self):
        return f"{self.name}"

    name = models.CharField(max_length=100)
    films = models.ManyToManyField("Film", blank=True)
    birth_place = models.ForeignKey(
        "Location",
        on_delete=models.SET_DEFAULT,
        default=None,
        blank=True,
        null=True
    )
    tags = TaggableManager(blank=True)
    about = models.TextField(blank=True)


class Analysis(models.Model):
    def __str__(self):
        return f"Analysis of {self.film}"

    text = models.TextField()
    film = models.ForeignKey(
        "Film", on_delete=models.DO_NOTHING, related_name="analyses"
    )


class Film(models.Model):
    def __str__(self):
        return f"{self.title}"

    title = models.CharField(max_length=100)
    release_date = models.IntegerField()  # can be more specific and use DateField()
    actors = models.ManyToManyField("Actor", blank=True)
    locations = models.ManyToManyField("Location", blank=True)
    tags = TaggableManager(blank=True)
    # themes = TaggableManager(blank=True) # need to make custom base
    summary = models.TextField(blank=True)


class Location(models.Model):
    def __str__(self):
        return f"{self.address}"

    address = models.CharField(max_length=200)
    # could use a geo package for more specific stuff, might help with google maps
    associated_actors = models.ManyToManyField("Actor", blank=True)
    associated_films = models.ManyToManyField("Film", blank=True)
