from bs4 import BeautifulSoup
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from ..utils.extract_citations import update_bibliography

from mod_app.models import Tag, Keyword, Topic, BibliographyItem


def display_list(list):
    if len(list) > 1:
        display_list = ", ".join(str(f) for f in list[:-1]) + f", and {list[-1]}"
    else:
        display_list = str(list[0])
    return display_list


def strip_empty_paragraphs(content):
    """There seems to be some weird behaviour wherein CKEditor is adding empty paragraphs after videos. We don't want this on the front end nor in the actual content field, so this function removes any <p>&nbsp;</p> that immediately follow a video div."""
    soup = BeautifulSoup(content, "html.parser")

    video_divs = soup.find_all("div", class_="ckeditor-html5-video")

    for div in video_divs:
        next_element = div.next_sibling

        # Keep checking and removing consecutive <p>&nbsp;</p> elements
        while True:
            # Skip whitespace text nodes
            while (
                next_element
                and isinstance(next_element, str)
                and next_element.strip() == ""
            ):
                next_element = next_element.next_sibling

            # Check if next element is <p>&nbsp;</p> or <p></p>
            if (
                next_element
                and next_element.name == "p"
                and (
                    next_element.encode_contents() == b"&nbsp;"
                    or next_element.get_text() == "\xa0"
                    or next_element.string == "\xa0"
                    or not next_element.contents
                )
            ):
                # Store the next sibling before removing the current element
                next_to_check = next_element.next_sibling
                # Remove the <p>&nbsp;</p> element and move to the next
                next_element.decompose()
                next_element = next_to_check
            else:
                # Break loop when we get back to real content
                break

    cleaned_html = str(soup)
    return cleaned_html


class Analysis(models.Model):
    class Meta:
        verbose_name_plural = "Analyses"

    def __str__(self):
        return self.title

    def default_title():
        return f"Analysis {Analysis.objects.count() + 1}"

    title = models.CharField(max_length=255, default=default_title)

    summary = models.TextField(max_length=1500, null=True, blank=True)

    content = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here and will contibute to the bibliography.",
    )

    films = models.ManyToManyField("Film", related_name="analyses", blank=True)

    topics = models.ManyToManyField(Topic, related_name="analysis_topics", blank=True)

    keywords = models.ManyToManyField(
        Keyword, related_name="analysis_keywords", blank=True
    )

    genre = models.ManyToManyField(Tag, related_name="analysis_genres", blank=True)

    holdings = models.CharField(max_length=400, blank=True, null=True)

    work_history = models.TextField(blank=True)

    teaching_resources = models.ManyToManyField(
        "TeachingResources", related_name="analyses", blank=True
    )

    bibliography = models.ManyToManyField(
        BibliographyItem,
        related_name="analyses",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.content is not None and len(self.content) > 0:
            self.content = strip_empty_paragraphs(self.content)

        update_bibliography(self, [self.content])


class TeachingResources(models.Model):
    class Meta:
        verbose_name_plural = "Teaching Resources"

    def __str__(self):
        return self.title

    def default_title():
        return f"Teaching Resources bundle{TeachingResources.objects.count() + 1}"

    title = models.CharField(max_length=255, default=default_title)
    material = RichTextUploadingField(
        null=True,
        blank=True,
        help_text="Mentions are available here and will contibute to the bibliography.",
    )

    films = models.ManyToManyField("Film", related_name="trs", blank=True)

    topics = models.ManyToManyField(Topic, related_name="tr_topics", blank=True)

    keywords = models.ManyToManyField(Keyword, related_name="tr_keywords", blank=True)

    tags = models.ManyToManyField(Tag, related_name="tr_tags", blank=True)

    bibliography = models.ManyToManyField(
        BibliographyItem,
        related_name="teaching_resources",
        help_text="This field updates on save, and some items may not be visible immediately",
    )

    clips = models.ManyToManyField(
        "Video",
        related_name="tr_clips",
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        update_bibliography(self, [self.material])
