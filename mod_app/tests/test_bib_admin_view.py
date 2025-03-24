from django.test import TestCase

from mod_app.admin.bibliography_admin import import_from_html


class TestImportfromHtml(TestCase):
    def setUp(self):
        self.valid_html_table = "mod_app/tests/data/valid_html_table.html"
        self.invalid_html_table = "mod_app/tests/data/invalid_html_table.html"
        self.blank_html_file = "mod_app/tests/data/blank_html.html"
        self.not_html_file = "mod_app/tests/data/not_html.txt"

    def test_valid_html_table(self):
        with open(self.valid_html_table) as file:
            created_count, skipped_count = import_from_html(file)
        self.assertEqual(created_count, 3)
        self.assertEqual(skipped_count, 0)

    def test_blank_html_file(self):
        with open(self.valid_html_file) as file:
            created_count, skipped_count = import_from_html(file)
        self.assertRaises(ValueError)

    def test_invalid_html_table(self):
        with open(self.invalid_html_table) as file:
            created_count, skipped_count = import_from_html(file)
        self.assertRaises(ValueError)

    def test_not_html_file(self):
        with open(self.not_html_file) as file:
            created_count, skipped_count = import_from_html(file)
        self.assertRaises(ValueError)
