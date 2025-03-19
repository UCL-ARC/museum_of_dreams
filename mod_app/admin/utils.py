from django.template.defaultfilters import truncatechars_html
from django.utils.html import format_html
import html


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
