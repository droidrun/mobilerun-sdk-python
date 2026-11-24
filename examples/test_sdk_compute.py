from __future__ import annotations

import json
from typing import Any, Callable
from pathlib import Path

import httpx
import pytest

from mobilerun_sdk import (
    Run,
    Device,
    Sandbox,
    AsyncRun,
    AsyncDevice,
    RoutineFile,
    MobilerunSDK,
    ScheduledRun,
    BadRequestError,
    ComputeFunction,
    WaitFailureError,
    AsyncMobilerunSDK,
    AsyncScheduledRun,
)
from examples.compute import compute
from examples.stream_token import stream_token
from examples.routine_files import routine_files
from examples.scheduled_runs import scheduled_runs
from examples.compute_sandbox import compute_sandbox
from mobilerun_sdk.types.compute import RunRetrieveResponse

# Literal public response shapes; HTTP service/storage are the only fakes.
VERSION: dict[str, Any] = {
    "functionId": "fn-1",
    "version": 2,
    "status": "ready",
    "apiKey": {"permissions": {}},
    "inspectError": None,
    "inputSchema": {},
    "outputSchema": {},
    "outputKind": "value",
    "manifest": {"hosts": [], "credentials": [], "scopes": []},
    "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
    "sizeBytes": 12,
    "runtimeVersion": "r1",
    "createdAt": "2026-11-23T00:00:00Z",
}
FUNCTION: dict[str, Any] = {
    "id": "fn-1",
    "name": "greeting",
    "description": None,
    "latestVersion": {
        "functionId": "fn-1",
        "version": 2,
        "status": "ready",
        "apiKey": {"permissions": {}},
        "inspectError": None,
        "inputSchema": {},
        "outputSchema": {},
        "outputKind": "value",
        "manifest": {"hosts": [], "credentials": [], "scopes": []},
        "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
        "sizeBytes": 12,
        "runtimeVersion": "r1",
        "createdAt": "2026-11-23T00:00:00Z",
    },
    "latestReadyVersion": 2,
    "versionCount": 2,
    "createdAt": "2026-11-23T00:00:00Z",
    "updatedAt": "2026-11-23T00:00:00Z",
}
RUNNING: dict[str, Any] = {
    "id": "run-1",
    "functionId": "fn-1",
    "version": 2,
    "status": "running",
    "outcome": None,
    "errorCode": None,
    "logs": "pending",
    "startedAt": None,
    "endedAt": None,
    "durationMs": None,
    "usedSeconds": None,
    "input": {"name": "Ada"},
    "result": None,
    "stdout": "",
    "stderr": "",
    "truncated": False,
}
DONE: dict[str, Any] = {
    "id": "run-1",
    "functionId": "fn-1",
    "version": 2,
    "status": "done",
    "outcome": "partial",
    "errorCode": None,
    "logs": "available",
    "startedAt": None,
    "endedAt": None,
    "durationMs": None,
    "usedSeconds": None,
    "input": {"name": "Ada"},
    "result": {"message": "Hello, Ada!"},
    "stdout": "",
    "stderr": "",
    "truncated": False,
}
SANDBOX: dict[str, Any] = {
    "id": "box-1",
    "name": "fixture",
    "status": "running",
    "stopReason": None,
    "createdAt": "2026-11-23T00:00:00Z",
    "expiresAt": "2026-11-23T00:01:00Z",
    "stoppedAt": None,
    "idleTimeoutS": 60,
    "allowedHosts": [],
    "usedSeconds": 0,
}
SCHEDULE: dict[str, Any] = {
    "id": "schedule-1",
    "flowId": "flow-1",
    "status": "scheduled",
    "runAt": "2026-11-23T12:00:00Z",
    "payload": {},
    "executionIds": [],
    "skipReason": None,
    "error": None,
    "createdBy": "user-1",
    "createdAt": "2026-11-23T00:00:00Z",
    "finishedAt": None,
    "cancelledAt": None,
}
FILE: dict[str, Any] = {
    "id": "file-1",
    "filename": "report.bin",
    "folder": "reports",
    "kind": "file",
    "mimeType": "application/octet-stream",
    "sizeBytes": 4,
    "flowId": "flow-1",
    "flowName": "fixture",
    "flowDeleted": False,
    "executionId": "exec-1",
    "createdAt": None,
}
PAGE: dict[str, Any] = {"page": 1, "pages": 1, "hasNext": False, "pageSize": 1, "total": 1}
PAGE_MORE = {"page": 1, "pages": 2, "hasNext": True, "pageSize": 1, "total": 2}
PAGE_LAST = {"page": 2, "pages": 2, "hasNext": False, "pageSize": 1, "total": 2}
CONTENT = b"\x00\xff\x80\x0a"


