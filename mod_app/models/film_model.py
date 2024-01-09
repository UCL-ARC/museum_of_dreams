from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.core.exceptions import ValidationError

from mod_app.models.support_models import (
    Tag,
    Source,
    Video,
    Drawing,
    Poster,
    OtherLink,
    Script,
    PressBook,
    Programme,
    Publicity,
    Still,
    Postcard,
)
from .bibliography_model import BibliographyItem
from mod_app.utils.extract_citations import update_bibliography


def validate_format_other(value, format_type):
    if format_type == "other" and not value:
        raise ValidationError("Please provide format details; you've selected 'other' ")


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
    FORMAT_CHOICES = {
        ("9.5", "9.5 mm"),
        ("16", "16 mm"),
        ("35", "35 mm"),
        ("70", "70 mm"),
        ("other", "Other"),
    }
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
        help_text="Optional notes about the print/s",
        verbose_name="Notes on Prints",
    )

    # Non filmic section / extras

    comments = RichTextUploadingField(blank=True)
    temporary_images = RichTextUploadingField(blank=True)

    bibliography = models.ManyToManyField(BibliographyItem, related_name="films")

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        validate_format_other(self.format_other, self.format_type)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, self.print_comments)
