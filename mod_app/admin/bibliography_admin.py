from ckeditor.widgets import CKEditorWidget
import csv
from django import forms

from django.contrib import admin
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


def import_all_bibliography(file):
    """reads in csv file data and saves data as biliography(s) as django object(s)"""
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")  # delimiter subject to change
        next(reader)

        for row in reader:
            bibliography = BibliographyItem(
                short_citation=row[0], long_citation=row[1], annotation=row[2]
            )
            bibliography.save()
