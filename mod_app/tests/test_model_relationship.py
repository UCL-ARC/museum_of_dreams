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

    def test_film_keyword(self):
        self.film.keyword.add(self.keyword)
        self.assertIn(self.keyword, self.film.keyword.all())

    def test_film_topic(self):
        self.film.topic.add(self.topic)
        self.assertIn(self.topic, self.film.topic.all())

    def test_film_genre(self):
        self.film.genre.add(self.genre)
        self.assertIn(self.genre, self.film.genre.all())

    def test_film_bibliography(self):
        self.film.bibliography.add(self.bibliography)
        self.assertIn(self.bibliography, self.film.bibliography.all())

    def test_analysis_films(self):
        self.analysis.films.add(self.film)
        self.assertIn(self.film, self.analysis.films.all())

    def test_analysis_topics(self):
        self.analysis.topics.add(self.topic)
        self.assertIn(self.topic, self.analysis.topics.all())

    def test_analysis_keywords(self):
        self.analysis.keywords.add(self.keyword)
        self.assertIn(self.keyword, self.analysis.keywords.all())

    def test_analysis_genre(self):
        self.analysis.genre.add(self.genre)
        self.assertIn(self.genre, self.analysis.genre.all())

    def test_analysis_teaching_resources(self):
        self.analysis.teaching_resources.add(self.tr)
        self.assertIn(self.tr, self.analysis.teaching_resources.all())

    def test_analysis_bibliography(self):
        self.analysis.bibliography.add(self.bibliography)
        self.assertIn(self.bibliography, self.analysis.bibliography.all())

    def test_teachingresources_clips(self):
        self.tr.clips.add(self.clip)
        self.assertIn(self.clip, self.tr.clips.all())

    def test_teachingresources_tags(self):
        self.tr.tags.add(self.tag)
        self.assertIn(self.tag, self.tr.tags.all())

    def test_visualinfluences_archive(self):
        self.vi.archive.add(self.archive)
        self.assertIn(self.archive, self.vi.archive.all())

    def test_writteninfluences_archive(self):
        self.wi.archive.add(self.archive)
        self.assertIn(self.archive, self.wi.archive.all())

    def test_source_film(self):
        self.source.film.add(self.film)
        self.assertIn(self.film, self.source.film.all())
