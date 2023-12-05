"""
URL configuration for museum_of_dreams_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
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

urlpatterns = [
    path("admin/", admin.site.urls, name=admin),
    distill_path("", views.HomeView.as_view(), name="home", distill_file="index.html"),
    distill_path("films/list", views.FilmListView.as_view(), name="film_list"),
    distill_path("films/<pk>", views.FilmDetailView.as_view(), name="film_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
