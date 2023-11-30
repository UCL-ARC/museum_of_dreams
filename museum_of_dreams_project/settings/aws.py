from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

STATIC_ROOT = "static"


ALLOWED_HOSTS = [
    "museumofdreams.eu-west-2.elasticbeanstalk.com",
    "museumofdreamworlds.eu-west-2.elasticbeanstalk.com",
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
