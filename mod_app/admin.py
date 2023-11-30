from django import forms
from django.contrib import admin
from .models import Actor, Film, Location, Analysis, Link, Copy, Tag, Crew


class FilmInline(admin.StackedInline):
    model = Film.actors.through
    extra = 1

    def __str__(self):
        return self.film.title


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


admin.site.register([Film, Location, Link, Copy, Tag, Crew])

# Customised
admin.site.register(Actor, ActorAdmin)
admin.site.register(Analysis, AnalysisAdmin)
