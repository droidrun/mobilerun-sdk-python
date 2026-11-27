# Costs: existing mailbox rental may apply; no mailbox is created. Run: rye run python examples/mailbox-otp.py MAILBOX_ID
import sys

from mobilerun_sdk import MobilerunSDK

if len(sys.argv) != 2:
    raise SystemExit("Pass an existing mailbox ID")
sdk = MobilerunSDK()  # Reads MOBILERUN_API_KEY from the environment.
print(sdk.mailboxes.from_id(sys.argv[1]).wait_for_otp())
