from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models import Case, When, CharField
from django.db.models.functions import Substr, Lower, Trim
from django.core.exceptions import ValidationError
from django.urls import reverse

from mod_app.models.support_models import (
    Tag,
)
from .bibliography_model import BibliographyItem
from mod_app.utils.extract_citations import update_bibliography


def validate_format_other(value, format_type):
    if format_type == "other" and not value:
        raise ValidationError("Please provide format details; you've selected 'other' ")


class FilmManager(models.Manager):
    def get_queryset(self):
        """Order films first by number, then alphabetically, discarding prefix if they start with 'The' or 'A'"""
        return (
            super()
            .get_queryset()
            .annotate(
                # annotate a field for sorting the title, ignoring "A " or "The "
                sort_title=Case(
                    # starts with "The"
                    When(
                        title__iregex=r"^The\s+",
                        then=Lower(Trim(Substr("title", 5))),
                    ),
                    # starts with "A"
                    When(
                        title__iregex=r"^A\s+",
                        then=Lower(Trim(Substr("title", 3))),
                    ),
                    # then other titles
                    default=Lower(Trim("title")),
                    output_field=CharField(),
                ),
            )
            .order_by("sort_title")
        )


class Film(models.Model):
    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("film_detail", kwargs={"pk": self.pk})

    objects = FilmManager()
    title = models.CharField(max_length=100)
    alt_titles = models.TextField(
        blank=True,
        null=True,
        help_text="Comma separated values, format as 'Filmname (Alternative),'",
    )
    release_date = models.IntegerField()

    production_country = models.CharField(max_length=50, blank=True, null=True)
    production_company = models.CharField(max_length=50, blank=True, null=True)

    synopsis = models.TextField(blank=True)

    genre = models.ManyToManyField(Tag, related_name="films", blank=True)

    bfi_category = models.CharField(
        max_length=100, blank=True, null=True
    )  # can use choices if preset

    cast = models.TextField(
        blank=True,
        null=True,
    )
    crew = models.TextField(blank=True, null=True, verbose_name="Credits")

    # Technical section

    duration = models.DecimalField(
        blank=True,
        null=True,
        max_digits=5,
        decimal_places=2,
        help_text="Enter the original run time in minutes. Please use a period (.) to denote fractions, eg. 10.5 meaning 10 mins 30 seconds",
    )
    current_length = models.DecimalField(
        blank=True,
        null=True,
        max_digits=5,
        decimal_places=2,
        help_text="Enter the run time of the BFI copy in minutes. Please use a period (.) to denote fractions, eg. 10.5 meaning 10 mins 30 seconds",
    )
    support = models.CharField(
        max_length=1,
        choices=[("V", "Viewable"), ("M", "Master")],
        default="V",
    )

    FORMAT_CHOICES = (
        ("9.5", "9.5 mm"),
        ("16", "16 mm"),
        ("35", "35 mm"),
        ("70", "70 mm"),
        ("other", "Other"),
    )

    format_type = models.CharField(
        max_length=5,
        default="35",
        verbose_name="format",
        choices=FORMAT_CHOICES,
    )
    format_other = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Use this if you chose 'other'",
    )

    is_in_colour = models.BooleanField(
        default=False,
        verbose_name="in colour?",
        help_text="Check box in colour and leave blank if black and white (default)",
    )
    print_comments = models.TextField(
        blank=True,
        help_text="Optional notes about the print/s. Mentions are available here and will contibute to the bibliography.",
        verbose_name="Notes on Prints",
    )

    # non-filmic section contains support models
    # comments + extras

    comments = RichTextUploadingField(
        blank=True, help_text="Internal comments between researchers"
    )
    temporary_images = RichTextUploadingField(blank=True, verbose_name="List images")

    bibliography = models.ManyToManyField(BibliographyItem, related_name="films")

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        validate_format_other(self.format_other, self.format_type)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        fields = [self.print_comments, self.comments, self.temporary_images]

        update_bibliography(self, fields)
