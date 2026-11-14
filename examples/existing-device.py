# Uses device minutes until the device is stopped or terminated. Run: rye run python examples/existing-device.py DEVICE_ID
import sys

from mobilerun_sdk import MobilerunSDK

if len(sys.argv) != 2:
    raise SystemExit("Pass an existing device ID")
sdk = MobilerunSDK()  # Reads MOBILERUN_API_KEY from the environment.
device = sdk.devices.get(sys.argv[1])
device.home()
device.open_app("com.android.settings")
device.back()
device.screenshot().save("screenshot.png")
for existing in sdk.devices.list():
    print(existing.id, existing.name)
