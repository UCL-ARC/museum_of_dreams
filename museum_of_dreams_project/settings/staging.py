from .aws import *

ENVIRONMENT = "staging"
ALLOWED_HOSTS = [
    "museumofdreams.eu-west-2.elasticbeanstalk.com",
    "staging.museumofdreamworlds.org",
    os.environ.get("PIP"),
]
GRAPPELLI_ADMIN_TITLE = "Museum of Dreams"
AWS_STORAGE_BUCKET_NAME = "moddevbucket"
AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
)
STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
