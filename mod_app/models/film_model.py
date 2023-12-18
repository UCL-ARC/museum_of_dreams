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
    Source,
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

    source = models.ManyToManyField(
        Source,
        help_text="Link to the source material",
        blank=True,
        limit_choices_to={"is_source": True},
        related_name="source_link",
    )
    genre = models.ManyToManyField(Tag, related_name="genres", blank=True)

    bfi_category = models.CharField(
        max_length=100, blank=True, null=True
    )  # can use choices if preset

    cast = models.TextField(
        blank=True,
        null=True,
    )
    crew = models.TextField(blank=True, null=True, verbose_name="Credits")

    video = models.ForeignKey(
        FileLink,
        help_text="Link or upload the video file",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="video_link",
    )

    # Technical section

    duration = models.IntegerField(
        blank=True,
        null=True,
        help_text="Enter the original run time in minutes.",
    )
    current_length = models.IntegerField(
        blank=True,
        null=True,
        help_text="Enter the run time of the BFI copy in minutes.",
    )
    support = models.CharField(
        max_length=1,
        choices=[("V", "Viewable"), ("M", "Master")],
        default="V",
    )
    # FORMAT_CHOICES = {
    #     (9.5, "9.5 mm"),
    #     (16, "16 mm"),
    #     (35, "35 mm"),
    #     (70, "70 mm"),
    # }
    format_type = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="format"
    )  # use choices + other
    is_in_colour = models.BooleanField(
        default=False,
        verbose_name="in colour?",
        help_text="Check box in colour and leave blank if black and white (default)",
    )
    print_comments = models.TextField(
        blank=True,
        help_text="Optional notes about the print/s",
        verbose_name="Notes on Prints",
    )

    # Non filmic section / extras

    additional_links = models.ManyToManyField(
        Link,
        help_text="Links to other things",
        related_name="other_links",
        blank=True,
    )
    scripts = models.ManyToManyField(
        Script,
        help_text="Link to or upload script file(s)",
        related_name="scripts",
        blank=True,
    )
    press_books = models.ManyToManyField(
        PressBook,
        help_text="Link to or upload press book file(s)",
        related_name="press_books",
        blank=True,
    )
    programmes = models.ManyToManyField(
        Programme,
        help_text="Link to or upload programme file(s)",
        related_name="programmes",
        blank=True,
    )
    pub_mat = models.ManyToManyField(
        Publicity,
        verbose_name="Publicity Materials",
        help_text="Link to or upload publicity material file(s)",
        related_name="pub_material",
        blank=True,
    )

    stills = models.ManyToManyField(
        Still,
        help_text="Link to or upload stills",
        related_name="stills",
        blank=True,
    )
    postcards = models.ManyToManyField(
        Postcard,
        help_text="Link to or upload postcards",
        related_name="postcards",
        blank=True,
    )
    posters = models.ManyToManyField(
        Poster,
        help_text="Link to or upload posters",
        related_name="posters",
        blank=True,
    )
    drawings = models.ManyToManyField(
        Drawing,
        help_text="Link to or upload drawings",
        related_name="drawings",
        blank=True,
    )

    comments = models.TextField(blank=True)
    temporary_images = models.ImageField(blank=True, upload_to="temp/")
