from .base import *

from .. import secrets


SECRET_KEY = secrets.secret_key

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}
