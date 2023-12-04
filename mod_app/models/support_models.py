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
        blank=True,
        help_text="Use this to expand on the condition, particularly if 'Other'",
    )

    entry_date = models.DateField(blank=True, null=True)  # maybe put on copy model

    duration = models.IntegerField(
        blank=True,
        null=True,
        help_text="Enter the run time in minutes.",
    )
    current_length = models.IntegerField(
        blank=True,
        null=True,
        help_text="Enter the run time in minutes.",
    )

    ELEMENT_CHOICES = [
        ("pos", "Scene positive"),
        ("ctn", "Negative coutertype"),
        ("intn", "Internegative"),
        ("lav", "Intermediate positive scene (lavender)"),
        ("olay", "Titles"),
    ]

    element = models.CharField(
        max_length=10,
        choices=ELEMENT_CHOICES,
        default="pos",
    )

    support = models.CharField(
        max_length=10,
        choices=[("S", "Safety"), ("N", "Nitrate")],
        default="S",
    )

    format_type = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="format"
    )

    rollers = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Number of rollers",
    )

    is_in_colour = models.BooleanField(
        default=False,
        verbose_name="in colour?",
        help_text="Check box in colour and leave blank if black and white (default)",
    )
    collection = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )  # could do this as choices potentially


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