def response(body: object) -> httpx.Response:
    return httpx.Response(200, json=body)


def transport(replies: list[httpx.Response]) -> tuple[MobilerunSDK, list[httpx.Request]]:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return replies.pop(0)

    sdk = MobilerunSDK(
        api_key="contract-fixture",
        base_url="https://api.example/v1",
        max_retries=0,
        http_client=httpx.Client(transport=httpx.MockTransport(handle), follow_redirects=True),
    )
    return sdk, requests


def test_compute_example_validates_inspects_numeric_versions_and_cleans_up() -> None:
    replies = [
        response({"data": {"id": "validation-1", "status": "done", "valid": True}}),
        response({"data": {"id": "validation-1", "status": "done", "valid": True}}),
        response({"data": FUNCTION}),
        response({"data": FUNCTION}),
        response({"data": {"source": "greeting"}}),
        response({"data": VERSION}),
        response({"data": VERSION}),
        response({"data": {"items": [VERSION], "pagination": PAGE}}),
        response({"data": {"items": [FUNCTION], "pagination": PAGE}}),
        response({"data": RUNNING}),
        response({"data": {**DONE, "logs": "pending"}}),
        response({"data": {**DONE, "logs": "pending"}}),
        response({"data": DONE}),
        response(
            {
                "data": {
                    "url": "https://storage.example/log",
                    "expiresAt": "2026-11-23T12:00:00Z",
                    "sizeBytes": 12,
                }
            }
        ),
        httpx.Response(204),
        httpx.Response(204),
    ]
    sdk, requests = transport(replies)
    finished, logs = compute(sdk, "greeting")
    assert finished.data.status == "done"
    assert finished.data.outcome == "partial"
    assert finished.data.logs == "pending"
    assert logs.data.url == "https://storage.example/log"
    assert [r.url.path for r in requests] == [
        "/v1/compute/functions/validations",
        "/v1/compute/functions/validations/validation-1",
        "/v1/compute/functions",
        "/v1/compute/functions/fn-1",
        "/v1/compute/functions/fn-1/source",
        "/v1/compute/functions/fn-1/versions",
        "/v1/compute/functions/fn-1/versions/2",
        "/v1/compute/functions/fn-1/versions",
        "/v1/compute/functions",
        "/v1/compute/functions/fn-1/runs",
        "/v1/compute/runs/run-1",
        "/v1/compute/runs/run-1",
        "/v1/compute/runs/run-1",
        "/v1/compute/runs/run-1/logs",
        "/v1/compute/functions/fn-1/versions/2",
        "/v1/compute/functions/fn-1",
    ]
    assert replies == []
    assert not hasattr(sdk, "functions")
    assert not hasattr(sdk.api, "functions")
    assert isinstance(sdk.compute.functions.from_id("fn-1"), ComputeFunction)


def test_function_run_factory_returns_global_run_and_failure_retains_response() -> None:
    sdk, requests = transport(
        [
            response({"data": RUNNING}),
            response({"data": {"id": "run-1", "status": "failed", "outcome": "failed"}}),
        ]
    )
    run = sdk.compute.functions.from_id("fn-1").runs.create(input={}, wait_s=0)
    assert isinstance(run, Run)
    with pytest.raises(WaitFailureError) as error:
        run.wait()
    assert isinstance(error.value.response, RunRetrieveResponse)
    assert error.value.response.data.status == "failed"
    assert run.status == "failed"
    assert requests[1].url.path == "/v1/compute/runs/run-1"


