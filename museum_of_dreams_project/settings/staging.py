from .aws import LOCAL_IP, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import os

ENVIRONMENT = "staging"
ALLOWED_HOSTS = [
    ".elasticbeanstalk.com",
    "museumofdreams.eu-west-2.elasticbeanstalk.com",
    "staging.museumofdreamworlds.org",
    LOCAL_IP,
]
GRAPPELLI_ADMIN_TITLE = "Museum of Dreams"
AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("RDS_DB_NAME", "none"),
        "USER": os.environ.get("RDS_USERNAME", "none"),
        "PASSWORD": os.environ.get("RDS_PASSWORD", "none"),
        "HOST": os.environ.get("RDS_HOSTNAME", "none"),
        "PORT": os.environ.get("RDS_PORT", "none"),
    }
}

STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
