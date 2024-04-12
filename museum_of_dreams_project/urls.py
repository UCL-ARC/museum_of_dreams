"""
URL configuration for museum_of_dreams_project project.
"""

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView

from django_distill import distill_path

from mod_app import views

if settings.ENVIRONMENT == "production":
    admin.site.site_header = "Administration for Museum of Dreamworlds Site"
    admin.site.site_title = "Museum of Dreamworlds Admin Site"
    admin.site.index_title = "Admin"
else:
    admin.site.site_header = "Administration for Museum of Dreams (staging)"
    admin.site.site_title = "Museum of Dreams Staging Admin Site"
    admin.site.index_title = "Admin (staging)"

urlpatterns = (
    [
        path("grappelli/", include("grappelli.urls")),
        path("grappelli-docs/", include("grappelli.urls_docs")),
        path("ckeditor/", include("ckeditor_uploader.urls")),
        path("admin/", admin.site.urls, name=admin),
        path("logout", LogoutView.as_view(next_page="/"), name="logout"),
        path(
            "view_bucket_items/",
            views.BucketItemsView.as_view(),
            name="view_bucket_items",
        ),
        distill_path(
            "", views.HomeView.as_view(), name="home", distill_file="index.html"
        ),
        path(
            "favicon.ico",
            RedirectView.as_view(url=f"{settings.STATIC_URL}admin/img/favicon.ico"),
        ),
        path("mentions-api", views.MentionsApiView.as_view(), name="mentions_api"),
        # website pages
        distill_path(
            "films",
            views.FilmListView.as_view(),
            name="film_list",
        ),
        distill_path(
            "films/<pk>",
            views.FilmDetailView.as_view(),
            name="film_detail",
        ),
        distill_path(
            "analyses",
            views.AnalysisListView.as_view(),
            name="analysis_list",
        ),
        distill_path(
            "analyses/<pk>",
            views.AnalysisDetailView.as_view(),
            name="analysis_detail",
        ),
        distill_path(
            "teaching-resources",
            views.TRListView.as_view(),
            name="tr_list",
        ),
        distill_path(
            "teaching-resources/<pk>",
            views.TRDetailView.as_view(),
            name="tr_detail",
        ),
        distill_path(
            "bibliography",
            views.BibliographyListView.as_view(),
            name="bibliography",
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
