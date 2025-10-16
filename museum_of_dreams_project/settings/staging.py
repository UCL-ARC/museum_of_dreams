import os
import re

from .aws import *

AWS_STAGING_ENV_NAME = os.environ.get("AWS_STAGING_ENV_NAME", "none")

ENVIRONMENT = "staging"
if AWS_STAGING_ENV_NAME:
    ALLOWED_HOSTS = [
        re.compile(
            rf"^{AWS_STAGING_ENV_NAME}\.[a-zA-Z0-9]\.eu-west-2\.elasticbeanstalk\.com$"
        ),
        LOCAL_IP,
    ]
else:
    ALLOWED_HOSTS = [
        "museumofdreams.eu-west-2.elasticbeanstalk.com",
        "staging.museumofdreamworlds.org",
        LOCAL_IP,
    ]

GRAPPELLI_ADMIN_TITLE = "Museum of Dreams"
AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
)
STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
