from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.test import TransactionTestCase


class TestUserCopyMigration(TransactionTestCase):
    app = "mod_app"

    def setUp(self):
        self.executor = MigrationExecutor(connection)

    def migrate_to(self, migration_name):
        self.executor.migrate([(self.app, migration_name)])
        return self.executor.loader.project_state((self.app, migration_name)).apps

    def test_transfer_keyword_to_topic(self):
        # Migrate to state before the transfer
        mod_app_pre_migration = self.migrate_to("0039_add_topic_field_to_Film")
        KeywordPreMigration = mod_app_pre_migration.get_model("mod_app", "Keyword")

        # Create testcases in the pre-migration model
        KeywordPreMigration.objects.create(name="Keyword1", is_genre=False)
        KeywordPreMigration.objects.create(name="Keyword2", is_genre=True)

        # Migrate to the state after the transfer
        mod_app_post_migration = self.migrate_to(
            "0040_data_migration_transfer_keyword_to_topic"
        )
        TopicPostMigration = mod_app_post_migration.get_model("mod_app", "Topic")
        KeywordPostMigration = mod_app_post_migration.get_model("mod_app", "Keyword")

        # Assert Keywords was deleted
        self.assertFalse(
            KeywordPostMigration.objects.filter(name="Keyword1", is_genre=False)
        ).exists()
        self.assertFalse(
            KeywordPostMigration.objects.filter(name="Keyword1", is_genre=True)
        ).exists()

        # Assert Topics were copied
        self.assertTrue(
            TopicPostMigration.objects.filter(name="Keyword1", is_genre=False)
        ).exists()
        self.assertTrue(
            TopicPostMigration.objects.filter(name="Keyword1", is_genre=False)
        ).exists()
