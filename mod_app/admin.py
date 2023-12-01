from django import forms
from django.contrib import admin

from .models import *


class FilmAdmin(admin.ModelAdmin):
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
                "fields": (
                    "duration",
                    "current_length",
                    "element",
                    "support",
                    "format_type",
                    "rollers",
                    "is_in_colour",
                    "collection",
                    "copies",
                    "entry_date",
                ),
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
