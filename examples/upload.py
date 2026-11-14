# Uploading uses storage quota and may incur storage charges.
# Usage: python examples/upload.py app.apk com.example.app "Example" 1 1.0
import sys
from pathlib import Path

from mobilerun_sdk import MobilerunSDK

if len(sys.argv) != 6:
    raise SystemExit("Usage: upload.py FILE BUNDLE_ID DISPLAY_NAME VERSION_CODE VERSION_NAME")
sdk = MobilerunSDK()
app = sdk.apps.upload(
    files=[Path(sys.argv[1])],
    bundle_id=sys.argv[2],
    display_name=sys.argv[3],
    version_code=float(sys.argv[4]),
    version_name=sys.argv[5],
)
print(app.id)
