from bs4 import BeautifulSoup
from ..models.bibliography_model import BibliographyItem


def update_bibliography(self, field):
    short_citations = extract_short_citations(field)
    # for each citation found add the bit item to the bibliography
    for short_citation in short_citations:
        bibitem = BibliographyItem.objects.filter(short_citation=short_citation).first()
        if bibitem:
            self.bibliography.add(bibitem)


def extract_short_citations(field):
    # extract short_citations using BeautifulSoup
    field_soup = BeautifulSoup(field, "html.parser")

    strong_tags = field_soup.find_all("strong")

    # Retrieve existing short_citations from BibItem
    existing_short_citations = set(
        BibliographyItem.objects.values_list("short_citation", flat=True)
    )

    # Filter strong_tags to include only those matching existing short_citations
    matching_tags = [
        tag.text.strip()
        for tag in strong_tags
        if tag.text.strip() in existing_short_citations
    ]

    # print("matching short citations found:", matching_tags)
    return matching_tags