@pytest.mark.parametrize("logs", ["none", "gone"])
def test_unavailable_logs_fail_with_the_run_response(logs: str) -> None:
    sdk, requests = transport(
        [
            response({"data": {**DONE, "logs": logs}}),
        ]
    )
    with pytest.raises(WaitFailureError) as error:
        sdk.compute.runs.from_id("run-1").wait_logs()
    assert isinstance(error.value.response, RunRetrieveResponse)
    assert error.value.response.data.logs == logs
    assert len(requests) == 1


@pytest.mark.parametrize(
    ("resource", "item", "cls"),
    [("functions", FUNCTION, ComputeFunction), ("runs", DONE, Run), ("sandboxes", SANDBOX, Sandbox)],
)
def test_compute_pages_return_handles_and_preserve_page_size(resource: str, item: object, cls: type[object]) -> None:
    sdk, requests = transport(
        [
            response({"data": {"items": [item], "pagination": PAGE_MORE}}),
            response({"data": {"items": [item], "pagination": PAGE_LAST}}),
        ]
    )
    page = getattr(sdk.compute, resource).list(page_size=1)
    second = page.get_next_page()
    assert isinstance(page.items[0], cls)
    assert isinstance(second.items[0], cls)
    assert [r.url.params["page"] for r in requests] == ["1", "2"]
    assert [r.url.params["pageSize"] for r in requests] == ["1", "1"]


def test_function_update_get_and_run_pages_bind_function_id() -> None:
    sdk, requests = transport(
        [
            response({"data": FUNCTION}),
            response({"data": FUNCTION}),
            response({"data": {"items": [DONE], "pagination": PAGE_MORE}}),
            response({"data": {"items": [DONE], "pagination": PAGE_LAST}}),
        ]
    )
    fn = sdk.compute.functions.get("fn-1")
    assert isinstance(fn, ComputeFunction)
    fn.update(name="renamed")
    page = fn.runs.list(status="done", page_size=1)
    assert isinstance(page.get_next_page().items[0], Run)
    assert [(r.url.path, r.url.params["status"]) for r in requests[2:]] == [
        ("/v1/compute/functions/fn-1/runs", "done"),
        ("/v1/compute/functions/fn-1/runs", "done"),
    ]


def test_sandbox_example_and_binary_commands_cover_all_nine_operations() -> None:
    sdk, requests = transport(
        [
            response({"data": SANDBOX}),
            response({"data": {"items": [SANDBOX], "pagination": PAGE}}),
            response({"data": SANDBOX}),
            httpx.Response(204),
            response({"data": {"id": "cmd-1"}}),
            response({"data": {"items": []}}),
            response({"data": {"id": "cmd-1"}}),
            httpx.Response(204),
            httpx.Response(200, content=CONTENT, headers={"content-type": "application/octet-stream"}),
            httpx.Response(202, json={"data": {**SANDBOX, "status": "stopped"}}),
        ]
    )
    assert isinstance(compute_sandbox(sdk), Sandbox)
    sandbox = sdk.compute.sandboxes.from_id("box-1")
    sandbox.exec(command="printf ok")
    sandbox.commands.list()
    sandbox.commands.retrieve("cmd-1", wait_s=0)
    sandbox.files.upload(CONTENT, path="/tmp/check.bin")
    assert sandbox.files.download(path="/tmp/check.bin") == CONTENT
    sandbox.delete()
    assert requests[7].content == CONTENT
    assert requests[7].headers["content-type"] == "application/octet-stream"
    assert requests[7].url.params["path"] == "/tmp/check.bin"
    assert requests[6].url.path == "/v1/compute/sandboxes/box-1/commands/cmd-1"


def test_only_create_owned_sandboxes_dispose() -> None:
    sdk, requests = transport(
        [
            response({"data": SANDBOX}),
            response({"data": SANDBOX}),
            response({"data": {"items": [SANDBOX], "pagination": PAGE}}),
            httpx.Response(204),
        ]
    )
    owned = sdk.compute.sandboxes.create()
    with sdk.compute.sandboxes.get("box-1"):
        pass
    with sdk.compute.sandboxes.list().items[0]:
        pass
    with sdk.compute.sandboxes.from_id("box-1"):
        pass
    with owned:
        pass
    with owned:
        pass
    assert [r.method for r in requests] == ["POST", "GET", "GET", "DELETE"]


