from django.contrib import admin


from ..models import *


class SourceInline(admin.TabularInline):
    model = Source
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class ScriptInline(admin.TabularInline):
    model = Script
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PressBookInline(admin.TabularInline):
    model = PressBook
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class ProgrammeInline(admin.TabularInline):
    model = Programme
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PublicityInline(admin.TabularInline):
    model = Publicity
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class StillInline(admin.TabularInline):
    model = Still
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PostcardInline(admin.TabularInline):
    model = Postcard
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class PosterInline(admin.TabularInline):
    model = Poster
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class DrawingInline(admin.TabularInline):
    model = Drawing
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


class OtherLinkInline(admin.TabularInline):
    model = OtherLink
    extra = 1
    classes = [
        "inline-inline",
        "grp-collapse",
        "grp-closed",
    ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]
    exclude = ["is_source"]


@admin.register(OtherLink)
class OtherLinkAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(PressBook)
class PressBookAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Publicity)
class PublicityAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Still)
class StillAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Postcard)
class PostcardAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
