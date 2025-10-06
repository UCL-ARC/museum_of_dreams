from .aws import *
from infrastructure.stacks.staging_stack import STAGING_ENV_NAME
import re

ENVIRONMENT = "staging"
ALLOWED_HOSTS = [
    re.compile(rf"^{STAGING_ENV_NAME}\.[a-zA-Z0-9]\.eu-west-2\.elasticbeanstalk\.com$"),
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
