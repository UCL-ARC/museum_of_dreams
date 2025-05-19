from typing import Dict, Tuple
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


def custom_inline(model, mixins: Tuple, options: Dict):
    base_classes = tuple(mixins) + (admin.TabularInline,)
    inline_class_name = f"{model.__name__}Inline"
    options.setdefault("model", model)
    inline_class_attrs = options

    inline = type(inline_class_name, base_classes, inline_class_attrs)

    return inline


common_filelink_class_inlines = []

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
    inline = custom_inline(
        model,
        mixins=(
            PreviewMixin,
            s3BrowserButtonMixin,
        ),
        options={
            "extra": 1,
            "classes": [
                "inline-inline",
                "grp-collaps",
                "grp-closed",
            ],
        },
    )

    common_filelink_class_inlines.append(inline)

video_inline = custom_inline(
    Video,
    mixins=(PreviewMixin,),
    options={
        "extra": 1,
        "classes": [
            "inline-inline",
            "grp-collapse",
            "grp-closed",
        ],
        "exclude": ("file",),
    },
)


class OtherLinkInline(PreviewMixin, admin.TabularInline):
    model = OtherLink
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
    exclude = ("archive",)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super(CardImageInline, self).formfield_for_dbfield(
            db_field, request, **kwargs
        )
        if db_field.name == "description":
            field.initial = "card header img"
        return field


# Registering models based off the Filelink abstract class
for model in [Video]:
    register_custom_admin(
        model=model,
        mixins=(PreviewMixin),
        search_fields=["description", "url"],
        list_display=["description", "film", "url", "preview"],
        autocomplete_fields=["archive"],
        inline=video_inline,
    )

for model in [CardImage]:
    register_custom_admin(
        model=model,
        mixins=(PreviewMixin, s3BrowserButtonMixin),
        search_fields=["description", "url"],
        list_display=["description", "film", "url", "preview"],
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
        inline=common_filelink_class_inlines,
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
