# Uses device minutes until the device is stopped or terminated. Task execution may incur costs. Run: rye run python examples/typed-output.py DEVICE_ID
import sys

from pydantic import BaseModel

from mobilerun_sdk import MobilerunSDK


class Heading(BaseModel):
    heading: str


if len(sys.argv) != 2:
    raise SystemExit("Pass an existing device ID")
sdk = MobilerunSDK()  # Reads MOBILERUN_API_KEY from the environment.
device = sdk.devices.get(sys.argv[1])
task = device.run(task="Read the visible heading", output_schema=Heading)
result = task.wait_output()
heading: str = result.output.heading
print(heading)
