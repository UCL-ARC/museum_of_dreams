from django.contrib import admin
from mod_app.utils.mixins import PreviewMixin

from ..models import *


class SourceInline(admin.TabularInline, PreviewMixin):
    model = Source
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class VideoInline(admin.TabularInline, PreviewMixin):
    model = Video
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class ScriptInline(admin.TabularInline, PreviewMixin):
    model = Script
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class PressBookInline(admin.TabularInline, PreviewMixin):
    model = PressBook
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class ProgrammeInline(admin.TabularInline, PreviewMixin):
    model = Programme
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class PublicityInline(admin.TabularInline, PreviewMixin):
    model = Publicity
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class StillInline(admin.TabularInline, PreviewMixin):
    model = Still
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class PostcardInline(admin.TabularInline, PreviewMixin):
    model = Postcard
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class PosterInline(admin.TabularInline, PreviewMixin):
    model = Poster
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class DrawingInline(admin.TabularInline, PreviewMixin):
    model = Drawing
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields += ("preview",)


class OtherLinkInline(admin.TabularInline, PreviewMixin):
    model = OtherLink
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    exclude = ["is_source"]
    list_display = ["description", "film", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(OtherLink)
class OtherLinkAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(PressBook)
class PressBookAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Publicity)
class PublicityAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Still)
class StillAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Postcard)
class PostcardAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin, PreviewMixin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]
    readonly_fields = ("preview",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
