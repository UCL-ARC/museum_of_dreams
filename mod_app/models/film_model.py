from django.db import models

from mod_app.models.support_models import (
    Drawing,
    FileLink,
    Link,
    Postcard,
    Poster,
    PressBook,
    Programme,
    Publicity,
    Script,
    Still,
    Tag,
)


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

    source = models.OneToOneField(
        Link,
        help_text="Link to the source material",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="source_link",
    )
    genre = models.ManyToManyField(Tag, related_name="genres", blank=True)

    bfi_category = models.CharField(
        max_length=100, blank=True, null=True
    )  # can use choices if preset

    cast = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    crew = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Credits"
    )

    video = models.OneToOneField(
        Link,
        help_text="Link to the video file",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="video_link",
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
    support = models.CharField(
        max_length=1,
        choices=[("V", "Viewable"), ("M", "Master")],
        default="V",
    )
    format_type = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="format"
    )
    is_in_colour = models.BooleanField(
        default=False,
        verbose_name="in colour?",
        help_text="Check box in colour and leave blank if black and white (default)",
    )
    print_comments = models.TextField(
        max_length=255,
        blank=True,
        help_text="Optional notes about the print/s",
        verbose_name="Notes on Prints",
    )

    # Non filmic section / extras

    additional_links = models.ForeignKey(
        Link,
        on_delete=models.SET_NULL,
        help_text="Links to other things",
        related_name="other_links",
        blank=True,
        null=True,
    )
    scripts = models.ForeignKey(
        Script,
        on_delete=models.SET_NULL,
        help_text="Link to or upload script file(s)",
        related_name="scripts",
        blank=True,
        null=True,
    )
    press_books = models.ForeignKey(
        PressBook,
        on_delete=models.SET_NULL,
        help_text="Link to or upload press book file(s)",
        related_name="press_books",
        blank=True,
        null=True,
    )
    programmes = models.ForeignKey(
        Programme,
        on_delete=models.SET_NULL,
        help_text="Link to or upload programme file(s)",
        related_name="programmes",
        blank=True,
        null=True,
    )
    pub_mat = models.ForeignKey(
        Publicity,
        on_delete=models.SET_NULL,
        verbose_name="Publicity Materials",
        help_text="Link to or upload publicity material file(s)",
        related_name="pub_material",
        blank=True,
        null=True,
    )

    stills = models.ForeignKey(
        Still,
        on_delete=models.SET_NULL,
        help_text="Link to or upload stills",
        related_name="stills",
        blank=True,
        null=True,
    )
    postcards = models.ForeignKey(
        Postcard,
        on_delete=models.SET_NULL,
        help_text="Link to or upload postcards",
        related_name="postcards",
        blank=True,
        null=True,
    )
    posters = models.ForeignKey(
        Poster,
        on_delete=models.SET_NULL,
        help_text="Link to or upload posters",
        related_name="posters",
        blank=True,
        null=True,
    )
    drawings = models.ForeignKey(
        Drawing,
        on_delete=models.SET_NULL,
        help_text="Link to or upload drawings",
        related_name="drawings",
        blank=True,
        null=True,
    )

    # archive_id = models.CharField(max_length=20)
    # archive_company = models.CharField(
    #     max_length=20
    # )  # maybe use choices instead if only small selection

    comments = models.TextField(blank=True)

    # bibliographies...how?
