from django import forms
from django.contrib import admin
from django.db import models

from .models import *
from ckeditor.widgets import CKEditorWidget


class FilmAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }
    fieldsets = (
        (
            "Main Information (Filmic Section)",
            {
                "fields": (
                    "title",
                    "release_date",
                    "alt_titles",
                    "production_country",
                    "production_company",
                    "synopsis",
                    "source_material",
                    "genre",
                    "bfi_category",
                    "actors",
                    "crew",
                    "intertitle_text",
                    "intertitle_photo",
                ),
            },
        ),
        (
            "Technical Section",
            {
                "fields": ("copies",),
            },
        ),
        (
            "Additional Information (non filmic)",
            {
                "fields": (
                    "video",
                    "additional_links",
                    "scripts",
                    "press_books",
                    "programmes",
                    "pub_mat",
                    "stills",
                    "postcards",
                    "posters",
                    "drawings",
                    "comments",
                ),
            },
        ),
    )


# this allows adding of films from an actor's page
class FilmInline(admin.TabularInline):
    model = Film.actors.through
    extra = 1


class ActorAdmin(admin.ModelAdmin):
    inlines = (FilmInline,)


class AnalysisAdminForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"class": "ckeditor"}),
        }


class AnalysisAdmin(admin.ModelAdmin):
    form = AnalysisAdminForm


admin.site.register([Location, Tag, Copy, Crew, FileLink])

# Customised
admin.site.register(Actor, ActorAdmin)
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(Film, FilmAdmin)
