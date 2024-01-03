from django.db import models
from ckeditor.fields import RichTextField

from mod_app.models import *


class BibliographyItem(models.Model):
    # """These should be automatically generated"""
    def __str__(self):
        return f"{self.short_citation}"

    short_citation = models.CharField(max_length=200, null=True)
    full_citation = RichTextField(null=True)

    @property
    def analysis_mentions(self):
        """check content of analyses for @ mentions"""
        analyses = []  # super.analysis_mentions()?
        for analysis in Analysis.objects.all():
            if analysis.content.includes(self.short_citation):
                analyses.push(analysis)
        return analyses

    @property
    def film_mentions(self):
        """check content of print comments for @ mentions"""
        films = []  # super.film_mentions()?
        for film in Film.objects.all():
            if film.print_comments.includes(self.short_citation):
                films.push(film)
        return films

    @property
    def tr_mentions(self):
        """check content of analyses for @ mentions"""
        trs = []  # super.trs_mentions()?
        for tr in TeachingResources.objects.all():
            if tr.content.includes(self.short_citation):
                trs.push(tr)
        return trs
