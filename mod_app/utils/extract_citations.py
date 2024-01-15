from bs4 import BeautifulSoup
from ..models.bibliography_model import BibliographyItem


def update_bibliography(self, field):
    if field:
        bib_items = get_bibliography_items(field)
        # for each pk found add the bib item to the bibliography
        for bib in bib_items:
            self.bibliography.add(bib)


def get_bibliography_items(field):
    # extract short_citations using BeautifulSoup
    field_soup = BeautifulSoup(field, "html.parser")

    strong_tags = field_soup.find_all("strong")

    pk_list = []
    for strong_tag in strong_tags:
        a_tags = strong_tag.find_all("a")
        for a_tag in a_tags:
            href = a_tag.get("href")
            if href:
                pk_list.append(href)

    bib_list = []
    for pk in pk_list:
        try:
            bib_item = BibliographyItem.objects.get(pk=pk)
            bib_list.append(bib_item)
        except (ValueError, IndexError, BibliographyItem.DoesNotExist) as e:
            print(f"Error retrieving BibliographyItem {pk}: {e}")
    return bib_list
