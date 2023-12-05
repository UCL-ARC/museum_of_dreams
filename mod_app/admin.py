from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.db import models

from .models import *


# class FilmInline(admin.StackedInline):
#     model = Film.actors.through
#     extra = 1

#     def __str__(self):
#         return self.film.title


# class ActorAdmin(admin.ModelAdmin):
#     inlines = (FilmInline,)


class LinkAdminForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = "__all__"
        # widgets = {
        #     "link_type": forms.HiddenInput(),
        # }

    def __init__(self, *args, **kwargs):
        # Extract field name from request or provide a default
        field_name = kwargs.pop("field_name", "default_field_name")
        print(field_name)
        super().__init__(*args, **kwargs)

        # Set initial value for link_type based on the field_name
        self.fields["link_type"].initial = field_name


class FileLinkAdminForm(LinkAdminForm):
    class Meta:
        model = FileLink
        fields = "__all__"
        # widgets = {
        #     "link_type": forms.HiddenInput(),
        # }


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    search_fields = ["description", "url"]
    form = LinkAdminForm


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(FileLink)
class FileLinkAdmin(admin.ModelAdmin):
    form = FileLinkAdminForm
    search_fields = ["description", "url"]

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)

    #     if obj is None:
    #         url_parts = request.path.split("/")
    #         field_name = url_parts[-2]

    #         if field_name:
    #             form.base_fields["link_type"].initial = field_name

    #     return form


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "genre",
        "additional_links",
        "scripts",
        "press_books",
        "programmes",
        "pub_mat",
        "stills",
        "postcards",
        "posters",
        "drawings",
    ]
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
                    "cast",
                    "crew",
                    "video",
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
                    "print_status",
                    "print_status_comments",
                    "entry_date",
                ),
            },
        ),
        (
            "Additional Information (non filmic)",
            {
                "fields": (
                    "intertitle_text",
                    "intertitle_photo",
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

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        film_id = request.resolver_match.kwargs.get("object_id")

        fields_to_filter = [
            "additional_links",
            "scripts",
            "press_books",
            "programmes",
            "pub_mat",
            "stills",
            "postcards",
            "posters",
            "drawings",
        ]
        # filter so only for this film instance shows
        if db_field.name in fields_to_filter:
            kwargs["queryset"] = FileLink.objects.filter(
                **{f"{db_field.related_query_name()}__id": film_id}
            )

        return super().formfield_for_manytomany(db_field, request, **kwargs)


class AnalysisAdminForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"class": "ckeditor"}),
        }


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    form = AnalysisAdminForm


# admin.site.register([Location])

# Customised
# admin.site.register(Analysis, AnalysisAdmin)
# admin.site.register(Film, FilmAdmin)
