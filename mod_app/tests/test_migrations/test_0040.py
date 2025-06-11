from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.recorder import MigrationRecorder
from django.test import TransactionTestCase


class TestUserCopyMigration(TransactionTestCase):
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

    def is_migration_applied(self, app, migration):
        recorder = MigrationRecorder(connection)

        applied = recorder.applied_migrations()
        return (app, migration) in applied

    def test_transfer_keyword_to_topic(self):
        # Migrate to state before the transfer
        mod_app_pre_migration = self.migrate_to("0039_add_topic_field_to_Film")

        self.assertTrue(
            self.is_migration_applied("mod_app", "0039_add_topic_field_to_Film")
        )

        KeywordPreMigration = mod_app_pre_migration.get_model("mod_app", "Keyword")

        # Create testcases in the pre-migration model
        KeywordPreMigration.objects.create(name="Keyword1", is_genre=False)
        KeywordPreMigration.objects.create(name="Keyword2", is_genre=True)

        self.assertEqual(KeywordPreMigration.objects.count(), 2)

        # Migrate to the state after the transfer,
        mod_app_post_migration = self.migrate_to(
            "0040_data_migration_transfer_keyword_to_topic"
        )

        self.assertTrue(
            self.is_migration_applied(
                "mod_app", "0040_data_migration_transfer_keyword_to_topic"
            )
        )

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

    def test_transfer_relationship(self):
        mod_app_pre_migration = self.migrate_to("0039_add_topic_field_to_Film")

        KeywordPreMigration = mod_app_pre_migration.get_model("mod_app", "Keyword")
        FilmPreMigration = mod_app_pre_migration.get_model("mod_app", "Film")
        AnalysisPreMigration = mod_app_pre_migration.get_model("mod_app", "Analysis")
        TeachingResourcesPreMigration = mod_app_pre_migration.get_model(
            "mod_app", "TeachingResources"
        )

        keyword = KeywordPreMigration.objects.create(name="Keyword")
        film = FilmPreMigration.objects.create(title="Film1", release_date="2000")
        analysis = AnalysisPreMigration.objects.create(title="Analysis1")
        teaching_resource = TeachingResourcesPreMigration.objects.create(
            title="TeachingResource1"
        )
        film.keyword.add(keyword)
        analysis.keywords.add(keyword)
        teaching_resource.keywords.add(keyword)

        mod_app_post_migration = self.migrate_to(
            "0040_data_migration_transfer_keyword_to_topic"
        )
        self.assertTrue(
            self.is_migration_applied(
                "mod_app", "0040_data_migration_transfer_keyword_to_topic"
            )
        )

        FilmPostMigration = mod_app_post_migration.get_model("mod_app", "Film")
        AnalysisPostMigration = mod_app_post_migration.get_model("mod_app", "Analysis")
        TeachingResourcesPostMigration = mod_app_post_migration.get_model(
            "mod_app", "TeachingResources"
        )
        TopicPostMigration = mod_app_post_migration.get_model("mod_app", "Topic")
        topic_post_migration = TopicPostMigration.objects.get(name="Keyword")

        self.assertEqual(topic_post_migration.id, keyword.id)
        self.assertTrue(
            FilmPostMigration.objects.filter(topic=topic_post_migration.id).exists()
        )
        self.assertTrue(
            AnalysisPostMigration.objects.filter(
                topics=topic_post_migration.id
            ).exists()
        )
        self.assertTrue(
            TeachingResourcesPostMigration.objects.filter(
                topics=topic_post_migration.id
            ).exists()
        )

        # Debugging
        for film in FilmPostMigration.objects.all():
            print(f"Film ID: {film.id}, Topic: {film.topic.all()}")
        for analysis in AnalysisPostMigration.objects.all():
            print(f"Analysis ID: {analysis.id}, Topic: {analysis.topics.all()}")
        for tr in TeachingResourcesPostMigration.objects.all():
            print(f"TeachingResource ID: {tr.id}, Topic: {tr.topics.all()}")
