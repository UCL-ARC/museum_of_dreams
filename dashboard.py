"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'museum_of_dreams_project.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for museumofdream(world)s
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration"
        self.children.append(
            modules.Group(
                _("Group: Administration & Applications"),
                column=3,
                collapsible=True,
                children=[
                    modules.AppList(
                        _("Auth"),
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
                        ),
                    ),
                    modules.ModelList(
                        _("Printed Material"),
                        collapsible=False,
                        models=(
                            "mod_app.models.support_models.Script",
                            "mod_app.models.support_models.PressBook",
                            "mod_app.models.support_models.Programme",
                            "mod_app.models.support_models.Publicity",
                        ),
                    ),
                    modules.ModelList(
                        _("Visual Resources"),
                        column=1,
                        collapsible=False,
                        models=(
                            "mod_app.models.support_models.Still",
                            "mod_app.models.support_models.Postcard",
                            "mod_app.models.support_models.Poster",
                            "mod_app.models.support_models.Drawing",
                        ),
                    ),
                    modules.ModelList(
                        _("Extras"),
                        column=1,
                        collapsible=False,
                        models=(
                            "mod_app.models.support_models.OtherLink",
                            "mod_app.models.support_models.Tag",
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
                _("Support"),
                column=3,
                children=[
                    # {
                    #     "title": _("Grappelli Documentation"),
                    #     "url": "http://packages.python.org/django-grappelli/",
                    #     "external": True,
                    # },
                    {
                        "title": _("How to use the Admin Interface"),
                        "url": "https://github.com/UCL-ARC/museum_of_dreams/wiki/Using-the-Admin-Interface",
                        "external": True,
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
