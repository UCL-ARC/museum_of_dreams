from django.test import Client, TestCase
from django.urls import reverse
from mod_app.models import Film, Analysis, TeachingResources, Tag


class TestViewContextData(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.film = Film.objects.create(title="Test Film", release_date="2020")
        cls.analysis = Analysis.objects.create(title="Test Analysis")
        cls.tr = TeachingResources.objects.create(title="Test TeachingResources")
        cls.tag = Tag.objects.create(name="Test Tag")

    def test_homeview_context(self):
        response = self.client.get(reverse("home"))

    def test_film_detailview_context(self):
        response = self.client.get(reverse("film_detail", args=[self.film.pk]))
        self.assertEqual(response.context["film"], self.film)

    def test_analysis_detailview_context(self):
        response = self.client.get(reverse("analysis_detail", args=[self.analysis.pk]))
        self.assertEqual(response.context["analysis"], self.analysis)

    def test_tr_detailview_context(self):
        response = self.client.get(reverse("tr_detail", args=[self.tr.pk]))
        self.assertEqual(response.context["tr"], self.tr)

    def test_tag_listview_context(self):
        response = self.client.get(reverse("tag_list"))

    def test_tag_detailview_context(self):
        response = self.client.get(reverse("tag_detail", args=[self.tag.pk]))
        self.assertEqual(response.context["tag"], self.tag)
