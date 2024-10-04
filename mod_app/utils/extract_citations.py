from bs4 import BeautifulSoup
from ..models.bibliography_model import BibliographyItem


def update_bibliography(self, fields):
    # fields should be a list
    if fields:
        bib_items = []
        for field in fields:
            if field:
                bib_items.extend(get_bibliography_items(field))

        # for each pk found add the bib item to the bibliography if it's changed
        if list(self.bibliography.all()) != bib_items:
            self.bibliography.set(bib_items)


def get_bibliography_items(field):
    # extract pks using BeautifulSoup
    field_soup = BeautifulSoup(field, "html.parser")

    strong_tags = field_soup.find_all("strong", class_="bib-mention")

    pk_list = [tag.get("data-bib-id") for tag in strong_tags]
    bib_qs = BibliographyItem.objects.filter(pk__in=pk_list)

    return bib_qs
