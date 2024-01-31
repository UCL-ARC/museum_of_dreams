from storages.backends.s3boto3 import S3Boto3Storage
from .museum_of_dreams_project.settings.aws import STATIC_ROOT, MEDIA_ROOT


class StaticStorage(S3Boto3Storage):
    location = STATIC_ROOT


class MediaStorage(S3Boto3Storage):
    location = MEDIA_ROOT
