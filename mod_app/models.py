from django.db import models
from django.db.models.signals import m2m_changed

from ckeditor.fields import RichTextField


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
    class Meta:
        verbose_name_plural = "Copies"

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
    class Meta:
        verbose_name_plural = "Analyses"

    def __str__(self):
        return f"Analysis of {self.film}"

    content = RichTextField()
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


class Crew(models.Model):
    class Meta:
        verbose_name_plural = "Crew Members"

    def __str__(self):
        return f"{self.name}"

    ROLE_CHOICES = [
        ("Director", "Director"),
        ("Screenplay", "Screenplay"),
        ("Scenography", "Scenography"),
        ("Photography", "Photography"),
    ]

    name = models.CharField(max_length=100)
    roles = models.CharField(max_length=255, choices=ROLE_CHOICES, blank=True)

    def get_roles(self):
        return self.roles.split(",") if self.roles else []

    def set_roles(self, roles):
        self.roles = ",".join(roles)


class Film(models.Model):
    def __str__(self):
        return f"{self.title}"

    title = models.CharField(max_length=100)
    alt_titles = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Comma separated values, can be 'Original: Filmname,' or 'Filmname (Original),'",
    )
    release_date = models.IntegerField()  # can be more specific and use DateField()

    production_country = models.CharField(max_length=50, blank=True, null=True)
    production_company = models.CharField(max_length=50, blank=True, null=True)

    synopsis = models.TextField(blank=True)

    source_material = models.OneToOneField(
        Link,
        help_text="Link to the source material",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="source_material_link",
    )
    genre = models.ManyToManyField(Tag, related_name="genres")
    bfi_category = models.CharField(
        max_length=100, blank=True, null=True
    )  # can use choices if preset

    actors = models.ManyToManyField(
        "Actor", related_name="films", blank=True, verbose_name="Cast"
    )
    crew = models.ManyToManyField("Crew", related_name="films", blank=True)

    intertitle_text = models.CharField(max_length=255, blank=True, null=True)
    intertitle_photo = models.ImageField(
        upload_to="intertitles/", blank=True, null=True
    )

    # Technical section

    duration = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Run time in Minutes",
        help_text="Enter the run time in minutes.",
    )
    current_length = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Run time in Minutes",
        help_text="Enter the run time in minutes.",
    )
    # element
    # support
    format_type = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="format"
    )

    rollers = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Number of  rollers",
    )

    is_in_colour = models.BooleanField(
        default=False,
        help_text="Select true if in colour and false if black and white (default)",
    )
    collection = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )  # could do this as choices potentially, maybe put on copy model

    copies = models.ManyToManyField(
        Copy,
        help_text="Links to where the copies can be found",
        related_name="copies",
        blank=True,
    )

    entry_date = models.DateField(blank=True, null=True)  # maybe put on copy model

    video = models.OneToOneField(
        Link,
        help_text="Link to the video file",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="video_link",
    )
    additional_links = models.ManyToManyField(
        Link,
        help_text="Links to other things",
        related_name="other_links",
        blank=True,
    )
    # archive_id = models.CharField(max_length=20)
    # archive_company = models.CharField(
    #     max_length=20
    # )  # maybe use choices instead if only small selection
    # files = models.FileField(upload_to=)

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
