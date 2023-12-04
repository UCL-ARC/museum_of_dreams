from django.db import models
from django.test import TestCase

from mod_app.models import Actor, Analysis, Copy, Crew, Film, Link, Location, Tag


class TestActor(TestCase):
    def setUp(self):
        Actor.objects.create(name="test actor")
        Film.objects.create(
            title="test film",
            release_date=2023,
        )

    def test_actor_creation(self):
        actor = Actor.objects.get(name="test actor")

        self.assertTrue(actor)
        self.assertEqual(actor.name, "test actor")

    def test_actor_film_link(self):
        actor = Actor.objects.get(name="test actor")
        film = Film.objects.get(title="test film")

        actor.films.add(film)
        self.assertQuerySetEqual(film.actors.all(), [actor])


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


class TestCopy(TestCase):
    def test_copy_creation(self):
        copy = Copy.objects.create(name="test copy")

        self.assertTrue(copy)
        self.assertEqual(copy.name, "test copy")
        self.assertEqual(copy.condition, "reasonable")


class TestAnalysis(TestCase):
    def test_analysis_creation(self):
        film = Film.objects.create(title="film title", release_date="1999")
        analysis = Analysis.objects.create(
            content="long, detailed analysis of film", film=film
        )

        self.assertTrue(analysis)
        self.assertEqual(analysis.content, "long, detailed analysis of film")
        self.assertEqual(analysis.film, film)


class TestCrew(TestCase):
    def test_crew_creation(self):
        crew = Crew.objects.create(name="crew member")

        self.assertTrue(crew)
        self.assertEqual(crew.name, "crew member")
        self.assertFalse(crew.roles)


class TestLocation(TestCase):
    def test_location_creation(self):
        loc = Location.objects.create(address="London, UK")

        self.assertTrue(loc)
        self.assertEqual(loc.address, "London, UK")
        self.assertFalse(loc.is_setting)
