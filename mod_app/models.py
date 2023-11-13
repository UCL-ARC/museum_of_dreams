from django.db import models
from django.db.models.signals import m2m_changed


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)


class Link(models.Model):
    def __str__(self):
        return self.path

    path = models.URLField()
    description = models.CharField(
        max_length=250,
        help_text="short description of what the link is to (optional)",
        blank=True,
        null=True,
    )


class Copy(Link):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return super().__str__()

    name = models.CharField(
        max_length=100,
        help_text="optional name/title for the copy",
        blank=True,
    )

    CONDITION_CHOICES = [
        ("good", "Good"),
        ("reasonable", "Reasonable"),
        ("poor", "Poor"),
        ("fragile", "Fragile"),
        ("other", "Other"),
    ]

    condition = models.CharField(
        max_length=10,
        choices=CONDITION_CHOICES,
        default="reasonable",
    )

    condition_comments = models.TextField(
        help_text="Use this to expand on the condition, particularly if 'Other'"
    )


class Analysis(models.Model):
    def __str__(self):
        return f"Analysis of {self.film}"

    text = models.TextField()
    film = models.ForeignKey(
        "Film", on_delete=models.DO_NOTHING, related_name="analyses"
    )


class Actor(models.Model):
    def __str__(self):
        return f"{self.name}"

    name = models.CharField(max_length=100)
    birth_place = models.ForeignKey(
        "Location", on_delete=models.SET_DEFAULT, default=None, blank=True, null=True
    )
    tags = models.ManyToManyField(Tag, related_name="actor_tags")
    about = models.TextField(blank=True)


class Film(models.Model):
    def __str__(self):
        return f"{self.title}"

    title = models.CharField(max_length=100)
    release_date = models.IntegerField()  # can be more specific and use DateField()
    alt_titles = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    actors = models.ManyToManyField("Actor", related_name="films", blank=True)

    locations = models.ManyToManyField(
        "Location",
        blank=True,
    )
    setting_location = locations.filter(is_setting=True)
    filmed_location = locations.filter(is_setting=False)

    genre = models.ManyToManyField(Tag, related_name="genres")
    themes = models.ManyToManyField(Tag, related_name="themes")

    run_time = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Run time in Minutes",
        help_text="Enter the run time in minutes.",
    )

    copies = models.ManyToManyField(
        Copy,
        help_text="Links to where the copies can be found",
        related_name="copies",
        blank=True,
        null=True,
    )
    source_material = models.OneToOneField(
        Link,
        help_text="Link to the source material",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    video = models.OneToOneField(
        Link,
        help_text="Link to the video file",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    additional_links = models.ManyToManyField(
        Link,
        help_text="Links to other things",
        related_name="other_links",
        blank=True,
        null=True,
    )
    # files = models.FileField(upload_to=)

    summary = models.TextField(blank=True)
    comments = models.TextField(blank=True)


class Location(models.Model):
    def __str__(self):
        return f"{self.address}"

    address = models.CharField(max_length=200)
    # could use a geo package for more specific stuff, might help with google maps
    associated_actors = models.ManyToManyField("Actor", blank=True)
    associated_films = models.ManyToManyField("Film", blank=True)

    is_setting = models.BooleanField(default=False)


def update_actors_films(sender, instance, action, reverse, pk_set, **kwargs):
    if action == "post_add" and not reverse:
        for pk in pk_set:
            actor = Actor.objects.get(pk=pk)
            actor.films.add(instance)


m2m_changed.connect(update_actors_films, sender=Film.actors.through)
