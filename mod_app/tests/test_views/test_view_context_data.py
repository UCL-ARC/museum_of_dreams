from django.test import Client, TestCase
from django.urls import reverse
from mod_app.models import Film, Analysis, TeachingResources, Tag, BibliographyItem


class TestViewContextData(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        film1 = Film.objects.create(title="Test Film1", release_date="2020")
        film2 = Film.objects.create(title="Test Film2", release_date="2020")
        film3 = Film.objects.create(title="Test Film3", release_date="2020")

        analysis1 = Analysis.objects.create(title="Test Analysis1")
        analysis2 = Analysis.objects.create(title="Test Analysis2")
        analysis3 = Analysis.objects.create(title="Test Analysis3")

        tr1 = TeachingResources.objects.create(title="Test TeachingResources1")
        tr2 = TeachingResources.objects.create(title="Test TeachingResources2")
        tr3 = TeachingResources.objects.create(title="Test TeachingResources3")

        tag1 = Tag.objects.create(name="Test Tag1")
        tag2 = Tag.objects.create(name="Test Tag2")
        tag3 = Tag.objects.create(name="Test Tag3")

        bib1 = BibliographyItem.objects.create(short_citation="Test Bibliography1")
        bib2 = BibliographyItem.objects.create(short_citation="Test Bibliography2")
        bib3 = BibliographyItem.objects.create(short_citation="Test Bibliography3")

        cls.slides_set = []
        cls.film_set = [film1, film2, film3]
        cls.analysis_set = [analysis1, analysis2, analysis3]
        cls.tr_set = [tr1, tr2, tr3]
        cls.tag_set = [tag1, tag2, tag3]
        cls.bibliography_set = [bib1, bib2, bib3]

        cls.test_detailveiw_data_set = {
            "film_detail": {"film": cls.film_set},
            "analysis_detail": {"analysis": cls.analysis_set},
            "tr_detail": {"tr": cls.tr_set},
            "tag_detail": {"tag": cls.tag_set},
        }
        cls.test_listview_data_set = {
            "film_list": {"film_list": cls.film_set},
            "analysis_list": {"analysis_list": cls.analysis_set},
            "tr_list": {"teachingresources_list": cls.tr_set},
            "tag_list": {"tags": cls.tag_set},
            "bibliography": {"bibliographyitem_list": cls.bibliography_set},
        }

    def test_homeview_context(self):
        response = self.client.get(reverse("home"))
        self.assertQuerysetEqual(
            response.context["slides"],
            self.slides_set,
        )
        self.assertQuerysetEqual(
            response.context["slide_images"],
            True,
        )

    def test_detailview_context(self):
        for url, test_context in self.test_detailveiw_data_set.items():
            for context, test_objects in test_context.items():
                for test_obj in test_objects:
                    response = self.client.get(reverse(url, args=[test_obj.pk]))
                    with self.subTest(test_set=test_obj):
                        self.assertEqual(test_obj, response.context[context])

    def test_listview_context(self):
        for url, test_context in self.test_listview_data_set.items():
            for context, test_objects in test_context.items():
                response = self.client.get(reverse(url))
                for test_obj in test_objects:
                    with self.subTest(test_set=test_obj):
                        self.assertIn(test_obj, response.context[context])
