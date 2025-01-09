// plugin.js
CKEDITOR.plugins.add("popout", {
  icons: "popout",
  init: function (editor) {
    editor.addCommand("popout", {
      exec: function (editor) {
        var newWindow = window.open("", "_blank", "width=800,height=600");
        // make sure new editor gets config
        var originalConfig = editor.config;
        var ckeditorBasePath = "/static/ckeditor/ckeditor/";

        // styling and qol bits
        var btnStyle =
          "background-color: #23a1cc; border: none;border-radius: 4px; color: white; padding: 1rem 1.2rem; text-align: center; text-decoration: none; display: flex; font-size: 16px; margin: 0.8rem; cursor: pointer; justify-self: center";

        var editorElement = editor.element.$;
        var editorContainer = editorElement.closest(".c-2");
        var labelElement =
          editorContainer.previousElementSibling.querySelector("label"); // Find the label in the sibling 'c-1'
        var labelText = labelElement
          ? labelElement.innerText
          : editor.name.split("id_").pop();

        var instanceTitle = document.getElementById("id_title").value;
        var path = window.location.pathname.split("mod_app/").pop();

        // Remove the trailing "/change"
        if (path.endsWith("/change")) {
          path = path.slice(0, -7);
        }
        var windowTitle = instanceTitle || path;

        // html structure for new window
        newWindow.document.write(
          `<html><head>              <title>MOD Editor || ${windowTitle} </title>
</head><body>
<h3 style="font-family:sans-serif">Editing ${labelText} for ${instanceTitle}</h3><textarea id="popout-editor"></textarea>
<button id="save-button" style="${btnStyle}">Save</button><button id="save-close-button" style="${btnStyle}">Save & Close</button></body></html>`
        );

        newWindow.document.close();

        // Load CKEditor script in the new window
        var script = newWindow.document.createElement("script");
        script.type = "text/javascript";
        script.src = ckeditorBasePath + "ckeditor.js";

        script.onload = function () {
          newWindow.CKEDITOR.replace("popout-editor", {
            ...originalConfig,
            // pass existing editor content to the new editor
            on: {
              instanceReady: function () {
                newWindow.CKEDITOR.instances["popout-editor"].setData(
                  editor.getData()
                );
              },
            },
          });

          // add listener to save button
          newWindow.document
            .getElementById("save-close-button")
            .addEventListener("click", function () {
              // Transfer content from the new editor to the original editor
              editor.setData(
                newWindow.CKEDITOR.instances["popout-editor"].getData()
              );

              // Close the new window
              newWindow.close();
            });

          newWindow.document
            .getElementById("save-button")
            .addEventListener("click", function () {
              // Transfer content from the new editor to the original editor
              editor.setData(
                newWindow.CKEDITOR.instances["popout-editor"].getData()
              );
            });
        };
        newWindow.document.body.appendChild(script);
      },
    });

    editor.ui.addButton("Popout", {
      label: "Open in new window",
      command: "popout",
      toolbar: "Popout",
      icon: this.path + "open_in_new.svg",
    });
  },
});
