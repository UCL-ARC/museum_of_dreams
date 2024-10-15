from django.core.exceptions import ValidationError
from django.db import models


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)


class BaseLinkModel(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        if self.url:
            return self.url
        else:
            return self.description

    url = models.URLField(
        blank=True,
        help_text="url to the item you'd like to link",
        max_length=500,
    )
    description = models.CharField(
        max_length=250,
        help_text="short description, required",
        null=False,
        blank=False,
    )
    film = models.ForeignKey(
        "Film", on_delete=models.CASCADE, related_name="%(class)ss", null=True
    )


class OtherLink(BaseLinkModel):
    class Meta:
        verbose_name = "Other Link"


class Source(BaseLinkModel):
    class Meta:
        verbose_name = "Source"

    film = models.ManyToManyField("Film", blank=True, related_name="sources")


class FileLink(BaseLinkModel):
    class Meta:
        abstract = True

    def upload_to(instance, filename):
        return f"files/{instance.__class__.__name__}/{filename}"

    def validate_max_size(file):
        # Set the maximum file size to 3gb
        max_size = 3 * 1024 * 1024 * 1024

        if file.size > max_size:
            raise ValidationError("The maximum file size that can be uploaded is 3GB")
        else:
            return file

    file = models.FileField(
        upload_to=upload_to,
        blank=True,
        null=True,
        validators=[
            validate_max_size,
        ],
    )


class Video(FileLink):
    class Meta:
        verbose_name = "Video"


class Script(FileLink):
    class Meta:
        verbose_name = "Script"


class PressBook(FileLink):
    class Meta:
        verbose_name = "Press Book"


class Programme(FileLink):
    class Meta:
        verbose_name = "Programme"


class Publicity(FileLink):
    class Meta:
        verbose_name = "Publicity Material"


class Still(FileLink):
    class Meta:
        verbose_name = "Still"


class Postcard(FileLink):
    class Meta:
        verbose_name = "Postcard"


class Poster(FileLink):
    class Meta:
        verbose_name = "Poster"


class Drawing(FileLink):
    class Meta:
        verbose_name = "Drawing"


class Location(models.Model):
    def __str__(self):
        return f"{self.address}"

    address = models.CharField(max_length=200)
    # could use a geo package for more specific stuff, might help with google maps
    associated_films = models.ManyToManyField(
        "Film", blank=True, related_name="locations"
    )

    is_setting = models.BooleanField(default=False)
