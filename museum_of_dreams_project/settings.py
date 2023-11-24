import os

IS_LOCAL_DEV = os.environ.get("LOCAL_DEV", "False")

if IS_LOCAL_DEV == True:
    from .settings_files.local import *
else:
    from .settings_files.aws import *

    print(
        "DJANGO_SETTINGS_MODULE:",
        os.environ.get("DJANGO_SETTINGS_MODULE"),
        "STATIC_URL:",
        os.environ.get("STATIC_URL"),
    )
    print("AWS STATIC", STATIC_ROOT, STATIC_URL)
