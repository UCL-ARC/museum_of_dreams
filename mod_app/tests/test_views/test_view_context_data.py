from django.test import Client, TestCase
from django.urls import reverse
from mod_app.models import Film, Analysis, TeachingResources, Tag


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

        cls.slides_set = []
        cls.film_set = [film1, film2, film3]
        cls.analysis_set = [analysis1, analysis2, analysis3]
        cls.tr_set = [tr1, tr2, tr3]
        cls.tag_set = [tag1, tag2, tag3]

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

    def test_film_listview_context(self):
        response = self.client.get(reverse("film_list"))
        for film in self.film_set:
            with self.subTest(film=film):
                self.assertIn(film, response.context["film_list"])

    def test_film_detailview_context(self):
        for film in self.film_set:
            with self.subTest(film=film):
                response = self.client.get(reverse("film_detail", args=[film.pk]))
                self.assertEqual(film, response.context["film"])

    def test_analysis_listview_context(self):
        response = self.client.get(reverse("analysis_list"))
        for analysis in self.analysis_set:
            with self.subTest(analysis=analysis):
                self.assertIn(analysis, response.context["analysis_list"])

    def test_analysis_detailview_context(self):
        for tr in self.tr_set:
            with self.subTest(teaching_resources=tr):
                response = self.client.get(reverse("tr_detail", args=[tr.pk]))
                self.assertEqual(tr, response.context["tr"])

    def test_tr_listview_context(self):
        response = self.client.get(reverse("tr_list"))
        for tr in self.tr_set:
            with self.subTest(teaching_resources=tr):
                self.assertIn(tr, response.context["teachingresources_list"])

    def test_tr_detailview_context(self):
        for tr in self.tr_set:
            with self.subTest(teaching_resources=tr):
                response = self.client.get(reverse("tr_detail", args=[tr.pk]))
                self.assertEqual(tr, response.context["tr"])

    def test_tag_listview_context(self):
        response = self.client.get(reverse("tag_list"))

        for tag in self.tag_set:
            with self.subTest(tag=tag):
                self.assertIn(tag, response.context["tags"])

    def test_tag_detailview_context(self):
        for tag in self.tag_set:
            with self.subTest(tag=tag):
                response = self.client.get(reverse("tag_detail", args=[tag.pk]))
                self.assertEqual(tag, response.context["tag"])
