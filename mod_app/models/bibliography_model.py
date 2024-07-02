from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags


class BibliographyItem(models.Model):
    """These should be automatically added to relevant bibliographies by the extract_citations.py file"""

    def __str__(self):
        plain_text = strip_tags(self.full_citation).replace("&nbsp;", " ")
        return f"\n{plain_text}"

    short_citation = models.CharField(
        max_length=200,
        null=True,
        help_text="Please use Harvard in-text citation style. Examples: (Author surname, year), or in the case of up to 3 authors: (Author 1 surname, Author 2 surname, Author 3 surname, year), or in the case or more than 3 authors: (Author 1 surname, et al., year) ",
    )
    full_citation = RichTextField(
        null=True,
        help_text="Please use Harvard reference list style. Examples: Author surname, initial. (year). 'Title of article/book/website/photograph'. Available at: URL or DOI where applicable (date accessed). Please note that the website or photo title should be italicised. For more detailed information and examples visit: https://www5.open.ac.uk/library/referencing-and-plagiarism/quick-guide-to-harvard-referencing-cite-them-right",
    )
    annotation = RichTextField(
        null=True,
        help_text="Notes on how this item was helpful or relevant, for example.",
    )
