from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags


class BibliographyItem(models.Model):
    """These should be automatically added to relevant bibliographies by the extract_citations.py file"""

    def __str__(self):
        plain_text = strip_tags(self.full_citation).replace("&nbsp;", " ")
        return f"\n{plain_text}"

    short_citation = models.CharField(max_length=200, null=True)
    full_citation = RichTextField(null=True)
