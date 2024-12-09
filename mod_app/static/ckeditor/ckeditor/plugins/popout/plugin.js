// plugin.js
CKEDITOR.plugins.add("popout", {
  icons: "popout",
  init: function (editor) {
    editor.addCommand("popout", {
      exec: function (editor) {
        var newWindow = window.open("", "_blank", "width=800,height=600");

        var originalConfig = editor.config;
        var ckeditorBasePath = "/static/ckeditor/ckeditor/";

        // html structure for new window
        newWindow.document.write(
          '<html><head></head><body><textarea id="popout-editor"></textarea></body></html>'
        );

        newWindow.document.close();

        // Load CKEditor script in the new window
        var script = newWindow.document.createElement("script");
        script.type = "application/javascript";
        script.src = ckeditorBasePath + "ckeditor.js";

        script.onload = function () {
          console.log(originalConfig);
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

          // Sync data from the new window to the original editor
          newWindow.CKEDITOR.instances["popout-editor"].on(
            "change",
            function () {
              editor.setData(
                newWindow.CKEDITOR.instances["popout-editor"].getData()
              );
            }
          );

          // Sync data from the original editor to the new window
          editor.on("change", function () {
            newWindow.CKEDITOR.instances["popout-editor"].setData(
              editor.getData()
            );
          });
        };
        newWindow.document.head.appendChild(script);
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
