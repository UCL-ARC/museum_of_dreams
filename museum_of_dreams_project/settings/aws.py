from base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    "3.11.242.245",  # AWS EC2 public IPv4 for prod
    "35.179.22.251",
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
