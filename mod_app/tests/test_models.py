from django.test import TestCase
from models import Film, Actor


class FilmTestCase(TestCase):
    def setUp(self):
        Film.objects.create(
            title="test film",
            release_date=2023,
        )

    def test_basic_film_creation(self):
        film = Film.objects.get(title="test film")

        self.assertTrue(film)
        self.assertEqual(film.title, "test film")
        self.assertEqual(film.release_date, 2023)
