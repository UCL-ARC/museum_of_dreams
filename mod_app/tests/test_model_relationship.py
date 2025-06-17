from django.test import TestCase
from models import (
    Film,
    Analysis,
    TeachingResources,
    VisualInfluences,
    WrittenInfluences,
    Source,
    Keyword,
    Topic,
    Bibliography,
    Tag,
    Clip,
    Archive,
)


class RelationshipFixtureTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # class wide fixture intialisation
        cls.film = Film.objects.create(title="Test Film", release_date=2025)
        cls.analysis = Analysis.objects.create(title="Test Analysis")
        cls.tr = TeachingResources.objects.create(title="Test Resource")
        cls.vi = VisualInfluences.objects.create(title="Test VisualInfluences")
        cls.wi = WrittenInfluences.objects.create(title="Test WrittenInfluences")
        cls.source = Source.objects.create(title="Test Source")

        cls.keyword = Keyword.objects.create(name="Keyword1")
        cls.topic = Topic.objects.create(name="Topic1")
        cls.genre = Tag.objects.create(name="Genre1", is_genre=True)
        cls.bibliography = Bibliography.objects.create(title="Bib1")
        cls.tag = Tag.objects.create(name="Tag1", is_genre=False)
        cls.clip = Clip.objects.create(title="Clip1")
        cls.archive = Archive.objects.create(name="Archive1")
