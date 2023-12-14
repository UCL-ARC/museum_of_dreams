from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("mod_app", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="film",
            name="additional_links",
            field=models.ManyToManyField(
                blank=True,
                help_text="Links to other things",
                related_name="other_links",
                to="mod_app.link",
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="video",
            field=models.ForeignKey(
                blank=True,
                help_text="Link or upload the video file",
                limit_choices_to={"video_link__isnull": False},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="video_link",
                to="mod_app.filelink",
            ),
        ),
    ]
