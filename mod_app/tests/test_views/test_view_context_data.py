from django.test import Client, TestCase
from django.urls import reverse

from mod_app.models import (
    Analysis,
    BibliographyItem,
    Film,
    Tag,
    TeachingResources,
)

from mod_app.models.baselink_models import (
    Script,
    PressBook,
    Programme,
    Publicity,
    Still,
    Drawing,
    Poster,
    Postcard,
    Video,
)


class TestViewContextData(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.film1 = Film.objects.create(title="Test Film1", release_date="2020")
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

        pm1 = Script.objects.create(url="", film=cls.film1)
        pm2 = PressBook.objects.create(url="", film=cls.film1)
        pm3 = Programme.objects.create(url="", film=cls.film1)
        pm4 = Publicity.objects.create(url="", film=cls.film1)

        vr1 = Still.objects.create(url="", film=cls.film1)
        vr2 = Drawing.objects.create(url="", film=cls.film1)
        vr3 = Poster.objects.create(url="", film=cls.film1)
        vr4 = Postcard.objects.create(url="", film=cls.film1)

        video1 = Video.objects.create(url="", film=cls.film1)
        video2 = Video.objects.create(url="", film=cls.film1)
        video3 = Video.objects.create(url="", film=cls.film1)

        cls.test_pm_slides = [pm1, pm2, pm3, pm4]
        cls.test_vr_slides = [vr1, vr2, vr3, vr4]
        cls.test_video_slides = [video1, video2, video3]

        cls.test_films = [cls.film1, film2, film3]
        cls.test_analyses = [analysis1, analysis2, analysis3]
        cls.test_trs = [tr1, tr2, tr3]
        cls.test_tags = [tag1, tag2, tag3]
        cls.test_bibliographies = [bib1, bib2, bib3]

        cls.test_detailveiw_data_set = {
            "film_detail": {"film": cls.test_films},
            "analysis_detail": {"analysis": cls.test_analyses},
            "tr_detail": {"tr": cls.test_trs},
            "tag_detail": {"tag": cls.test_tags},
        }
        cls.test_listview_data_set = {
            "film_list": {"film_list": cls.test_films},
            "analysis_list": {"analysis_list": cls.test_analyses},
            "tr_list": {"teachingresources_list": cls.test_trs},
            "tag_list": {"tags": cls.test_tags},
            "bibliography": {"bibliographyitem_list": cls.test_bibliographies},
        }

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

    def test_film_detailview_printed_material_slides(self):
        response = self.client.get(reverse("film_detail", args=[self.film1.pk]))
        self.assertCountEqual(self.test_pm_slides, response.context["pm_slides"])
        print(response.context["pm_slides"])

    def test_film_detailview_visual_resources_slides(self):
        response = self.client.get(reverse("film_detail", args=[self.film1.pk]))
        self.assertCountEqual(self.test_vr_slides, response.context["vr_slides"])
        print(response.context["vr_slides"])

    def test_film_detailview_video_slides(self):
        response = self.client.get(reverse("film_detail", args=[self.film1.pk]))
        self.assertCountEqual(self.test_video_slides, response.context["video_slides"])
        print(response.context["video_slides"])
