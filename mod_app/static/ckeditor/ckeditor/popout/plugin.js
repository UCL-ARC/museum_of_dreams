// plugin.js
CKEDITOR.plugins.add("popout", {
  icons: "popout",
  init: function (editor) {
    editor.addCommand("popout", {
      exec: function (editor) {
        // Open a new window
        var newWindow = window.open("", "_blank", "width=800,height=600");

        // Write a basic HTML structure to the new window
        newWindow.document.write(
          '<html><head></head><body><textarea id="editor"></textarea></body></html>'
        );
        newWindow.document.close();

        // Load CKEditor script in the new window
        var script = newWindow.document.createElement("script");
        script.type = "text/javascript";
        script.src = "//cdn.ckeditor.com/4.16.0/standard/ckeditor.js";
        script.onload = function () {
          newWindow.CKEDITOR.replace("editor", {
            // Optionally, you can pass existing editor content to the new editor
            on: {
              instanceReady: function () {
                newWindow.CKEDITOR.instances.editor.setData(editor.getData());
              },
            },
          });

          // Sync data from the new window to the original editor
          newWindow.CKEDITOR.instances.editor.on("change", function () {
            editor.setData(newWindow.CKEDITOR.instances.editor.getData());
          });

          // Sync data from the original editor to the new window
          editor.on("change", function () {
            newWindow.CKEDITOR.instances.editor.setData(editor.getData());
          });
        };
        newWindow.document.head.appendChild(script);
      },
    });

    editor.ui.addButton("Popout", {
      label: "Open in new window",
      command: "popout",
      toolbar: "document",
      icon: this.path + "open_in_new.svg",
    });
  },
});
