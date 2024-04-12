import boto3
from museum_of_dreams_project.settings.staging import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
# Then use the session to get the resource
s3 = session.resource("s3")
my_bucket = s3.Bucket("moddevbucket")
