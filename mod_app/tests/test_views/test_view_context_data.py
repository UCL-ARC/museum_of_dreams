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

        cls.test_detailview_data_set = [
            {
                "url_name": "film_detail",
                "model": Film,
                "context_key": "film",
                "test_objects": cls.test_films,
            },
            {
                "url_name": "analysis_detail",
                "model": Analysis,
                "context_key": "analysis",
                "test_objects": cls.test_analyses,
            },
            {
                "url_name": "tr_detail",
                "model": TeachingResources,
                "test_objects": cls.test_trs,
                "context_key": "tr",
            },
            {
                "url_name": "tag_detail",
                "model": Tag,
                "context_key": "tag",
                "test_objects": cls.test_tags,
            },
        ]

        cls.test_listview_data_set = [
            {
                "url_name": "film_list",
                "model": Film,
                "context_key": "film_list",
                "test_objects": cls.test_films,
                "fallback_text": "No Films found",
            },
            {
                "url_name": "analysis_list",
                "model": Analysis,
                "context_key": "analysis_list",
                "test_objects": cls.test_analyses,
                "fallback_text": "No Analyses found",
            },
            {
                "url_name": "tr_list",
                "model": TeachingResources,
                "test_objects": cls.test_trs,
                "context_key": "teachingresources_list",
                "fallback_text": "No Teaching Resources found",
            },
            {
                "url_name": "tag_list",
                "model": Tag,
                "context_key": "tags",
                "test_objects": cls.test_tags,
                "fallback_text": "No Tags found",
            },
            {
                "url_name": "bibliography",
                "model": BibliographyItem,
                "test_objects": cls.test_bibliographies,
                "context_key": "bibliographyitem_list",
                "fallback_text": "No Bibliographies found",
            },
        ]

    def test_detailview_context(self):
        for view in self.test_detailview_data_set:
            # access relevant information from data set
            url_name = view["url_name"]
            context_key = view["context_key"]
            test_objects = view["test_objects"]

            # validate individual responses for each test object
            for obj in test_objects:
                with self.subTest(view=view["url_name"], test_object=obj):
                    response = self.client.get(reverse(url_name, args=[obj.pk]))
                    self.assertEqual(obj, response.context[context_key])

    def test_listview_context(self):
        for view in self.test_listview_data_set:
            with self.subTest(view=view["url_name"]):
                # access relevant information from data set
                url_name = view["url_name"]
                context_key = view["context_key"]
                test_objects = view["test_objects"]

                # get HTTP Template response
                response = self.client.get(reverse(url_name))

                # checks that each object fixture in present in the context value
                for obj in test_objects:
                    self.assertIn(obj, response.context[context_key])

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

    # no context data tests are run at the very end because it will clear the database fixtures intialised in setUp
    def test_list_view_no_context_data(self):
        for view in self.test_listview_data_set:
            with self.subTest(view=view["url_name"]):
                url_name = view["url_name"]
                model = view["model"]
                context_key = view["context_key"]
                fallback_text = view["fallback_text"]

                # clear the model and get response
                model.objects.all().delete()
                response = self.client.get(reverse(url_name))

                # check that the context key is present and empty
                self.assertIn(context_key, response.context)
                self.assertFalse(response.context[context_key])

                # check for fallback message in template
                self.assertContains(response, fallback_text)
