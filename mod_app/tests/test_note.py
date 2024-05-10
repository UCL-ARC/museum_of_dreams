from django.test import TestCase

from mod_app.models import ProjectNote


class TestProjectNote(TestCase):
    def test_tag_creation(self):
        note = ProjectNote.objects.create(title="test note", content="testingtesting")

        self.assertTrue(note)
        self.assertEqual(note.title, "test note")
        self.assertEqual(note.content, "testingtesting")
