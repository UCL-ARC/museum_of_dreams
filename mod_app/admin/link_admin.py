from django.contrib import admin
from mod_app.utils.mixins import PreviewMixin, s3BrowserButtonMixin

from mod_app.models import *


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


class OtherLinkInline(PreviewMixin, admin.TabularInline):
    model = OtherLink
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


@admin.register(Video)
class VideoAdmin(PreviewMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "url", "preview"]


@admin.register(Source)
class SourceAdmin(PreviewMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    exclude = ["is_source"]
    list_display = ["description", "film", "url", "preview"]


@admin.register(OtherLink)
class OtherLinkAdmin(PreviewMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "url", "preview"]


@admin.register(Script)
class ScriptAdmin(PreviewMixin, s3BrowserButtonMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]


@admin.register(PressBook)
class PressBookAdmin(PreviewMixin, s3BrowserButtonMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]


@admin.register(Publicity)
class PublicityAdmin(PreviewMixin, s3BrowserButtonMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]


@admin.register(Programme)
class ProgrammeAdmin(PreviewMixin, s3BrowserButtonMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]


@admin.register(Still)
class StillAdmin(PreviewMixin, s3BrowserButtonMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]


@admin.register(Postcard)
class PostcardAdmin(PreviewMixin, s3BrowserButtonMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]


@admin.register(Poster)
class PosterAdmin(PreviewMixin, s3BrowserButtonMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]


@admin.register(Drawing)
class DrawingAdmin(PreviewMixin, s3BrowserButtonMixin, admin.ModelAdmin):
    search_fields = ["description", "url"]
    list_display = ["description", "film", "file", "url", "preview"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
