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

        film1 = Film.objects.create(title="Test Film1", release_date="2020")
        film2 = Film.objects.create(title="Test Film2", release_date="2020")
        film3 = Film.objects.create(title="Test Film3", release_date="2020")
        cls.test_film_detail = Film.objects.create(
            title="Test Film Detail", release_date="2020"
        )

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

        pm1 = Script.objects.create(url="test_url1.com", film=cls.test_film_detail)
        pm2 = PressBook.objects.create(url="test_url2.com", film=cls.test_film_detail)
        pm3 = Programme.objects.create(url="test_url3.com", film=cls.test_film_detail)
        pm4 = Publicity.objects.create(url="test_url4.com", film=cls.test_film_detail)

        vr1 = Still.objects.create(url="test_url5.com", film=cls.test_film_detail)
        vr2 = Drawing.objects.create(url="test_url6.com", film=cls.test_film_detail)
        vr3 = Poster.objects.create(url="test_url7.com", film=cls.test_film_detail)
        vr4 = Postcard.objects.create(url="test_url8.com", film=cls.test_film_detail)

        video1 = Video.objects.create(url="test_url9.com", film=cls.test_film_detail)
        video2 = Video.objects.create(url="test_url10.com", film=cls.test_film_detail)
        video3 = Video.objects.create(url="test_url11.com", film=cls.test_film_detail)

        cls.test_pm_slides = [pm1, pm2, pm3, pm4]
        cls.test_vr_slides = [vr1, vr2, vr3, vr4]
        cls.test_video_slides = [video1, video2, video3]

        cls.test_films = [film1, film2, film3]
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
        response = self.client.get(
            reverse("film_detail", args=[self.test_film_detail.pk])
        )
        self.assertCountEqual(self.test_pm_slides, response.context["pm_slides"])
        print(response.context["pm_slides"])

    def test_film_detailview_visual_resources_slides(self):
        response = self.client.get(
            reverse("film_detail", args=[self.test_film_detail.pk])
        )
        self.assertCountEqual(self.test_vr_slides, response.context["vr_slides"])
        print(response.context["vr_slides"])

    def test_film_detailview_video_slides(self):
        response = self.client.get(
            reverse("film_detail", args=[self.test_film_detail.pk])
        )
        self.assertCountEqual(self.test_video_slides, response.context["video_slides"])
        print(response.context["video_slides"])
