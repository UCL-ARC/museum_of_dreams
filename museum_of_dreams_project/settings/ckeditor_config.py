def generate_ckeditor_config(media_url):
    return {
        "default": {
            "extraPlugins": ",".join(
                [
                    "uploadimage",
                    "uploadwidget",
                    "mentions",
                ]
            ),
            "removePlugins": "exportpdf",
            "uiColor": "#fcf5e7",
            "extraAllowedContent": "strong[data-bib-id](bib-mention);",
            "filebrowserBrowseUrl": media_url,
        },
    }
