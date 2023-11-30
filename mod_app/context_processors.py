# myapp/context_processors.py
from django.contrib.sites.shortcuts import get_current_site


def admin_custom_titles(request):
    current_site = get_current_site(request)
    site_header = "Administration for Museum of Dreamworlds Site"
    site_title = "Museum of Dreamworlds Admin Site"
    index_title = "Admin"

    if "museumofdreamworlds" not in current_site.domain:
        site_header = "Administration for Museum of Dreams (staging)"
        site_title = "Museum of Dreams Staging Admin Site"
        index_title = "Admin"

    return {
        "admin_site_header": site_header,
        "admin_site_title": site_title,
        "admin_index_title": index_title,
    }
