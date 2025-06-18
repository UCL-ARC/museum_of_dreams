from django.test import Client, TestCase
from django.urls import reverse
from mod_app.models import Film, Analysis, TeachingResources, Tag


class TestViewContextData(TestCase):
    def Setup(self):
        self.client = Client()

    def test_homeview_context(self):
        response = self.client.get(reverse("home"))

    def test_film_detailview_context(self):
        response = self.client.get(reverse("film_detail"))

    def test_analysis_detailview_context(self):
        analysis = Analysis.objects.create(title="Test Analysis")
        response = self.client.get(reverse("analysis_detail"))
        self.assertIn(analysis, response.context)
        self.assertEqual(response.context[analysis], "expected_value")

    def test_tr_detailview_context(self):
        response = self.client.get(reverse("tr_detail"))

    def test_tag_listview_context(self):
        response = self.client.get(reverse("tag_list"))

    def test_tag_detailview_context(self):
        response = self.client.get(reverse("tag_detail"))
