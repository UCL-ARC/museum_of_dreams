from django.db import models
from django.test import TestCase

from mod_app.models import (
    Analysis,
    Film,
    Link,
    Location,
    Tag,
    Script,
    PressBook,
    Programme,
    Publicity,
    Still,
    Postcard,
    Poster,
    Drawing,
)


class TestTag(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="test tag")

        self.assertTrue(tag)
        self.assertEqual(tag.name, "test tag")


class TestLink(TestCase):
    def test_link_creation(self):
        url = models.URLField("some_url.com")
        link = Link.objects.create(url=url, description="testing link creation")

        self.assertTrue(link)
        self.assertEqual(link.url, url)
        self.assertEqual(link.description, "testing link creation")
        self.assertIsInstance(link.url, models.URLField)


from django.core.files.uploadedfile import SimpleUploadedFile


class TestFileLinkModels(TestCase):
    filelink_models = [
        Script,
        PressBook,
        Programme,
        Publicity,
        Still,
        Postcard,
        Poster,
        Drawing,
    ]

    def create_instance(self, model_class):
        # Create an instance of the specified model with file, url, and description
        return model_class.objects.create(
            file=SimpleUploadedFile(
                "test_file.txt", b"File content goes here.", content_type="text/plain"
            ),
            url="https://example.com",
            description="A test filelink.",
        )

    def test_filelink_creation(self):
        for model_class in self.filelink_models:
            instance = self.create_instance(model_class)

            self.assertTrue(instance)
            self.assertEqual(instance.url, "https://example.com")
            self.assertEqual(instance.description, "A test filelink.")

    def test_upload_to_function(self):
        for model_class in self.filelink_models:
            instance = self.create_instance(model_class)
            expected_path = f"files/{model_class.__name__}/test_file"

            self.assertIn(expected_path, instance.file.name)

    def tearDown(self):
        for model_class in self.filelink_models:
            instances = model_class.objects.all()
            for instance in instances:
                instance.file.delete()


class TestAnalysis(TestCase):
    def test_analysis_creation(self):
        film = Film.objects.create(title="film title", release_date="1999")
        analysis = Analysis.objects.create(content="long, detailed analysis of film")
        analysis.film.add(film)

        self.assertTrue(analysis)
        self.assertEqual(analysis.content, "long, detailed analysis of film")
        self.assertEqual(analysis.film.first(), film)


class TestLocation(TestCase):
    def test_location_creation(self):
        loc = Location.objects.create(address="London, UK")

        self.assertTrue(loc)
        self.assertEqual(loc.address, "London, UK")
        self.assertFalse(loc.is_setting)
