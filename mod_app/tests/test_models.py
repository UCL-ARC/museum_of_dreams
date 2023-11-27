from django.test import TestCase
from mod_app.models import Film, Actor


class TestFilm(TestCase):
    def setUp(self):
        Film.objects.create(
            title="test film",
            release_date=2023,
        )

    def test_film_creation(self):
        film = Film.objects.get(title="test film")

        self.assertTrue(film)
        self.assertEqual(film.title, "test film")
        self.assertEqual(film.release_date, 2023)


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
