from ckeditor.widgets import CKEditorWidget
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
    list_display = ["safe_citation", "annotation"]
    form = BIAdminForm

    def safe_citation(self, obj):
        return format_html(obj.full_citation)

    safe_citation.allow_tags = True
    safe_citation.short_description = "Full Citation"
    safe_citation.admin_order_field = "full_citation"
