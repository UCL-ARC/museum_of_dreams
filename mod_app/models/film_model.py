from django.db import models
from django.db.models.signals import m2m_changed


from mod_app.models.support_models import Link, Tag, Copy, FileLink


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
    release_date = models.IntegerField()

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
        upload_to="images/intertitles/", blank=True, null=True
    )

    # Technical section

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
    )  # could do this as choices potentially, maybe put on copy model

    copies = models.ManyToManyField(
        Copy,
        help_text="Links to where the copies can be found",
        related_name="copies",
        blank=True,
    )

    entry_date = models.DateField(blank=True, null=True)  # maybe put on copy model

    # Non filmic section / extras

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
    scripts = models.ManyToManyField(
        FileLink,
        help_text="Link to or upload script file(s)",
        related_name="scripts",
        blank=True,
    )
    press_books = models.ManyToManyField(
        FileLink,
        help_text="Link to or upload press book file(s)",
        related_name="press_books",
        blank=True,
    )
    programmes = models.ManyToManyField(
        FileLink,
        help_text="Link to or upload programme file(s)",
        related_name="programmes",
        blank=True,
    )
    pub_mat = models.ManyToManyField(
        FileLink,
        verbose_name="Publicity Materials",
        help_text="Link to or upload publicity material file(s)",
        related_name="pub_material",
        blank=True,
    )

    stills = models.ManyToManyField(
        FileLink,
        help_text="Link to or upload stills",
        related_name="stills",
        blank=True,
    )
    postcards = models.ManyToManyField(
        FileLink,
        help_text="Link to or upload postcards",
        related_name="postcards",
        blank=True,
    )
    posters = models.ManyToManyField(
        FileLink,
        help_text="Link to or upload posters",
        related_name="posters",
        blank=True,
    )
    drawings = models.ManyToManyField(
        FileLink,
        help_text="Link to or upload drawings",
        related_name="drawings",
        blank=True,
    )

    # archive_id = models.CharField(max_length=20)
    # archive_company = models.CharField(
    #     max_length=20
    # )  # maybe use choices instead if only small selection

    comments = models.TextField(blank=True)

    # bibliographies...how?


def update_actors_films(sender, instance, action, reverse, pk_set, **kwargs):
    from mod_app.models import Actor

    if action == "post_add" and not reverse:
        for pk in pk_set:
            actor = Actor.objects.get(pk=pk)
            actor.films.add(instance)


m2m_changed.connect(update_actors_films, sender=Film.actors.through)
