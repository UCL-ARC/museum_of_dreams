import re
from html import unescape

from bs4 import BeautifulSoup
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin, messages
from django.shortcuts import redirect
from django.utils.html import format_html, strip_tags

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
            if not html_file.name.endswith(".html") or html_file.name.endswith(".htm"):
                self.message_user(
                    request, "This is not a valid html file", level=messages.ERROR
                )
                return redirect(request.path)
            try:
                created_count, skipped_count = import_from_html(html_file)
            except Exception as e:
                self.message_user(request, e, level=messages.ERROR)
                return redirect(request.path)

            self.message_user(
                request,
                f"{created_count} bibliography item(s) successfully created.",
                level=messages.SUCCESS,
            )
            if skipped_count:
                self.message_user(
                    request,
                    f"{skipped_count} item(s) not created because they already exist",
                    level=messages.WARNING,
                )
            return redirect(request.path)

        return super().changelist_view(request)


def clean_style(soup_html_data):
    """remove unwanted styling from <span> html tags"""
    styles_to_remove = ["color", "font-family", "font-size"]

    for span in soup_html_data.find_all("span"):
        if "style" in span.attrs:
            styles = span["style"].split(";")

            # retain styles like italics and bold
            filtered_styles = [
                s
                for s in styles
                if not any(
                    s.strip().startswith(style_to_remove)
                    for style_to_remove in styles_to_remove
                )
            ]
            # replace old style with cleaned style
            cleaned_style = ";".join(filtered_styles).strip()
            if cleaned_style:
                span["style"] = cleaned_style
            else:
                del span["style"]
    return soup_html_data


def normalise_text(input_text):
    """get_text() and strip_tags() give slightly different outputs regarding whitespace, this should normalise it"""
    # Decode HTML entities
    decoded_text = unescape(input_text)
    # Normalize whitespace to a single space
    normalized_text = re.sub(r"\s+", " ", decoded_text)
    # Trim leading and trailing whitespace
    normalized_text = normalized_text.strip()
    return normalized_text


def import_from_html(html_file):
    """Extract and create bibliography items from html table"""

    created_count = 0
    skipped_count = 0

    soup = BeautifulSoup(html_file, "html.parser")
    table = soup.find("table")

    # remove unwanted format style
    rows = clean_style(table).find_all("tr")

    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) > 3:
            raise ValueError()

        # content duplication check
        stripped_existing_full_citations = [
            strip_tags(normalise_text(bib.full_citation))
            for bib in BibliographyItem.objects.all()
        ]
        stripped_current_bibliography = [normalise_text(col.get_text()) for col in cols]
        if stripped_current_bibliography[1] in stripped_existing_full_citations:
            skipped_count += 1
            continue

        # populating BibliographyItem object from data
        bibliography = [col.decode_contents() for col in cols]

        _, created = BibliographyItem.objects.get_or_create(
            short_citation=bibliography[0],
            full_citation=bibliography[1],
            annotation=bibliography[2] if len(cols) == 3 else "",
        )
        if created:
            created_count += 1
        else:
            skipped_count += 1

    return created_count, skipped_count
