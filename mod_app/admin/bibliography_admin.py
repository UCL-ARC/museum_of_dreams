import csv
import io

from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin, messages
from django.shortcuts import redirect
from django.utils.html import format_html

from ..models import BibliographyItem


class BIAdminForm(forms.ModelForm):
    class Meta:
        model = BibliographyItem
        fields = "__all__"
        widgets = {
            "full_citation": CKEditorWidget(),
        }


@admin.register(BibliographyItem)
class BibliographyItemAdmin(admin.ModelAdmin):
    model = BibliographyItem
    list_display = ["safe_citation", "safe_annotation"]
    form = BIAdminForm
    search_fields = ["full_citation", "annotation"]
    change_list_template = "../templates/admin/bibliography_change_list.html"

    def safe_citation(self, obj):
        return format_html(obj.full_citation)

    def safe_annotation(self, obj):
        if obj.annotation is not None:
            return format_html(obj.annotation)
        else:
            return ""

    safe_citation.allow_tags = True
    safe_citation.short_description = "Full Citation"
    safe_citation.admin_order_field = "full_citation"
    safe_annotation.allow_tags = True
    safe_annotation.short_description = "Annotations"
    safe_annotation.admin_order_field = "annotation"

    # overiding django admin's changelist_view
    def changelist_view(self, request):
        if request.method == "POST" and request.FILES.get("csv_file"):
            csv_file = request.FILES["csv_file"]

            if not csv_file.name.endswith(".csv"):
                self.message_user(
                    request, "This is not a CSV file", level=messages.ERROR
                )
                return redirect(request.path)

            created_count, skipped_count = import_all_bibliography(csv_file)

            self.message_user(
                request,
                f"{created_count} bibliography successfully created.",
                level=messages.SUCCESS,
            )
            self.message_user(
                request,
                f"{skipped_count} items skipped" ,
                level=messages.WARNING,
            )
            return redirect(request.path)

        return super().changelist_view(request)


def import_all_bibliography(csv_file):
    """reads in csv file data and saves data as biliography(s) as django object(s)"""
    data_set = csv_file.read().decode("UTF-8")
    io_string = io.StringIO(data_set)
    next(io_string)

    created_count = 0
    skipped_count = 0
    for row in csv.reader(io_string, delimiter=";", quotechar='"'):
        _, created = BibliographyItem.objects.get_or_create(
            short_citation=row[0].strip(),
            full_citation=row[1].strip(),
            annotation="",
        )
        if created:
            created_count += 1
        else:
            skipped_count += 1

    return created_count,skipped_count
