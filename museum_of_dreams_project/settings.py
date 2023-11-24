import os

IS_LOCAL_DEV = os.getenv("LOCAL_DEV", "False")

if IS_LOCAL_DEV == True:
    from .settings_files.local import *
else:
    from .settings_files.aws import *
