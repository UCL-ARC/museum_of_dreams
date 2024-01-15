# Setting up S3 for static files and editor uploads

These instructions assume you are using CKEditor.

### In the codebase
In settings.py (settings/aws.py in our case as we only wanted to apply this to the staging and production versions) you need to have the following:

This tells CKeditor what to use for file uploads in the editor
```DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3.S3Storage"
```

To connect the app to AWS you'll need to define the following, which you can store the value for in the ElasticBeanstalk config with other environment variables.
`AWS_ACCESS_KEY_ID`
`AWS_SECRET_ACCESS_KEY`
`AWS_STORAGE_BUCKET_NAME`
`AWS_S3_REGION_NAME` - this should remain consistent so can be defined here or on EBS

### On AWS
As mentioned above, you'll want to store values for some of the variables in the EBS config. In order to get these values, you'll need to create a s3 bucket.

Go to the s3 console and click "create a new bucket". Select you region and choose `General Purpose` for the type. Name the bucket and uncheck `block all public access`. Everything else can be left as default.

You then need to go to the IAM console and create a new user, attaching the `S3FullAccess` policy to it. Create a new access key (which can be used for both prod and staging, or you can create separate ones). Make sure to copy the access key secret and ID for the variables above and input them into the EBS config for each server.

This should work, but if you've not set up HTTPS on your website, it may fail with 403 errors. You can check if the app recognises the buckets by seeing their contents after EBS deploys a fresh version after updating the config - you should see your static files in the bucket.
