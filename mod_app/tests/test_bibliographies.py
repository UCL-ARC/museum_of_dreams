from django.test import TestCase

from mod_app.models import BibliographyItem, Analysis, Film


class TestBibliographyItems(TestCase):
    def setUp(self):
        self.bib_item = BibliographyItem.objects.create(
            short_citation="Citation, S. (2024)",
            full_citation="Citation, S. (2024).Advanced Mention Testing. Journal of Testing Sciences, 15(3), 123-145.",
        )
        self.bib_item2 = BibliographyItem.objects.create(
            short_citation="Service, T. (2024)",
            full_citation="Service, T. (2024).Advanced Mention Testing. Journal of Testing Sciences, 15(3), 123-145.",
        )
        self.analysis = Analysis.objects.create(
            title="test analysis",
            content=f"This is a test citation <strong>{self.bib_item.short_citation}</strong>",
        )
        self.film = Film.objects.create(
            title="test film",
            print_comments=f"This is a test citation <strong>{self.bib_item2.short_citation}</strong>",
        )

    def test_bib_item_creation(self):
        bib_item = BibliographyItem.objects.get(
            short_citation=self.bib_item.short_citation
        )

        self.assertTrue(bib_item)
        self.assertEqual(bib_item.short_citation, self.bib_item.short_citation)
        self.assertEqual(bib_item.full_citation, self.bib_item.full_citation)

    def test_bib_automatically_generates(self):
        analysis = Analysis.objects.get(title="test analysis")
        film = Film.objects.get(title="test film")

        self.assertIn(self.bib_item, analysis.bibliography.all())
        self.assertIn(self.bib_item2, film.bibliography.all())

    def test_bib_automatically_updates(self):
        analysis = Analysis.objects.get(title="test analysis")
        analysis.content = (
            f"This is a test citation <strong>{self.bib_item2.short_citation}</strong>"
        )
        analysis.save()

        self.assertIn(self.bib_item2, analysis.bibliography.all())
