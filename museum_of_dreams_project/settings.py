import os

IS_LOCAL_DEV = os.environ.get("LOCAL_DEV", "False")
print("IS_LOCAL_DEV", IS_LOCAL_DEV)

if IS_LOCAL_DEV != False:
    from .settings_files.local import *

    print("LOCAL SETTINGS USED")
else:
    from .settings_files.aws import *

    print("AWS SETTINGS USED")
