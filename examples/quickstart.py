# Uses device minutes until the device is stopped or terminated. Task execution may incur costs. Run: rye run python examples/quickstart.py
from mobilerun_sdk import MobilerunSDK

sdk = MobilerunSDK()  # Reads MOBILERUN_API_KEY from the environment.
device = sdk.devices.create(billing="minute", device_type="android_cloud_phone")
try:
    task = device.run(task="Open Settings")
    print(task.wait().status)
finally:
    device.stop()
