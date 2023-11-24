import os

IS_LOCAL_DEV = os.getenv("LOCAL_DEV", "False")
print(IS_LOCAL_DEV)

if IS_LOCAL_DEV:
    from .settings_files.local import *
else:
    from .settings_files.aws import *