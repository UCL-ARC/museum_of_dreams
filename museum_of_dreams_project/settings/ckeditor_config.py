CKEDITOR_CONFIGS = {
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
        "filebrowserBrowseUrl": MEDIA_URL,
    },
}
