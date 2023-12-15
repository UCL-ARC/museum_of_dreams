from django import forms
from django.contrib import admin

from .models import *


class SourceAdminForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = "__all__"


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]
    form = SourceAdminForm
    readonly_fields = ("is_source",)


@admin.register(FileLink)
class FileLinkAdmin(admin.ModelAdmin):
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
