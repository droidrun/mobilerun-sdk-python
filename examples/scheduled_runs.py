# Schedule then cancel without dispatching a device run. Pass an existing test flow ID.
import sys
from datetime import datetime, timezone, timedelta

from mobilerun_sdk import MobilerunSDK, ScheduledRun


def scheduled_runs(sdk: MobilerunSDK, flow_id: str) -> ScheduledRun:
    flow = sdk.workflows.flows.from_id(flow_id)
    schedule = flow.scheduled_runs.create(run_at=datetime.now(timezone.utc) + timedelta(minutes=10), payload={})
    failed = False
    try:
        if not any(item.id == schedule.id for item in flow.scheduled_runs.list()):
            raise RuntimeError("Schedule missing from list")
    except BaseException:
        failed = True
        raise
    finally:
        try:
            cancelled = schedule.cancel()
            if cancelled.data.status != "cancelled":
                raise RuntimeError("Schedule was not cancelled")
        except Exception:
            if not failed:
                raise
            print("Schedule cleanup failed for " + schedule.id, file=sys.stderr)
    for item in flow.scheduled_runs.list(status="all"):
        if item.id == schedule.id and item.status == "cancelled":
            return item
    raise RuntimeError("Cancelled schedule missing from list")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Pass an existing test flow ID")
    scheduled_runs(MobilerunSDK(), sys.argv[1])
