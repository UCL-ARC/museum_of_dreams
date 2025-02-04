from .base import *
import socket


SECRET_KEY = os.environ.get("SECRET_KEY", "none")

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
        "NAME": os.environ.get("RDS_DB_NAME", "none"),
        "USER": os.environ.get("RDS_USERNAME", "none"),
        "PASSWORD": os.environ.get("RDS_PASSWORD", "none"),
        "HOST": os.environ.get("RDS_HOSTNAME", "none"),
        "PORT": os.environ.get("RDS_PORT", "none"),
    }
}
GRAPPELLI_ADMIN_TITLE = "Museum of Dreamworlds"

#### Using S3 for static and media storage
AWS_QUERYSTRING_AUTH = False  # needed by grappelli to work with s3

DEFAULT_FILE_STORAGE = "static.MediaStorage"
STATICFILES_STORAGE = "static.StaticStorage"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "none")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "none")
AWS_STORAGE_BUCKET_NAME = os.environ.get("BUCKET_NAME", "none")
AWS_S3_REGION_NAME = "eu-west-2"
AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
)

# Email functionality
EMAIL_BACKEND = "django_ses.SESBackend"
AWS_SES_REGION_NAME = "eu-west-2"


STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN


S3_BROWSER_SETTINGS = "djangoS3Browser"

CKEDITOR_CONFIGS["default"]["staticUrl"] = f"{STATIC_URL}"
