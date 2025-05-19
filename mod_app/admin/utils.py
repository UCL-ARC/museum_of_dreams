import html
from typing import Iterable

from django.contrib import admin
from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html
from django.contrib.admin.sites import AlreadyRegistered


def safe_bibliography(obj):
    bib_items = obj.bibliography.all()
    formatted_items = [
        format_html("<li>{}</li>", format_html(html.unescape(bib_item.full_citation)))
        for bib_item in bib_items
    ]
    return format_html("<ul>{}</ul>", format_html("".join(formatted_items)))


def safe_content(obj):
    truncated_content = truncatechars_html(obj.content, 200)
    modified_content = truncated_content.replace("{", "(").replace("}", ")")
    return format_html(modified_content)


def list_keywords(obj):
    keywords = obj.keywords.all()
    return ", ".join(str(kw) for kw in keywords)


def list_genres(obj):
    genres = obj.genre.all()
    return ", ".join(str(g) for g in genres)


def list_tags(obj):
    tags = obj.tags.all()
    return ", ".join(str(t) for t in tags)


def register_custom_admin(model, mixins=(), **options):
    """To be used to register django admin models:\n
    parameters:\n
    model : the django model you are registering\n
    mixins : mixin(s) that you want to apply\n
    options: kwargs - fields for the admin.ModelAdmin\n

    Example usage:\n
    for model in [Model1, Model2]:\n
        register_custom_admin(
            model=model,
            mixins=(PreviewMixin),
            search_fields=["description", "url"],
            list_display=["description", "film", "url", "preview"],
            autocomplete_fields=["archive"],
            )


    """
    if not isinstance(mixins, Iterable) or isinstance(mixins, type):
        mixins = (mixins,)

    base_classes = tuple(mixins) + (admin.ModelAdmin,)
    admin_class_name = f"{model.__name__}Admin"
    admin_class_attrs = options

    admin_class = type(admin_class_name, base_classes, admin_class_attrs)

    try:
        admin.site.register(model, admin_class)
    except AlreadyRegistered:
        pass
