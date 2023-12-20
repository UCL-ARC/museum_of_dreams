from django import forms
from django.contrib import admin
from django.forms import inlineformset_factory


from ..models import *


class SourceInlineForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = "__all__"


class ScriptInline(forms.ModelForm):
    class Meta:
        model = Source
        fields = "__all__"


class PressBookInline(forms.ModelForm):
    class Meta:
        model = Source
        fields = "__all__"


class ProgrammeInline(admin.TabularInline):
    model = Programme
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


class PublicityInline(admin.TabularInline):
    model = Publicity
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


class StillInline(admin.TabularInline):
    model = Still
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


class PostcardInline(admin.TabularInline):
    model = Postcard
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


class PosterInline(admin.TabularInline):
    model = Poster
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


class DrawingInline(admin.TabularInline):
    model = Drawing
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
    ]
    insert_after = "bfi_category"


class OtherLinkInline(admin.TabularInline):
    model = OtherLink
    extra = 1
    classes = [
        "grp-collapse",
        "grp-open",
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
