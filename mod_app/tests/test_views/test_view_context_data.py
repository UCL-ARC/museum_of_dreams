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
        self.assertQuerysetEqual(
            response.context["film_list"],
            self.film_set,
        )

    def test_film_detailview_context(self):
        response = self.client.get(reverse("film_detail", args=[self.film.pk]))
        self.assertEqual(response.context["film"], self.film)

    def test_analysis_listview_context(self):
        response = self.client.get(reverse("analyses_list"))
        self.assertQuerysetEqual(
            response.context["analyses_list"],
            self.analysis_set,
        )

    def test_analysis_detailview_context(self):
        response = self.client.get(reverse("analysis_detail", args=[self.analysis.pk]))
        self.assertEqual(response.context["analysis"], self.analysis)

    def test_tr_listview_context(self):
        response = self.client.get(reverse("tr_list"))
        self.assertQuerysetEqual(
            response.context["tr_list"],
            self.tr_set,
        )

    def test_tr_detailview_context(self):
        response = self.client.get(reverse("tr_detail", args=[self.tr.pk]))
        self.assertEqual(response.context["tr"], self.tr)

    def test_tag_listview_context(self):
        response = self.client.get(reverse("tag_list"))

        for tag in self.tag_set:
            self.assertIn(tag, response.context["tags"])

    def test_tag_detailview_context(self):
        for tag in self.tag_set:
            response = self.client.get(reverse("tag_detail", args=[tag.pk]))
            self.assertEqual(response.context["tag"], tag)
