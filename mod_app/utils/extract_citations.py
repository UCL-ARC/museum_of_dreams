from bs4 import BeautifulSoup
from ..models.bibliography_model import BibliographyItem


def update_bibliography(self, field):
    if field:
        bib_items = get_bibliography_items(field)
        # for each pk found add the bib item to the bibliography if it's changed
        print("bib_list:", bib_items)
        if list(self.bibliography.all()) != bib_items:
            self.bibliography.clear()
            for bib in bib_items:
                self.bibliography.add(bib)


def get_bibliography_items(field):
    # extract pks using BeautifulSoup
    field_soup = BeautifulSoup(field, "html.parser")

    strong_tags = field_soup.find_all("strong", class_="bib-mention")

    print("strong tags", strong_tags)
    pk_list = []
    for strong_tag in strong_tags:
        pk = strong_tag.get("data-bib-id")
        if pk:
            print("yes pk")
            pk_list.append(pk)

    bib_list = []
    for pk in pk_list:
        try:
            bib_item = BibliographyItem.objects.get(pk=pk)
            bib_list.append(bib_item)
        except (ValueError, IndexError, BibliographyItem.DoesNotExist) as e:
            print(f"Error retrieving BibliographyItem {pk}: {e}")

    return bib_list
