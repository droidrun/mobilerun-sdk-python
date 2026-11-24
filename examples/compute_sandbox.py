# Compute charges apply until stopped. Run: rye run python examples/compute_sandbox.py
import sys

from mobilerun_sdk import Sandbox, MobilerunSDK


def compute_sandbox(sdk: MobilerunSDK) -> Sandbox:
    sandbox = sdk.compute.sandboxes.create(timeout_s=60, idle_timeout_s=60)
    failed = False
    try:
        sdk.compute.sandboxes.list()
        return sdk.compute.sandboxes.get(sandbox.id)
    except BaseException:
        failed = True
        raise
    finally:
        try:
            sandbox.delete()
        except Exception:
            if not failed:
                raise
            print("Sandbox cleanup failed for " + sandbox.id, file=sys.stderr)


if __name__ == "__main__":
    compute_sandbox(MobilerunSDK())
