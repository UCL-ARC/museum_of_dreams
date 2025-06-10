"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'museum_of_dreams_project.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for museumofdream(world)s
    """

    class Media:
        css = {
            "all": ("admin/css/custom.css",),
        }

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration"
        self.children.append(
            modules.Group(
                _("Administration & Applications"),
                column=3,
                collapsible=True,
                children=[
                    modules.ModelList(
                        column=1,
                        collapsible=False,
                        models=("django.contrib.*",),
                    ),
                ],
            )
        )

        # append a group for the models
        self.children.append(
            modules.Group(
                _("Models"),
                column=1,
                collapsible=True,
                children=[
                    modules.ModelList(
                        _("Main Models"),
                        column=1,
                        collapsible=False,
                        models=(
                            "mod_app.models.film_model.*",
                            "mod_app.models.teaching_analysis_models.*",
                            "mod_app.models.bibliography_model.*",
                            "mod_app.models.project_note_model.ProjectNote",
                        ),
                    ),
                    modules.ModelList(
                        _("Printed Material"),
                        collapsible=False,
                        models=(
                            "mod_app.models.baselink_models.Script",
                            "mod_app.models.baselink_models.PressBook",
                            "mod_app.models.baselink_models.Programme",
                            "mod_app.models.baselink_models.Publicity",
                        ),
                    ),
                    modules.ModelList(
                        _("Visual Resources"),
                        column=1,
                        collapsible=False,
                        models=(
                            "mod_app.models.baselink_models.Still",
                            "mod_app.models.baselink_models.Postcard",
                            "mod_app.models.baselink_models.Poster",
                            "mod_app.models.baselink_models.Drawing",
                        ),
                    ),
                    modules.ModelList(
                        _("Extras"),
                        column=1,
                        collapsible=False,
                        models=(
                            "mod_app.models.baselink_models.Video",
                            "mod_app.models.baselink_models.Source",
                            "mod_app.models.baselink_models.OtherLink",
                            "mod_app.models.support_models.Tag",
                            "mod_app.models.support_models.Keyword",
                            "mod_app.models.support_models.Topic",
                            "mod_app.models.feedback_model.Feedback",
                            "mod_app.models.visual_written_influences_model.VisualInfluences",
                            "mod_app.models.visual_written_influences_model.WrittenInfluences",
                            "mod_app.models.support_models.Archive",
                        ),
                    ),
                ],
            )
        )

        # # append another link list module for "support"
        # # this needs some extra setup, possibly Pillow
        # self.children.append(
        #     modules.LinkList(
        #         _("Media Management"),
        #         column=2,
        #         children=[
        #             {
        #                 "title": _("FileBrowser"),
        #                 "url": "/admin/filebrowser/browse/",
        #                 "external": False,
        #             },
        #         ],
        #     )
        # )

        # append another link list module for "support".
        self.children.append(
            modules.LinkList(
                _("Support: Docs for usage"),
                column=3,
                children=[
                    {
                        "title": _("How to use the Admin Interface"),
                        "url": "https://github.com/UCL-ARC/museum_of_dreams/wiki/Using-the-Admin-Interface",
                        "external": True,
                        "header": True,
                    },
                    {
                        "title": _("How to add MediaCentral & Flickr links"),
                        "url": "https://github.com/UCL-ARC/museum_of_dreams/wiki/Adding-links-from-mediacentral-&-flickr",
                        "external": True,
                        "header": True,
                    },
                    {
                        "title": _("Adding Images"),
                        "url": "https://github.com/UCL-ARC/museum_of_dreams/wiki/Adding-Images",
                        "external": True,
                        "header": True,
                    },
                    {
                        "title": _("Importing from Word"),
                        "url": "https://github.com/UCL-ARC/museum_of_dreams/wiki/Importing-from-Word",
                        "external": True,
                        "header": True,
                    },
                    {
                        "title": _("Uploading Bibliography Items"),
                        "url": "https://github.com/UCL-ARC/museum_of_dreams/wiki/Using-the-Admin-Interface/_edit#importing-a-list-of-bibliographies-from-html-table",
                        "external": True,
                        "header": True,
                    },
                ],
            )
        )

        # append a recent actions module
        self.children.append(
            modules.RecentActions(
                _("Recent actions"),
                limit=10,
                collapsible=False,
                column=2,
            )
        )
