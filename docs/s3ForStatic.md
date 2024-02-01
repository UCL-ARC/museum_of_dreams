# Setting up S3 for static files and editor uploads

These instructions assume you are using CKEditor.

### In the codebase
In settings.py (settings/aws.py in our case as we only wanted to apply this to the staging and production versions) you need to have the following:

This tells CKeditor what to use for file uploads in the editor
```DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3.S3Storage"
```

To connect the app to AWS you'll need to define several variables (seen at the bottom of [aws.py](../museum_of_dreams_project/settings/aws.py)). You'll also need to create a file for some custom storage classes. [This tutorial](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/) outlines everything nicely. The only difference is you don't need to set up s3 to host a static website

 Make sure to copy the access key secret and ID for the variables mentioned above and input them into the EBS config for each server.

This should work, but if you've not set up HTTPS on your website, it may fail with 403 errors. You can check if the app recognises the buckets by seeing their contents after EBS deploys a fresh version after updating the config - you should see your static files in the bucket.
