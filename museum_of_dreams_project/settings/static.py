from storages.backends.s3boto3 import S3Boto3Storage
import aws


class StaticStorage(S3Boto3Storage):
    location = aws.STATIC_ROOT


class MediaStorage(S3Boto3Storage):
    location = aws.MEDIA_ROOT
