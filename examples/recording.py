# Uses device minutes until the device is stopped or terminated. Task execution may incur costs. Recording storage may incur costs. Run: rye run python examples/recording.py DEVICE_ID
import sys
from pathlib import Path

from mobilerun_sdk import MobilerunSDK

if len(sys.argv) != 2:
    raise SystemExit("Pass an existing device ID")
sdk = MobilerunSDK()  # Reads MOBILERUN_API_KEY from the environment.
device = sdk.devices.from_id(sys.argv[1])
recording = device.recordings.start()
try:
    task = device.run(task="Open Settings")
    task.wait()
finally:
    recording.stop()
recording.wait()
Path("recording.mp4").write_bytes(recording.video())
