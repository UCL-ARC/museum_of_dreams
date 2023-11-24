import os

IS_LOCAL_DEV = os.environ.get("LOCAL_DEV", False)
print("IS_LOCAL_DEV", IS_LOCAL_DEV)

if IS_LOCAL_DEV is not False:
    print("LOCAL SETTINGS USED")
    from .settings_files.local import *

else:
    print("AWS SETTINGS USED")
    from .settings_files.aws import *