def test_scheduled_example_and_from_id_cancel_preserve_both_ids() -> None:
    sdk, requests = transport(
        [
            response({"data": SCHEDULE}),
            response({"items": [SCHEDULE], "pagination": PAGE}),
            response({"data": {**SCHEDULE, "status": "cancelled"}}),
            response({"items": [{**SCHEDULE, "status": "cancelled"}], "pagination": PAGE}),
            response({"data": {**SCHEDULE, "status": "cancelled"}}),
        ]
    )
    assert isinstance(scheduled_runs(sdk, "flow-1"), ScheduledRun)
    child = sdk.workflows.flows.from_id("flow-1").scheduled_runs.from_id("schedule-1")
    child.cancel(extra_body={"flowId": "wrong", "scheduledRunId": "wrong"})
    assert not hasattr(child, "refresh")
    assert not hasattr(sdk.workflows.flows.from_id("flow-1").scheduled_runs, "get")
    assert requests[4].url.path == "/v1/flows/flow-1/scheduled-runs/schedule-1/cancel"


def test_root_scheduled_pages_keep_flow_and_status() -> None:
    sdk, requests = transport(
        [
            response({"items": [SCHEDULE], "pagination": PAGE_MORE}),
            response({"items": [SCHEDULE], "pagination": PAGE_LAST}),
        ]
    )
    page = sdk.workflows.flows.from_id("flow-1").scheduled_runs.list(status="all", page_size=1)
    assert isinstance(page.get_next_page().items[0], ScheduledRun)
    assert [r.url.params["page"] for r in requests] == ["1", "2"]
    assert [r.url.params["status"] for r in requests] == ["all", "all"]


def test_routine_pages_snapshot_and_manager_delete_surfaces() -> None:
    sdk, requests = transport(
        [
            response({"items": [FILE], "pagination": PAGE_MORE}),
            response({"items": [FILE], "pagination": PAGE_LAST}),
            httpx.Response(204),
            response({"deleted": 2}),
        ]
    )
    page = sdk.routine_files.list(execution_id="exec-1", page_size=1)
    assert isinstance(page.items[0], RoutineFile)
    assert page.items[0].filename == "report.bin"
    assert isinstance(page.get_next_page().items[0], RoutineFile)
    handle = sdk.routine_files.from_id("file-1")
    assert handle.info is None
    assert not hasattr(handle, "refresh")
    assert not hasattr(handle, "delete_many")
    assert not hasattr(sdk.routine_files, "get")
    handle.delete()
    sdk.routine_files.delete_many(folder="reports")
    assert [r.url.params["page"] for r in requests[:2]] == ["1", "2"]
    assert [r.url.params["executionId"] for r in requests[:2]] == ["exec-1", "exec-1"]
    assert requests[2].url.path == "/v1/routine-files/file-1"
    assert requests[3].url.path == "/v1/routine-files"


def test_routine_example_native_httpx_redirect_preserves_bytes_without_authorization(tmp_path: Path) -> None:
    sdk, requests = transport(
        [
            response({"items": [], "pagination": PAGE}),
            response({"items": [FILE], "pagination": PAGE}),
            httpx.Response(302, headers={"location": "https://storage.example/blob"}),
            httpx.Response(200, content=CONTENT),
        ]
    )
    assert routine_files(sdk, "exec-1", tmp_path / "report.bin") == CONTENT
    assert (tmp_path / "report.bin").read_bytes() == CONTENT
    assert requests[2].headers["authorization"] == "Bearer contract-fixture"
    assert "authorization" not in requests[3].headers
    assert requests[3].url.host == "storage.example"


def test_device_token_binding_and_top_level_api_do_not_leak_snapshots() -> None:
    token = {"key": "fixture-only-secret", "keyId": "key-1", "expiresAt": "2026-11-23T12:00:00Z"}
    sdk, requests = transport([response(token), httpx.Response(204), response(token), httpx.Response(204)])
    stream_token(sdk, "device-1", ["https://app.example"])
    device = sdk.devices.from_id("device-1")
    device.create_stream_token(ttl_seconds=120, extra_body={"deviceId": "wrong"})
    sdk.stream_tokens.delete("key-1")
    assert json.loads(requests[0].content) == {
        "deviceId": "device-1",
        "ttlSeconds": 120,
        "allowedOrigins": ["https://app.example"],
    }
    assert json.loads(requests[2].content) == {"deviceId": "device-1", "ttlSeconds": 120}
    assert device.info is None
    assert token["key"] not in repr(device)
    assert token["key"] not in json.dumps(device.info)
    assert callable(sdk.stream_tokens.create)


