from django.db import models
from django.test import TestCase

from mod_app.models import Analysis, Film, Link, Location, Tag


class TestTag(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="test tag")

        self.assertTrue(tag)
        self.assertEqual(tag.name, "test tag")


class TestLink(TestCase):
    def test_link_creation(self):
        url = models.URLField("some_url.com")
        link = Link.objects.create(path=url, description="testing link creation")

        self.assertTrue(link)
        self.assertEqual(link.path, url)
        self.assertEqual(link.description, "testing link creation")
        self.assertIsInstance(link.path, models.URLField)


class TestAnalysis(TestCase):
    def test_analysis_creation(self):
        film = Film.objects.create(title="film title", release_date="1999")
        analysis = Analysis.objects.create(
            content="long, detailed analysis of film", film=film
        )

        self.assertTrue(analysis)
        self.assertEqual(analysis.content, "long, detailed analysis of film")
        self.assertEqual(analysis.film, film)


class TestLocation(TestCase):
    def test_location_creation(self):
        loc = Location.objects.create(address="London, UK")

        self.assertTrue(loc)
        self.assertEqual(loc.address, "London, UK")
        self.assertFalse(loc.is_setting)
