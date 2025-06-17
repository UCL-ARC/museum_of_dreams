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
    OtherLink,
)


class RelationshipFixtureTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # class wide fixture intialisation
        cls.film = Film.objects.create(title="Test Film", release_date=2025)
        cls.analysis = Analysis.objects.create(title="Test Analysis")
        cls.tr = TeachingResources.objects.create(title="Test Resource")
        cls.vi = VisualInfluences.objects.create(title="Test VisualInfluences")
        cls.baselinkmodel = OtherLink.objects.create(
            description="Test BaseLinkModel"
        )  # testing on child model object because BaseLinkModel is abstract
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

        cls.film_relationships = {
            "keyword": cls.keyword,
            "topic": cls.topic,
            "genre": cls.genre,
            "bibliography": cls.bibliography,
        }

        cls.analysis_relationships = {
            "films": cls.film,
            "topics": cls.topic,
            "keywords": cls.keyword,
            "genre": cls.genre,
            "bibliography": cls.bibliography,
        }

        cls.tr_relationships = {
            "tags": cls.tag,
            "clips": cls.clip,
        }

        cls.vi_relationships = {
            "films": cls.film,
            "archive": cls.archive,
            "bibliography": cls.bibliography,
        }

    def test_film_relationships(self):
        for field_name, related_object in self.film_relationships.items():
            # separate loop into individual subtests which outputs distinct fail reports
            with self.subTest(field=field_name):
                related_manager = getattr(self.film, field_name)
                related_manager.add(related_object)
                self.assertIn(related_object, related_manager.all())

    def test_analysis_relationships(self):
        for field_name, related_object in self.analysis_relationships.items():
            with self.subTest(field=field_name):
                related_manager = getattr(self.analysis, field_name)
                related_manager.add(related_object)
                self.assertIn(related_object, related_manager.all())

    def test_tr_relationships(self):
        for field_name, related_object in self.tr_relationships.items():
            with self.subTest(msg="test", field=field_name):
                related_manager = getattr(self.tr, field_name)
                related_manager.add(related_object)
                self.assertIn(related_object, related_manager.all())

    def test_vi_relationships(self):
        for field_name, related_object in self.vi_relationships.items():
            with self.subTest(field=field_name):
                related_manager = getattr(self.vi, field_name)
                related_manager.add(related_object)
                self.assertIn(related_object, related_manager.all())

    def test_source_relationship(self):
        self.source.film.add(self.film)
        self.assertIn(self.film, self.source.film.all())