def test_cleanup_does_not_hide_initial_http_error() -> None:
    sdk, requests = transport(
        [
            response({"data": SANDBOX}),
            httpx.Response(400, json={"message": "initial failure"}),
            httpx.Response(400, json={"message": "cleanup failure"}),
        ]
    )
    with pytest.raises(BadRequestError, match="initial failure"):
        compute_sandbox(sdk)
    assert requests[2].method == "DELETE"


@pytest.mark.parametrize("scenario", ["compute", "scheduled", "stream", "routine"])
def test_examples_propagate_native_http_failure(scenario: str, tmp_path: Path) -> None:
    sdk, _ = transport([httpx.Response(400, json={"message": "initial failure"})])
    scenarios: dict[str, Callable[[], object]] = {
        "compute": lambda: compute(sdk, "greeting"),
        "scheduled": lambda: scheduled_runs(sdk, "flow-1"),
        "stream": lambda: stream_token(sdk, "device-1"),
        "routine": lambda: routine_files(sdk, "exec-1", tmp_path / "unused"),
    }
    with pytest.raises(BadRequestError):
        scenarios[scenario]()


@pytest.mark.asyncio
async def test_async_global_run_wait_and_scheduled_parent_binding() -> None:
    replies = [
        response({"data": RUNNING}),
        response({"data": DONE}),
        response({"data": {**SCHEDULE, "status": "cancelled"}}),
    ]
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return replies.pop(0)

    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as http_client:
        sdk = AsyncMobilerunSDK(
            api_key="contract-fixture",
            base_url="https://api.example/v1",
            max_retries=0,
            http_client=http_client,
        )
        run = await sdk.compute.functions.from_id("fn-1").runs.create(input={}, wait_s=0)
        assert isinstance(run, AsyncRun)
        assert (await run.wait(timeout=1)).data.status == "done"
        child = sdk.workflows.flows.from_id("flow-1").scheduled_runs.from_id("schedule-1")
        assert isinstance(child, AsyncScheduledRun)
        await child.cancel(extra_body={"flowId": "wrong"})
    assert [r.url.path for r in requests] == [
        "/v1/compute/functions/fn-1/runs",
        "/v1/compute/runs/run-1",
        "/v1/flows/flow-1/scheduled-runs/schedule-1/cancel",
    ]


def test_global_run_get_refresh_and_object_version_retrieval() -> None:
    sdk, requests = transport(
        [
            response({"data": RUNNING}),
            response({"data": DONE}),
            response({"data": VERSION}),
        ]
    )
    run = sdk.compute.runs.get("run-1")
    assert isinstance(run, Run)
    run.refresh()
    assert run.status == "done"
    sdk.compute.functions.from_id("fn-1").versions.retrieve(2)
    assert [r.url.path for r in requests] == [
        "/v1/compute/runs/run-1",
        "/v1/compute/runs/run-1",
        "/v1/compute/functions/fn-1/versions/2",
    ]


def test_run_wait_rejects_a_response_that_spans_its_deadline(monkeypatch: pytest.MonkeyPatch) -> None:
    from mobilerun_sdk import WaitTimeoutError

    clock = [0.0]
    monkeypatch.setattr("mobilerun_sdk.sdk._common.time.monotonic", lambda: clock[0])

    def slow_response(_request: httpx.Request) -> httpx.Response:
        clock[0] = 0.02
        return response({"data": RUNNING})

    with httpx.Client(transport=httpx.MockTransport(slow_response)) as http_client:
        sdk = MobilerunSDK(
            api_key="contract-fixture",
            base_url="https://api.example/v1",
            max_retries=0,
            http_client=http_client,
        )
        with pytest.raises(WaitTimeoutError):
            sdk.compute.runs.from_id("run-1").wait(timeout=0.01)


