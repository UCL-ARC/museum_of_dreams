from django.db import models

from mod_app.models.support_models import FileLink, Link, Tag


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
        limit_choices_to={"link_type": "video"},
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

    ELEMENT_CHOICES = [
        ("pos", "Scene positive"),
        ("ctn", "Negative coutertype"),
        ("intn", "Internegative"),
        ("lav", "Intermediate positive scene (lavender)"),
        ("olay", "Titles"),
    ]

    element = models.CharField(
        max_length=4,
        choices=ELEMENT_CHOICES,
        default="pos",
    )

    support = models.CharField(
        max_length=1,
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
    COLLECTION_CHOICES = [
        ("tv", "Television"),
        ("feat", "Feature Films and Short Fiction"),
        ("silent", "Silent Film"),
        ("moving", "Artists' Moving Image"),
        ("nonfic", "Non-fiction"),
        ("special", "Special Collections"),
    ]
    collection = models.CharField(
        max_length=7, default="silent", choices=COLLECTION_CHOICES
    )
    PRINT_STAT_CHOICES = [
        ("good", "Good"),
        ("reasonable", "Reasonable"),
        ("poor", "Poor"),
        ("fragile", "Fragile"),
        ("other", "Other"),
    ]
    print_status = models.CharField(max_length=255, blank=True, null=True)
    print_status_comments = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional comments about the print's status",
    )

    entry_date = models.DateField(blank=True, null=True)

    # Non filmic section / extras

    intertitle_text = models.CharField(max_length=255, blank=True, null=True)
    intertitle_photo = models.ImageField(
        upload_to="images/intertitles/", blank=True, null=True
    )
    additional_links = models.ManyToManyField(
        Link,
        limit_choices_to={"link_type": "other"},
        help_text="Links to other things",
        related_name="other_links",
        blank=True,
    )
    scripts = models.ManyToManyField(
        FileLink,
        limit_choices_to={"link_type": "scripts"},
        help_text="Link to or upload script file(s)",
        related_name="scripts",
        blank=True,
    )
    press_books = models.ManyToManyField(
        FileLink,
        limit_choices_to={"link_type": "press_books"},
        help_text="Link to or upload press book file(s)",
        related_name="press_books",
        blank=True,
    )
    programmes = models.ManyToManyField(
        FileLink,
        limit_choices_to={"link_type": "programmes"},
        help_text="Link to or upload programme file(s)",
        related_name="programmes",
        blank=True,
    )
    pub_mat = models.ManyToManyField(
        FileLink,
        limit_choices_to={"link_type": "pub_mat"},
        verbose_name="Publicity Materials",
        help_text="Link to or upload publicity material file(s)",
        related_name="pub_material",
        blank=True,
    )

    stills = models.ManyToManyField(
        FileLink,
        limit_choices_to={"link_type": "stills"},
        help_text="Link to or upload stills",
        related_name="stills",
        blank=True,
    )
    postcards = models.ManyToManyField(
        FileLink,
        limit_choices_to={"link_type": "postcards"},
        help_text="Link to or upload postcards",
        related_name="postcards",
        blank=True,
    )
    posters = models.ManyToManyField(
        FileLink,
        limit_choices_to={"link_type": "posters"},
        help_text="Link to or upload posters",
        related_name="posters",
        blank=True,
    )
    drawings = models.ManyToManyField(
        FileLink,
        limit_choices_to={"link_type": "drawings"},
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
