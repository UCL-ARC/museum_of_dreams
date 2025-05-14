from django.contrib import admin

from mod_app.models.film_model import Film
from mod_app.models.support_models import (
    CardImage,
    Drawing,
    Keyword,
    OtherLink,
    Postcard,
    Poster,
    PressBook,
    Programme,
    Publicity,
    PublicVisualInfluence,
    Script,
    Source,
    Still,
    Tag,
    Topic,
    Video,
)
from mod_app.admin.utils import register_custom_admin
from mod_app.utils.mixins import (
    PreviewMixin,
    s3BrowserButtonMixin,
)


class SourceInline(PreviewMixin, admin.TabularInline):
    model = Film.sources.through
    extra = 1
    classes = [
        "grp-collapse",
        "grp-closed",
    ]
    verbose_name = "Source"
    verbose_name_plural = "Sources of Adaptations"


class VideoInline(PreviewMixin, admin.TabularInline):
    model = Video
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]
    exclude = ("file",)


class ScriptInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = Script
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PressBookInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = PressBook
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class ProgrammeInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = Programme
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PublicityInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = Publicity
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class StillInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = Still
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PostcardInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = Postcard
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PosterInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = Poster
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class DrawingInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = Drawing
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class CardImageInline(PreviewMixin, s3BrowserButtonMixin, admin.TabularInline):
    model = CardImage
    extra = 1
    max_num = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]
    verbose_name_plural = "Card Image"

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super(CardImageInline, self).formfield_for_dbfield(
            db_field, request, **kwargs
        )
        if db_field.name == "description":
            field.initial = "card header img"
        return field


class PublicVisualInfluenceInline(
    PreviewMixin, s3BrowserButtonMixin, admin.TabularInline
):
    model = PublicVisualInfluence
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class OtherLinkInline(PreviewMixin, admin.TabularInline):
    model = OtherLink
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


# Registering models based off the Filelink abstract class
for model in [Video]:
    register_custom_admin(
        model=model,
        mixins=(PreviewMixin),
        search_fields=["description", "url"],
        list_display=["description", "film", "url", "preview"],
        autocomplete_fields=["archive"],
    )

for model in [CardImage]:
    register_custom_admin(
        model=model,
        mixins=(PreviewMixin, s3BrowserButtonMixin),
        search_fields=["description", "url"],
        list_display=["description", "film", "url", "preview"],
        exclude=["archive"],
    )

for model in [
    Script,
    PressBook,
    Programme,
    Publicity,
    Still,
    Postcard,
    Poster,
    Drawing,
    PublicVisualInfluence,
]:
    register_custom_admin(
        model=model,
        mixins=(PreviewMixin, s3BrowserButtonMixin),
        search_fields=["description", "url"],
        list_display=["description", "film", "file", "url", "preview"],
        autocomplete_fields=["archive"],
    )


@admin.register(Source)
class SourceAdmin(PreviewMixin, admin.ModelAdmin):
    def list_films(self, obj):
        return ", ".join([film.title for film in obj.film.all()])

    list_films.short_description = "Films"

    search_fields = ["description", "url", "film__title"]
    filter_horizontal = ("film",)
    exclude = ["is_source"]
    list_display = ["description", "list_films", "url", "preview"]


@admin.register(OtherLink)
class OtherLinkAdmin(PreviewMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "url", "preview"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name", "is_genre"]


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ["name"]