def test_compute_failure_confirms_cancel_before_deleting_function() -> None:
    sdk, requests = transport(
        [
            response({"data": {"id": "validation-1", "status": "done", "valid": True}}),
            response({"data": {"id": "validation-1", "status": "done", "valid": True}}),
            response({"data": FUNCTION}),
            response({"data": FUNCTION}),
            response({"data": {"source": "greeting"}}),
            response({"data": VERSION}),
            response({"data": VERSION}),
            response({"data": {"items": [VERSION], "pagination": PAGE}}),
            response({"data": {"items": [FUNCTION], "pagination": PAGE}}),
            response({"data": RUNNING}),
            httpx.Response(400, json={"message": "initial run failure"}),
            response({"data": RUNNING}),
            response({"data": {**DONE, "status": "failed", "outcome": "failed", "errorCode": "cancelled"}}),
            httpx.Response(204),
            httpx.Response(204),
        ]
    )
    with pytest.raises(BadRequestError, match="initial run failure"):
        compute(sdk, "greeting")
    assert [(r.method, r.url.path) for r in requests[11:]] == [
        ("POST", "/v1/compute/runs/run-1/cancel"),
        ("GET", "/v1/compute/runs/run-1"),
        ("DELETE", "/v1/compute/functions/fn-1/versions/2"),
        ("DELETE", "/v1/compute/functions/fn-1"),
    ]


def test_stream_token_without_key_id_preserves_shape_error_without_revocation() -> None:
    sdk, requests = transport([response({"key": "fixture-only-secret", "expiresAt": "2026-11-23T12:00:00Z"})])
    with pytest.raises(RuntimeError, match="Invalid token response"):
        stream_token(sdk, "device-1")
    assert [request.method for request in requests] == ["POST"]


IDLE_DEVICE = {
    "id": "device-1",
    "name": "fixture",
    "state": "ready",
    "stateMessage": "",
    "streamUrl": "",
    "type": "cloud",
    "platform": "android",
    "createdAt": "2026-11-24T00:00:00Z",
    "updatedAt": "2026-11-24T00:00:00Z",
    "assignedAt": None,
    "terminatesAt": None,
    "taskCount": 0,
    "activeTaskId": "",
    "idleTimeoutSource": "default",
    "idleTimeoutMinutes": 15,
}


@pytest.mark.parametrize("minutes", [30, 0, None])
def test_device_idle_timeout_returns_fresh_handle(minutes: int | None) -> None:
    sdk, requests = transport([response(IDLE_DEVICE), response(IDLE_DEVICE)])
    device = sdk.devices.from_id("device-1")
    raw = sdk.api.devices.update_idle_timeout("device-1", minutes=minutes)
    updated = device.set_idle_timeout(minutes)
    assert raw.id == "device-1"
    assert isinstance(updated, Device)
    assert updated is not device
    assert updated.id == "device-1"
    assert updated.info is not None
    assert updated.info.idle_timeout_minutes == 15
    assert updated.info.idle_timeout_source == "default"
    assert device.info is None
    assert [r.method for r in requests] == ["PUT", "PUT"]
    assert [r.url.path for r in requests] == [
        "/v1/devices/device-1/idle-timeout",
        "/v1/devices/device-1/idle-timeout",
    ]
    assert [json.loads(r.content) for r in requests] == [{"minutes": minutes}, {"minutes": minutes}]


@pytest.mark.asyncio
@pytest.mark.parametrize("minutes", [30, 0, None])
async def test_async_device_idle_timeout_returns_fresh_handle(minutes: int | None) -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return response(IDLE_DEVICE)

    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as client:
        sdk = AsyncMobilerunSDK(
            api_key="contract-fixture",
            base_url="https://api.example/v1",
            max_retries=0,
            http_client=client,
        )
        device = sdk.devices.from_id("device-1")
        updated = await device.set_idle_timeout(minutes)
    assert isinstance(updated, AsyncDevice)
    assert updated is not device
    assert updated.id == "device-1"
    assert updated.info is not None
    assert updated.info.idle_timeout_minutes == 15
    assert device.info is None
    assert requests[0].method == "PUT"
    assert requests[0].url.path == "/v1/devices/device-1/idle-timeout"
    assert json.loads(requests[0].content) == {"minutes": minutes}
