from .base import *


SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

STATIC_ROOT = "static"
MEDIA_ROOT = "media"

ENVIRONMENT = "production"

ALLOWED_HOSTS = [
    "museumofdreamworlds.eu-west-2.elasticbeanstalk.com",
    "museumofdreamworlds.org",
    os.environ.get("PIP"),
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["RDS_DB_NAME"],
        "USER": os.environ["RDS_USERNAME"],
        "PASSWORD": os.environ["RDS_PASSWORD"],
        "HOST": os.environ["RDS_HOSTNAME"],
        "PORT": os.environ["RDS_PORT"],
    }
}
GRAPPELLI_ADMIN_TITLE = "Museum of Dreamworlds"
AWS_QUERYSTRING_AUTH = False  # needed by grappelli to work with s3


DEFAULT_FILE_STORAGE = "static.MediaStorage"
STATICFILES_STORAGE = "static.StaticStorage"

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = "modprodbucket"
AWS_S3_REGION_NAME = "eu-west-2"
AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
)
STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
