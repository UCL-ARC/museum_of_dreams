from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.recorder import MigrationRecorder
from django.test import TransactionTestCase


class TestKeywordToTopicMigration(TransactionTestCase):
    app = "mod_app"

    def setUp(self):
        self.executor = MigrationExecutor(connection)

    def migrate_to(self, migration_name):
        # The MigrationExecutor caches the migration graph and states. If you migrate to a certain state (e.g. 0002_initial), and then later try to migrate to 0003_add_field, Django may think it has already applied it — especially if the migration record exists in the database, or if the executor wasn't reloaded.
        self.executor = MigrationExecutor(
            connection
        )  # Reloads the executor each time function is called, to prevent migrations not applying
        self.executor.migrate([(self.app, migration_name)])
        return self.executor.loader.project_state((self.app, migration_name)).apps

    def test_apply_migration(self):
        recorder = MigrationRecorder(connection)
        # Pre-migration
        self.migrate_to("0039_add_topic_field_to_Film")

        # Post-migration
        self.migrate_to("0040_data_migration_transfer_keyword_to_topic")

        self.assertTrue(
            (self.app, "0040_data_migration_transfer_keyword_to_topic")
            in recorder.applied_migrations()
        )

    def test_transfer_keyword_to_topic(self):
        # Setup pre-migration state
        mod_app_pre_migration = self.migrate_to("0039_add_topic_field_to_Film")

        # Create testcases in the pre-migration model
        KeywordPreMigration = mod_app_pre_migration.get_model("mod_app", "Keyword")
        KeywordPreMigration.objects.create(name="Keyword1", is_genre=False)
        KeywordPreMigration.objects.create(name="Keyword2", is_genre=True)

        # Asserts testcases were created correctly
        self.assertEqual(KeywordPreMigration.objects.count(), 2)

        # Apply migration
        mod_app_post_migration = self.migrate_to(
            "0040_data_migration_transfer_keyword_to_topic"
        )

        # Get state of models post-migration
        TopicPostMigration = mod_app_post_migration.get_model("mod_app", "Topic")
        KeywordPostMigration = mod_app_post_migration.get_model("mod_app", "Keyword")

        # Assert Keywords are deleted
        self.assertFalse(
            KeywordPostMigration.objects.filter(
                name="Keyword1", is_genre=False
            ).exists()
        )
        self.assertFalse(
            KeywordPostMigration.objects.filter(name="Keyword2", is_genre=True).exists()
        )

        # Assert Topics were copied
        self.assertTrue(
            TopicPostMigration.objects.filter(name="Keyword1", is_genre=False).exists()
        )
        self.assertTrue(
            TopicPostMigration.objects.filter(name="Keyword2", is_genre=False).exists()
        )

    def test_transfer_keyword_relationship_to_topic(self):
        mod_app_pre_migration = self.migrate_to("0039_add_topic_field_to_Film")

        KeywordPreMigration = mod_app_pre_migration.get_model("mod_app", "Keyword")
        FilmPreMigration = mod_app_pre_migration.get_model("mod_app", "Film")
        AnalysisPreMigration = mod_app_pre_migration.get_model("mod_app", "Analysis")
        TeachingResourcesPreMigration = mod_app_pre_migration.get_model(
            "mod_app", "TeachingResources"
        )

        # mock data
        keyword = KeywordPreMigration.objects.create(name="Keyword")
        film = FilmPreMigration.objects.create(title="Film1", release_date="2000")
        analysis = AnalysisPreMigration.objects.create(title="Analysis1")
        teaching_resource = TeachingResourcesPreMigration.objects.create(
            title="TeachingResource1"
        )

        film.keyword.add(keyword)
        analysis.keywords.add(keyword)
        teaching_resource.keywords.add(keyword)

        # Apply migration
        mod_app_post_migration = self.migrate_to(
            "0040_data_migration_transfer_keyword_to_topic"
        )

        # Get Topic object values after mi
        TopicPostMigration = mod_app_post_migration.get_model("mod_app", "Topic")
        topic_post_migration = TopicPostMigration.objects.get(name="Keyword")

        film_related_topics = list(film.topic.all())
        analysis_related_topics = list(analysis.topics.all())
        tr_related_topics = list(teaching_resource.topics.all())

        # Asserts previous relationship to keyword are now in the topic(s) field
        self.assertEqual(topic_post_migration.id, keyword.id)
        self.assertEqual(
            film_related_topics[0].id,
            topic_post_migration.id,
            f"Expected topic id {topic_post_migration.id}, got {film_related_topics[0].id}",
        )
        self.assertEqual(
            analysis_related_topics[0].id,
            topic_post_migration.id,
            f"Expected topic id {topic_post_migration.id}, got {analysis_related_topics[0].id}",
        )
        self.assertEqual(
            tr_related_topics[0].id,
            topic_post_migration.id,
            f"Expected topic id {topic_post_migration.id}, got {tr_related_topics[0].id}",
        )
