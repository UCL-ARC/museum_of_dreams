from django.db import models
from ckeditor.fields import RichTextField

from mod_app.models import *


class BibliographyItem(models.Model):
    """These should be automatically added to relevant bibliographies by the extract_citations.py file"""

    def __str__(self):
        return f"{self.short_citation}"

    short_citation = models.CharField(max_length=200, null=True)
    full_citation = RichTextField(null=True)
