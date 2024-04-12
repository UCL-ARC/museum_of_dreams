from .base import *
import socket


SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

STATIC_ROOT = "static"
MEDIA_ROOT = "media"

ENVIRONMENT = "production"

# the health checks come from a local instance private IP
# and fail if not recognised as a valid host
LOCAL_IP = str(socket.gethostbyname(socket.gethostname()))

ALLOWED_HOSTS = [
    "museumofdreamworlds.eu-west-2.elasticbeanstalk.com",
    "museumofdreamworlds.org",
    LOCAL_IP,
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

#### Using S3 for static and media storage
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

CKEDITOR_CONFIGS = CKEDITOR_CONFIGS = generate_ckeditor_config(MEDIA_URL)

S3_BROWSER_SETTINGS = "djangoS3Browser"
