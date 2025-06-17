from django.test import TestCase

from mod_app.models import (
    Analysis,
    Archive,
    BibliographyItem,
    Film,
    Keyword,
    Source,
    Tag,
    TeachingResources,
    Topic,
    Video,
    VisualInfluences,
    WrittenInfluences,
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
        cls.source = Source.objects.create(description="Test Source")

        cls.tag = Tag.objects.create(name="Tag1", is_genre=False)
        cls.keyword = Keyword.objects.create(name="Keyword1", is_genre=False)
        cls.topic = Topic.objects.create(name="Topic1", is_genre=False)
        cls.genre = Tag.objects.create(name="Genre1", is_genre=True)
        cls.bibliography = BibliographyItem.objects.create(
            short_citation="Bib1", full_citation="Bib1 Full Citation"
        )
        cls.clip = Video.objects.create(description="Clip1")
        cls.archive = Archive.objects.create(name="Archive1")
