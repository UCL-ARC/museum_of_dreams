from django.contrib import admin
from mod_app.utils.mixins import PreviewMixin

from ..models import *


class SourceInline(PreviewMixin, admin.TabularInline):
    model = Source
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class VideoInline(PreviewMixin, admin.TabularInline):
    model = Video
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class ScriptInline(PreviewMixin, admin.TabularInline):
    model = Script
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PressBookInline(PreviewMixin, admin.TabularInline):
    model = PressBook
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class ProgrammeInline(PreviewMixin, admin.TabularInline):
    model = Programme
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PublicityInline(PreviewMixin, admin.TabularInline):
    model = Publicity
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class StillInline(PreviewMixin, admin.TabularInline):
    model = Still
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PostcardInline(PreviewMixin, admin.TabularInline):
    model = Postcard
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PosterInline(PreviewMixin, admin.TabularInline):
    model = Poster
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class DrawingInline(PreviewMixin, admin.TabularInline):
    model = Drawing
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
