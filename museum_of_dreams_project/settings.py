import os

IS_LOCAL_DEV = os.environ.get("LOCAL_DEV", "False")

if IS_LOCAL_DEV:
    from settings.local import *
else:
    from settings.aws import *
