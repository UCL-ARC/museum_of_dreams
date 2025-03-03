# Adding Plugins to CK Editor

- Download the plugin from CKE 4
- unpack the zip file
- in the codebase, create a new folder with the plugin name under `/mod_app/static/ckeditor/plugins/`
- from the unpacked zip, you mainly need the plugin.js file but some other files can/should be included, especially if you need icons
- in `/museum_of_dreams_project/settings/base.py` update `CKEDITOR_CONFIGS.default.extraPlugins` to include the name of the plugin and if it should have a button, add it in the toolbar section as well
