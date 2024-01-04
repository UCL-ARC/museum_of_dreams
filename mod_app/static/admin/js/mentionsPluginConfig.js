"use-strict";
{
  document.addEventListener("DOMContentLoaded", function () {
    const itemTemplate =
      '<li data-id="{id}" data-value="{id}">{full_citation}</li>';
    const outputTemplate = "<b>{short_citation}</b>";

    CKEDITOR.config.mentions = [
      {
        feed: "/mentions-api?query={encodedQuery}",
        minChars: 0,
        itemTemplate: itemTemplate,
        followingSpace: true,
        denotationChar: "@",
        outputTemplate: outputTemplate,
      },
    ];
    CKEDITOR.config.autocomplete = [
      {
        itemTemplate: itemTemplate,
        outputTemplate: outputTemplate,
      },
    ];
  });
}
