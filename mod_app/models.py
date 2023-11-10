from django.db import models
from django.db.models.signals import m2m_changed

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Actor(models.Model):
    def __str__(self):
        return f"{self.name}"

    name = models.CharField(max_length=100)
    birth_place = models.ForeignKey(
        "Location",
        on_delete=models.SET_DEFAULT,
        default=None,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='actor_tags')
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
    actors = models.ManyToManyField("Actor",related_name="films", blank=True)
    locations = models.ManyToManyField("Location", blank=True)

    genre = models.ManyToManyField(Tag, related_name='genres')
    themes = models.ManyToManyField(Tag, related_name='themes')
    summary = models.TextField(blank=True)
    comments = models.TextField(blank=True)


class Location(models.Model):
    def __str__(self):
        return f"{self.address}"

    address = models.CharField(max_length=200)
    # could use a geo package for more specific stuff, might help with google maps
    associated_actors = models.ManyToManyField("Actor", blank=True)
    associated_films = models.ManyToManyField("Film", blank=True)






def update_actors_films(sender, instance, action, reverse, pk_set, **kwargs):
    if action == 'post_add' and not reverse:
        for pk in pk_set:
            actor = Actor.objects.get(pk=pk)
            actor.films.add(instance)

m2m_changed.connect(update_actors_films, sender=Film.actors.through)