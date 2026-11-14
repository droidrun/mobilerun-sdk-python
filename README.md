# Mobilerun Python API library

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/mobilerun-sdk.svg?label=pypi%20(stable))](https://pypi.org/project/mobilerun-sdk/)

The Mobilerun Python library provides convenient access to the Mobilerun REST API from any Python 3.10+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

The full API of this library can be found in [api.md](api.md).

## Installation

```sh
pip install mobilerun-sdk
```

## Usage

Creating a device uses device minutes until you stop or terminate it. This example selects minute billing and stops the device at the end.

```python
from mobilerun_sdk import MobilerunSDK

sdk = MobilerunSDK()
device = sdk.devices.create(billing="minute", device_type="android_cloud_phone")
try:
    task = device.run(task="Open Settings")
    result = task.wait()
    print(result.status, device.name)
finally:
    device.stop()
```

Stopping requires a device type that supports stop; otherwise use `device.terminate()`.

### Full client (`.api`)

The full API of this library can be found in [api.md](api.md).

```python
import os
from mobilerun_sdk import Mobilerun

client = Mobilerun(
    api_key=os.environ.get("MOBILERUN_API_KEY"),  # This is the default and can be omitted
)

devices = client.devices.list()
print(devices.items)
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `MOBILERUN_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.

## Object API

The object API is additive. Existing client APIs are unchanged and the complete raw client is available as `.api`. Properties such as `device.name` and `task.status` read the last response in `info` without making a request. Call `refresh()` to update it. Object-layer logs show class, ID and declared fields, never `info` or the client; the explicit `.api` escape hatch stays raw. Waits poll with bounded requests and back off on 408/409/429/5xx.

### Objects

| Object             | How to get it                    | Main methods                                                                                 |
| ------------------ | -------------------------------- | -------------------------------------------------------------------------------------------- |
| Device             | `sdk.devices`                    | `get, list, create, run, screenshot, recordings`                                             |
| Task               | `sdk.tasks / device.run()`       | `run, get, list, wait, wait_output`                                                          |
| App                | `sdk.apps`                       | `get, list, upload, delete, list_versions`                                                   |
| ProxyConfiguration | `sdk.proxies`                    | `get, list, create, update, delete`                                                          |
| Trigger            | `sdk.workflows.triggers`         | `get, list, create, update, delete, fire`                                                    |
| WorkflowAction     | `sdk.workflows.actions`          | `get, list, create, update, delete`                                                          |
| CatalogEntry       | `sdk.workflows.action_catalog`   | `get, list`                                                                                  |
| Flow               | `sdk.workflows.flows`            | `get, list, create, clone, run, verify`                                                      |
| Execution          | `sdk.workflows.executions`       | `get, list, wait`                                                                            |
| Agent              | `sdk.agents`                     | `create, list, profile.update, files.list, conversations, routines, requests.list_for_agent` |
| AgentRequest       | `sdk.agents.requests`            | `get, list, retrieve_by_session`                                                             |
| AgentFile          | `sdk.files / agent.files.list()` | `upload, list, update, delete, confirm, cancel_pending, download`                            |
| ConnectUser        | `sdk.connect.users`              | `get, list, create, update, delete, list_connections`                                        |
| ConnectProxy       | `sdk.connect.proxies`            | `get, list, buy, update, ping, ensure_healthy, checkout, cancel`                             |
| CredentialPackage  | `sdk.credentials.packages`       | `get, list, create, credentials`                                                             |
| Credential         | `package.credentials`            | `create, list, delete, fields`                                                               |
| NumberMessage      | `sdk.messages`                   | `get, list`                                                                                  |
| Mailbox            | `sdk.mailboxes`                  | `get, list, create, wait_for_otp, messages`                                                  |
| MailboxMessage     | `mailbox.messages`               | `get, list`                                                                                  |
| PhoneNumber        | `sdk.numbers`                    | `get, list, create, send, messages.list, wait_until_active`                                  |
| Webhook            | `sdk.webhooks`                   | `get, list, create, verify, update, delete, test, rotate_secret`                             |
| TrafficSession     | `device.traffic_sessions`        | `create, get, list, delete`                                                                  |
| MailboxConnection  | `sdk.mailboxes.connections`      | `create, get`                                                                                |
| SavedScreenshot    | `device.screenshots`             | `list, image, delete`                                                                        |
| WebhookDelivery    | `webhook.deliveries`             | `get, list`                                                                                  |
| Recording          | `device.recordings`              | `get, list, start, stop, wait, delete, trajectory, video, screenshots`                       |

Every manager has `fromId(id)` / `from_id(id)` for an unfetched handle. Child managers carry their parent context. Agent and AgentFile have no get or refresh: their fields carry only the last create/list snapshot; fromId/from_id handles have no data. Agent profile.update returns a fresh Agent and leaves the original snapshot unchanged. Package get retains the full credentials-array response and takes its canonical name from the first row; an empty response keeps the requested name. Credential list maps that same package route to child handles. Recording start is its only factory and owns stop on scope exit; handles from get/list/fromId never stop automatically. Recording video/trajectory and AgentFile download return bytes. SavedScreenshot.image returns bytes; Screenshot remains the capture result returned by device.screenshot().

Object purchase methods keep the API's own operation name:

- Device.create uses device minutes until the device is stopped or terminated.
- ConnectProxy.buy and ConnectProxy.checkout can incur upstream proxy charges.
- PhoneNumber.create can incur upstream number rental charges.
- Mailbox.create and Mailbox.restart can incur upstream mailbox rental charges; included capacity may apply.

### Upload an app

Uploading uses storage quota and may incur storage charges. A string upload input always names a local file path. Paths stream from disk with a measured Content-Length; bytes and binary file objects can specify metadata with `UploadFile(data, filename=..., content_type=...)`. `sdk.files.upload(file=Path("notes.txt"))` uploads an agent file. Cleanup runs best-effort only for definite failures before confirmation; ambiguous confirm failures and failures after successful confirmation do not mark the upload failed; `UploadError.__cause__` retains the original failure. Sync and async clients share the same inputs.

```python
from pathlib import Path
from mobilerun_sdk import MobilerunSDK

sdk = MobilerunSDK()
app = sdk.apps.upload(
    bundle_id="com.example.app",
    display_name="Example",
    version_code=1,
    version_name="1.0",
    files=[Path("app.apk")],
)
print(app.id)
```

### Verify webhook signatures

Verify the exact raw body before JSON parsing. Deduplicate replays within the tolerance window using an ID inside the signed body, never the unsigned `x-mobilerun-event-id` header. The helper needs the endpoint signing secret, but no API key. It checks both past and future timestamps with a five-minute tolerance. `sdk.webhooks.verify` offers the same synchronous verification on both clients. Failures raise `WebhookVerificationError` with a `reason` code. `now` is epoch seconds; `tolerance` overrides the tolerance in seconds.

```python
import os
from http.server import BaseHTTPRequestHandler
from mobilerun_sdk import verify_webhook


class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        verify_webhook(
            body,
            {name: self.headers.get_all(name) for name in self.headers},
            os.environ["WEBHOOK_SECRET"],
        )
        self.send_response(204)
        self.end_headers()
```

### Existing devices and screenshots

```python
from mobilerun_sdk import MobilerunSDK

sdk = MobilerunSDK()
device = sdk.devices.get("device-id")
device.home()
device.open_app("com.android.settings")
device.back()
device.stop_app("com.android.settings")
device.swipe(300, 800, 300, 200, 400)
screenshot = device.screenshot()
screenshot.save("screenshot.png")
for existing in sdk.devices.list():
    print(existing.id, existing.name, existing.state)
```

### Park and wake a device

```python
from mobilerun_sdk import MobilerunSDK

device = MobilerunSDK().devices.from_id("device-id")
device.stop()
# Later, when the customer returns:
device.resume()
```

Both methods return the handle once the device has reached its target state: stopped or ready; async clients use `await`.

### Typed task output

`wait_output` validates output with the supplied Pydantic model and returns `WaitOutput` containing `output` and the raw `response`. Validation failures raise `OutputValidationError` with `object_id` and the response.

```python
from pydantic import BaseModel
from mobilerun_sdk import MobilerunSDK


class Heading(BaseModel):
    heading: str


sdk = MobilerunSDK()
device = sdk.devices.get("device-id")
task = device.run(task="Read the visible heading", output_schema=Heading)
result = task.wait_output()
heading: str = result.output.heading
print(heading)
```

### Recording uploads

```python
from pathlib import Path
from mobilerun_sdk import MobilerunSDK

sdk = MobilerunSDK()
device = sdk.devices.from_id("device-id")
recording = device.recordings.start()
task = device.run(task="Open Settings")
task.wait()
recording.stop()
recording.wait()
video = recording.video()
Path("recording.mp4").write_bytes(video)
```

The async client uses `await` for start, stop, wait and video.

The Python SDK runs on your server; to show a device in a web app, pass `device.info.stream_url` and `device.info.stream_token` for a device the authenticated end user may see to the frontend and render it with [`@mobilerun/react`](https://github.com/droidrun/mobilerun-react#readme), keeping the API key on the server.

### Automatic cleanup and async

If readiness inside `create` fails, the new resource is disposed best-effort by default; set `dispose_on_ready_failure=False` to retain it. `ObjectReadyError` keeps the handle and readiness cause, with `disposed` and `cleanup_error` reporting cleanup; async cancellation keeps its original exception type after shielded cleanup.

Only lifecycle factories own their resources: `create` normally, and `Recording.start` for recordings. `with` and `async with` terminate that device on exit. Handles from `get`, `from_id`, lists and returned task handles do not clean up automatically. The async client provides the same methods with `await`.

```python
from mobilerun_sdk import MobilerunSDK, AsyncMobilerunSDK

sdk = MobilerunSDK()
with sdk.devices.create(billing="minute", device_type="android_cloud_phone") as device:
    device.run(task="Open Settings").wait()


async def run_once() -> None:
    sdk = AsyncMobilerunSDK()
    async with await sdk.devices.create(
        billing="minute", device_type="android_cloud_phone"
    ) as device:
        task = await device.run(task="Open Settings")
        await task.wait()
```

Examples: see [`examples/`](https://github.com/droidrun/mobilerun-sdk-python/tree/HEAD/examples)

## Async usage

Simply import `AsyncMobilerun` instead of `Mobilerun` and use `await` with each API call:

```python
import os
import asyncio
from mobilerun_sdk import AsyncMobilerun

client = AsyncMobilerun(
    api_key=os.environ.get("MOBILERUN_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    devices = await client.devices.list()
    print(devices.items)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from the production repo
pip install 'mobilerun-sdk[aiohttp] @ git+ssh://git@github.com/droidrun/mobilerun-sdk-python.git'
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from mobilerun_sdk import DefaultAioHttpClient
from mobilerun_sdk import AsyncMobilerun


async def main() -> None:
    async with AsyncMobilerun(
        api_key=os.environ.get("MOBILERUN_API_KEY"),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        devices = await client.devices.list()
        print(devices.items)


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from mobilerun_sdk import Mobilerun

client = Mobilerun()

device = client.devices.create(
    carrier={
        "gsm_operator_alpha": "GsmOperatorAlpha",
        "gsm_operator_numeric": 0,
        "gsm_sim_operator_alpha": "GsmSimOperatorAlpha",
        "gsm_sim_operator_iso_country": "GsmSimOperatorIsoCountry",
        "gsm_sim_operator_numeric": 0,
        "persist_sys_timezone": "PersistSysTimezone",
    },
)
print(device.carrier)
```

## File uploads

Request parameters that correspond to file uploads can be passed as `bytes`, or a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from mobilerun_sdk import Mobilerun

client = Mobilerun()

client.devices.files.upload(
    device_id="deviceId",
    path="path",
    file=Path("/path/to/file"),
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `mobilerun_sdk.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `mobilerun_sdk.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `mobilerun_sdk.APIError`.

```python
import mobilerun_sdk
from mobilerun_sdk import Mobilerun

client = Mobilerun()

try:
    client.devices.list()
except mobilerun_sdk.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except mobilerun_sdk.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except mobilerun_sdk.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from mobilerun_sdk import Mobilerun

# Configure the default for all requests:
client = Mobilerun(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).devices.list()
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from mobilerun_sdk import Mobilerun

# Configure the default for all requests:
client = Mobilerun(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Mobilerun(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).devices.list()
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `MOBILERUN_LOG` to `info`.

```shell
$ export MOBILERUN_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from mobilerun_sdk import Mobilerun

client = Mobilerun()
response = client.devices.with_raw_response.list()
print(response.headers.get('X-My-Header'))

device = response.parse()  # get the object that `devices.list()` would have returned
print(device.items)
```

These methods return an [`APIResponse`](https://github.com/droidrun/mobilerun-sdk-python/tree/main/src/mobilerun_sdk/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/droidrun/mobilerun-sdk-python/tree/main/src/mobilerun_sdk/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.devices.with_streaming_response.list() as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from mobilerun_sdk import Mobilerun, DefaultHttpxClient

client = Mobilerun(
    # Or use the `MOBILERUN_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from mobilerun_sdk import Mobilerun

with Mobilerun() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/droidrun/mobilerun-sdk-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import mobilerun_sdk
print(mobilerun_sdk.__version__)
```

## Requirements

Python 3.10 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
