from django.db import models
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile


from mod_app.models import (
    Analysis,
    Film,
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
    TeachingResources,
    OtherLink,
    Source,
)


class TestTag(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="test tag")

        self.assertTrue(tag)
        self.assertEqual(tag.name, "test tag")


class TestBaseLinkModels(TestCase):
    baselink_models = [OtherLink, Source]
    url = models.URLField("some-url.com")

    def create_instance(self, model_class):
        return model_class.objects.create(
            url=self.url,
            description="testing links.",
        )

    def test_link_creation(self):
        for model_class in self.baselink_models:
            instance = self.create_instance(model_class)

            self.assertTrue(instance)
            self.assertEqual(instance.url, self.url)
            self.assertEqual(instance.description, "testing links.")
            self.assertIsInstance(instance.url, models.URLField)


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
        tr = TeachingResources.objects.create(title="teaching resource")
        analysis.films.add(film)
        analysis.teaching_resources.add(tr)

        self.assertTrue(analysis)
        self.assertEqual(analysis.content, "long, detailed analysis of film")
        self.assertEqual(analysis.films.first(), film)
        self.assertEqual(analysis.teaching_resources.first(), tr)


class TestTeachingResources(TestCase):
    def test_tr_creation(self):
        film = Film.objects.create(title="film title", release_date="1999")
        analysis = Analysis.objects.create()
        tr = TeachingResources.objects.create(title="teaching resource")
        tr.films.add(film)
        analysis.teaching_resources.add(tr)

        self.assertTrue(tr)
        self.assertEqual(tr.films.first(), film)
        self.assertEqual(tr.analyses.first(), analysis)


class TestLocation(TestCase):
    def test_location_creation(self):
        loc = Location.objects.create(address="London, UK")

        self.assertTrue(loc)
        self.assertEqual(loc.address, "London, UK")
        self.assertFalse(loc.is_setting)
