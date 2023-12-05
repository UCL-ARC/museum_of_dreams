from ckeditor.fields import RichTextField
from django.db import models


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)


class Link(models.Model):
    def __str__(self):
        return self.url

    url = models.URLField(blank=True)
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
        help_text="Use this to expand on the condition, particularly if 'Other'",
        blank=True,
    )


class Analysis(models.Model):
    class Meta:
        verbose_name_plural = "Analyses"

    def __str__(self):
        return f"Analysis of {self.film}"

    content = RichTextField(null=True)
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
    tags = models.ManyToManyField(Tag, related_name="actor_tags", blank=True)
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


class Location(models.Model):
    def __str__(self):
        return f"{self.address}"

    address = models.CharField(max_length=200)
    # could use a geo package for more specific stuff, might help with google maps
    associated_actors = models.ManyToManyField("Actor", blank=True)
    associated_films = models.ManyToManyField("Film", blank=True)

    is_setting = models.BooleanField(default=False)
