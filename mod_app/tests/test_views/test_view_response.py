from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import MagicMock, patch
from mod_app.models import Film, Analysis, TeachingResources, Tag, BibliographyItem


class TestViewResponse(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.view_urls = [
            "home",
            "film_list",
            "analysis_list",
            "tr_list",
            "tag_list",
            "bibliography",
            "mentions_api",
        ]
        cls.detail_view_urls = [
            "film_detail",
            "analysis_detail",
            "tr_detail",
            "tag_detail",
        ]
        cls.bibilography = BibliographyItem.objects.create(
            short_citation="Test Short Citation", full_citation="Test Full Citation"
        )
        cls.film = Film.objects.create(title="Test Film", release_date="2020")
        cls.analysis = Analysis.objects.create(title="Test Analysis")
        cls.tr = TeachingResources.objects.create(title="Test TeachingResources")
        cls.tag = Tag.objects.create(name="Test Tag")

    def test_views_http_response(self):
        for view_url in self.view_urls:
            with self.subTest(view=view_url):
                response = self.client.get(reverse(view_url))
                self.assertEqual(response.status_code, 200)

    def test_detail_views_http_response(self):
        for detail_view_url in self.detail_view_urls:
            with self.subTest(view=detail_view_url):
                response = self.client.get(reverse(detail_view_url, args=[1]))
                self.assertEqual(response.status_code, 200)

    @patch("mod_app.views.boto3.Session")
    def test_bucket_items_view_http_response(self, mock_boto_session):
        User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        mock_boto_session.return_value = MagicMock()

        response = self.client.get(reverse("view_bucket_items"))
        self.assertEqual(response.status_code, 200)
