from .aws import *

ENVIRONMENT = "staging"
DEBUG = True

ALLOWED_HOSTS = [
    "museumofdreams.eu-west-2.elasticbeanstalk.com",
    "staging.museumofdreamworlds.org",
]
GRAPPELLI_ADMIN_TITLE = "Museum of Dreams"
AWS_STORAGE_BUCKET_NAME = "moddevbucket"
