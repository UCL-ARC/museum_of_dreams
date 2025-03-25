from bs4 import BeautifulSoup
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
        if request.method == "POST" and request.FILES.get("html-file"):
            html_file = request.FILES["html-file"]
            if not html_file.name.endswith(".html") or not html_file.name.endswith(".htm"):
                self.message_user(
                    request, "This is not a valid html file", level=messages.ERROR
                )
                return redirect(request.path)
            try:
                created_count, skipped_count = import_from_html(html_file)
            except Exception as e:
                self.message_user(e, level=messages.ERROR)
                return redirect(request.path)

            self.message_user(
                request,
                f"{created_count} bibliography successfully created.",
                level=messages.SUCCESS,
            )
            if skipped_count:
                self.message_user(
                    request,
                    f"{skipped_count} items skipped",
                    level=messages.WARNING,
                )
            return redirect(request.path)

        return super().changelist_view(request)


def import_from_html(html_file):
    """Extract and create bibliography items from html table"""

    created_count = 0
    skipped_count = 0

    soup = BeautifulSoup(html_file, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) != 2:
            raise ValueError()
        bibliography = [col.decode_contents() for col in cols]
        _, created = BibliographyItem.objects.get_or_create(
            short_citation=bibliography[0],
            full_citation=bibliography[1],
            annotation="",
        )
        if created:
            created_count += 1
        else:
            skipped_count += 1

    return created_count, skipped_count
