# Shared Types

```python
from mobilerun.types import (
    Config,
    DeviceCarrier,
    DeviceIdentifiers,
    DeviceSpec,
    Meta,
    Pagination,
    PaginationMeta,
    PermissionSet,
)
```

# Tasks

Types:

```python
from mobilerun.types import (
    PackageCredentials,
    Task,
    TaskStatus,
    UsageResult,
    TaskRetrieveResponse,
    TaskListResponse,
    TaskGetStatusResponse,
    TaskGetTrajectoryResponse,
    TaskRunResponse,
    TaskSendMessageResponse,
    TaskStopResponse,
)
```

Methods:

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">retrieve</a>(task_id) -> <a href="./src/mobilerun/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="get /tasks">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">list</a>(\*\*<a href="src/mobilerun/types/task_list_params.py">params</a>) -> <a href="./src/mobilerun/types/task_list_response.py">TaskListResponse</a></code>
- <code title="get /tasks/{task_id}/attach">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">attach</a>(task_id) -> None</code>
- <code title="get /tasks/{task_id}/status">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">get_status</a>(task_id) -> <a href="./src/mobilerun/types/task_get_status_response.py">TaskGetStatusResponse</a></code>
- <code title="get /tasks/{task_id}/trajectory">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">get_trajectory</a>(task_id) -> <a href="./src/mobilerun/types/task_get_trajectory_response.py">TaskGetTrajectoryResponse</a></code>
- <code title="post /tasks">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">run</a>(\*\*<a href="src/mobilerun/types/task_run_params.py">params</a>) -> <a href="./src/mobilerun/types/task_run_response.py">TaskRunResponse</a></code>
- <code title="post /tasks/stream">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">run_streamed</a>(\*\*<a href="src/mobilerun/types/task_run_streamed_params.py">params</a>) -> object</code>
- <code title="post /tasks/{task_id}/message">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">send_message</a>(task_id, \*\*<a href="src/mobilerun/types/task_send_message_params.py">params</a>) -> <a href="./src/mobilerun/types/task_send_message_response.py">TaskSendMessageResponse</a></code>
- <code title="post /tasks/{task_id}/cancel">client.tasks.<a href="./src/mobilerun/resources/tasks/tasks.py">stop</a>(task_id) -> <a href="./src/mobilerun/types/task_stop_response.py">TaskStopResponse</a></code>

## Screenshots

Types:

```python
from mobilerun.types.tasks import MediaResponse, ScreenshotListResponse
```

Methods:

- <code title="get /tasks/{task_id}/screenshots/{index}">client.tasks.screenshots.<a href="./src/mobilerun/resources/tasks/screenshots.py">retrieve</a>(index, \*, task_id) -> <a href="./src/mobilerun/types/tasks/media_response.py">MediaResponse</a></code>
- <code title="get /tasks/{task_id}/screenshots">client.tasks.screenshots.<a href="./src/mobilerun/resources/tasks/screenshots.py">list</a>(task_id) -> <a href="./src/mobilerun/types/tasks/screenshot_list_response.py">ScreenshotListResponse</a></code>

## UiStates

Types:

```python
from mobilerun.types.tasks import UiStateListResponse
```

Methods:

- <code title="get /tasks/{task_id}/ui_states/{index}">client.tasks.ui_states.<a href="./src/mobilerun/resources/tasks/ui_states.py">retrieve</a>(index, \*, task_id) -> <a href="./src/mobilerun/types/tasks/media_response.py">MediaResponse</a></code>
- <code title="get /tasks/{task_id}/ui_states">client.tasks.ui_states.<a href="./src/mobilerun/resources/tasks/ui_states.py">list</a>(task_id) -> <a href="./src/mobilerun/types/tasks/ui_state_list_response.py">UiStateListResponse</a></code>

# Agents

Types:

```python
from mobilerun.types import AgentListResponse
```

Methods:

- <code title="get /agents">client.agents.<a href="./src/mobilerun/resources/agents.py">list</a>() -> <a href="./src/mobilerun/types/agent_list_response.py">AgentListResponse</a></code>

# Proxies

Types:

```python
from mobilerun.types import (
    ProxyConfig,
    ProxyCreateResponse,
    ProxyRetrieveResponse,
    ProxyUpdateResponse,
    ProxyListResponse,
    ProxyDeleteResponse,
)
```

Methods:

- <code title="post /proxies">client.proxies.<a href="./src/mobilerun/resources/proxies.py">create</a>(\*\*<a href="src/mobilerun/types/proxy_create_params.py">params</a>) -> <a href="./src/mobilerun/types/proxy_create_response.py">ProxyCreateResponse</a></code>
- <code title="get /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun/resources/proxies.py">retrieve</a>(proxy_id) -> <a href="./src/mobilerun/types/proxy_retrieve_response.py">ProxyRetrieveResponse</a></code>
- <code title="put /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun/resources/proxies.py">update</a>(proxy_id, \*\*<a href="src/mobilerun/types/proxy_update_params.py">params</a>) -> <a href="./src/mobilerun/types/proxy_update_response.py">ProxyUpdateResponse</a></code>
- <code title="get /proxies">client.proxies.<a href="./src/mobilerun/resources/proxies.py">list</a>() -> <a href="./src/mobilerun/types/proxy_list_response.py">ProxyListResponse</a></code>
- <code title="delete /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun/resources/proxies.py">delete</a>(proxy_id) -> <a href="./src/mobilerun/types/proxy_delete_response.py">ProxyDeleteResponse</a></code>

# Carriers

Types:

```python
from mobilerun.types import Carrier, CarrierListResponse, CarrierDeleteResponse
```

Methods:

- <code title="post /carriers">client.carriers.<a href="./src/mobilerun/resources/carriers.py">create</a>(\*\*<a href="src/mobilerun/types/carrier_create_params.py">params</a>) -> <a href="./src/mobilerun/types/carrier.py">Carrier</a></code>
- <code title="get /carriers/{carrierId}">client.carriers.<a href="./src/mobilerun/resources/carriers.py">retrieve</a>(carrier_id) -> <a href="./src/mobilerun/types/carrier.py">Carrier</a></code>
- <code title="patch /carriers/{carrierId}">client.carriers.<a href="./src/mobilerun/resources/carriers.py">update</a>(carrier_id, \*\*<a href="src/mobilerun/types/carrier_update_params.py">params</a>) -> <a href="./src/mobilerun/types/carrier.py">Carrier</a></code>
- <code title="get /carriers">client.carriers.<a href="./src/mobilerun/resources/carriers.py">list</a>(\*\*<a href="src/mobilerun/types/carrier_list_params.py">params</a>) -> <a href="./src/mobilerun/types/carrier_list_response.py">CarrierListResponse</a></code>
- <code title="delete /carriers/{carrierId}">client.carriers.<a href="./src/mobilerun/resources/carriers.py">delete</a>(carrier_id) -> <a href="./src/mobilerun/types/carrier_delete_response.py">CarrierDeleteResponse</a></code>
- <code title="get /carriers/lookup">client.carriers.<a href="./src/mobilerun/resources/carriers.py">lookup</a>(\*\*<a href="src/mobilerun/types/carrier_lookup_params.py">params</a>) -> <a href="./src/mobilerun/types/carrier.py">Carrier</a></code>

# Profiles

Types:

```python
from mobilerun.types import Profile, ProfileListResponse, ProfileDeleteResponse
```

Methods:

- <code title="post /profiles">client.profiles.<a href="./src/mobilerun/resources/profiles.py">create</a>(\*\*<a href="src/mobilerun/types/profile_create_params.py">params</a>) -> <a href="./src/mobilerun/types/profile.py">Profile</a></code>
- <code title="get /profiles/{profileId}">client.profiles.<a href="./src/mobilerun/resources/profiles.py">retrieve</a>(profile_id) -> <a href="./src/mobilerun/types/profile.py">Profile</a></code>
- <code title="put /profiles/{profileId}">client.profiles.<a href="./src/mobilerun/resources/profiles.py">update</a>(profile_id, \*\*<a href="src/mobilerun/types/profile_update_params.py">params</a>) -> <a href="./src/mobilerun/types/profile.py">Profile</a></code>
- <code title="get /profiles">client.profiles.<a href="./src/mobilerun/resources/profiles.py">list</a>(\*\*<a href="src/mobilerun/types/profile_list_params.py">params</a>) -> <a href="./src/mobilerun/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /profiles/{profileId}">client.profiles.<a href="./src/mobilerun/resources/profiles.py">delete</a>(profile_id) -> <a href="./src/mobilerun/types/profile_delete_response.py">ProfileDeleteResponse</a></code>

# Devices

Types:

```python
from mobilerun.types import Device, DeviceListResponse, DeviceCountResponse
```

Methods:

- <code title="post /devices">client.devices.<a href="./src/mobilerun/resources/devices/devices.py">create</a>(\*\*<a href="src/mobilerun/types/device_create_params.py">params</a>) -> <a href="./src/mobilerun/types/device.py">Device</a></code>
- <code title="get /devices/{deviceId}">client.devices.<a href="./src/mobilerun/resources/devices/devices.py">retrieve</a>(device_id) -> <a href="./src/mobilerun/types/device.py">Device</a></code>
- <code title="get /devices">client.devices.<a href="./src/mobilerun/resources/devices/devices.py">list</a>(\*\*<a href="src/mobilerun/types/device_list_params.py">params</a>) -> <a href="./src/mobilerun/types/device_list_response.py">DeviceListResponse</a></code>
- <code title="get /devices/count">client.devices.<a href="./src/mobilerun/resources/devices/devices.py">count</a>() -> <a href="./src/mobilerun/types/device_count_response.py">DeviceCountResponse</a></code>
- <code title="delete /devices/{deviceId}">client.devices.<a href="./src/mobilerun/resources/devices/devices.py">terminate</a>(device_id, \*\*<a href="src/mobilerun/types/device_terminate_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/wait">client.devices.<a href="./src/mobilerun/resources/devices/devices.py">wait_ready</a>(device_id) -> <a href="./src/mobilerun/types/device.py">Device</a></code>

## Time

Types:

```python
from mobilerun.types.devices import TimeTimeResponse, TimeTimezoneResponse
```

Methods:

- <code title="post /devices/{deviceId}/time">client.devices.time.<a href="./src/mobilerun/resources/devices/time.py">set_time</a>(device_id, \*\*<a href="src/mobilerun/types/devices/time_set_time_params.py">params</a>) -> None</code>
- <code title="post /devices/{deviceId}/timezone">client.devices.time.<a href="./src/mobilerun/resources/devices/time.py">set_timezone</a>(device_id, \*\*<a href="src/mobilerun/types/devices/time_set_timezone_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/time">client.devices.time.<a href="./src/mobilerun/resources/devices/time.py">time</a>(device_id) -> str</code>
- <code title="get /devices/{deviceId}/timezone">client.devices.time.<a href="./src/mobilerun/resources/devices/time.py">timezone</a>(device_id) -> <a href="./src/mobilerun/types/devices/time_timezone_response.py">TimeTimezoneResponse</a></code>

## Profile

Methods:

- <code title="put /devices/{deviceId}/profile">client.devices.profile.<a href="./src/mobilerun/resources/devices/profile.py">update</a>(device_id, \*\*<a href="src/mobilerun/types/devices/profile_update_params.py">params</a>) -> None</code>

## Files

Types:

```python
from mobilerun.types.devices import FileInfo, FileListResponse, FileDownloadResponse
```

Methods:

- <code title="get /devices/{deviceId}/files">client.devices.files.<a href="./src/mobilerun/resources/devices/files.py">list</a>(device_id, \*\*<a href="src/mobilerun/types/devices/file_list_params.py">params</a>) -> <a href="./src/mobilerun/types/devices/file_list_response.py">FileListResponse</a></code>
- <code title="delete /devices/{deviceId}/files">client.devices.files.<a href="./src/mobilerun/resources/devices/files.py">delete</a>(device_id, \*\*<a href="src/mobilerun/types/devices/file_delete_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/files/download">client.devices.files.<a href="./src/mobilerun/resources/devices/files.py">download</a>(device_id, \*\*<a href="src/mobilerun/types/devices/file_download_params.py">params</a>) -> str</code>
- <code title="post /devices/{deviceId}/files">client.devices.files.<a href="./src/mobilerun/resources/devices/files.py">upload</a>(device_id, \*\*<a href="src/mobilerun/types/devices/file_upload_params.py">params</a>) -> None</code>

## Proxy

Methods:

- <code title="post /devices/{deviceId}/proxy">client.devices.proxy.<a href="./src/mobilerun/resources/devices/proxy.py">connect</a>(device_id, \*\*<a href="src/mobilerun/types/devices/proxy_connect_params.py">params</a>) -> None</code>
- <code title="delete /devices/{deviceId}/proxy">client.devices.proxy.<a href="./src/mobilerun/resources/devices/proxy.py">disconnect</a>(device_id) -> None</code>

## Location

Types:

```python
from mobilerun.types.devices import LocationGetResponse
```

Methods:

- <code title="get /devices/{deviceId}/location">client.devices.location.<a href="./src/mobilerun/resources/devices/location.py">get</a>(device_id) -> <a href="./src/mobilerun/types/devices/location_get_response.py">LocationGetResponse</a></code>
- <code title="post /devices/{deviceId}/location">client.devices.location.<a href="./src/mobilerun/resources/devices/location.py">set</a>(device_id, \*\*<a href="src/mobilerun/types/devices/location_set_params.py">params</a>) -> None</code>

## Actions

Types:

```python
from mobilerun.types.devices import ActionOverlayVisibleResponse
```

Methods:

- <code title="post /devices/{deviceId}/global">client.devices.actions.<a href="./src/mobilerun/resources/devices/actions.py">global\_</a>(device_id, \*\*<a href="src/mobilerun/types/devices/action_global_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/overlay">client.devices.actions.<a href="./src/mobilerun/resources/devices/actions.py">overlay_visible</a>(device_id) -> <a href="./src/mobilerun/types/devices/action_overlay_visible_response.py">ActionOverlayVisibleResponse</a></code>
- <code title="post /devices/{deviceId}/overlay">client.devices.actions.<a href="./src/mobilerun/resources/devices/actions.py">set_overlay_visible</a>(device_id, \*\*<a href="src/mobilerun/types/devices/action_set_overlay_visible_params.py">params</a>) -> None</code>
- <code title="post /devices/{deviceId}/swipe">client.devices.actions.<a href="./src/mobilerun/resources/devices/actions.py">swipe</a>(device_id, \*\*<a href="src/mobilerun/types/devices/action_swipe_params.py">params</a>) -> None</code>
- <code title="post /devices/{deviceId}/tap">client.devices.actions.<a href="./src/mobilerun/resources/devices/actions.py">tap</a>(device_id, \*\*<a href="src/mobilerun/types/devices/action_tap_params.py">params</a>) -> None</code>

## State

Types:

```python
from mobilerun.types.devices import Rect, StateScreenshotResponse, StateUiResponse
```

Methods:

- <code title="get /devices/{deviceId}/screenshot">client.devices.state.<a href="./src/mobilerun/resources/devices/state.py">screenshot</a>(device_id, \*\*<a href="src/mobilerun/types/devices/state_screenshot_params.py">params</a>) -> str</code>
- <code title="get /devices/{deviceId}/ui-state">client.devices.state.<a href="./src/mobilerun/resources/devices/state.py">ui</a>(device_id, \*\*<a href="src/mobilerun/types/devices/state_ui_params.py">params</a>) -> <a href="./src/mobilerun/types/devices/state_ui_response.py">StateUiResponse</a></code>

## Apps

Types:

```python
from mobilerun.types.devices import AppListResponse
```

Methods:

- <code title="patch /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun/resources/devices/apps.py">update</a>(package_name, \*, device_id) -> None</code>
- <code title="get /devices/{deviceId}/apps">client.devices.apps.<a href="./src/mobilerun/resources/devices/apps.py">list</a>(device_id, \*\*<a href="src/mobilerun/types/devices/app_list_params.py">params</a>) -> <a href="./src/mobilerun/types/devices/app_list_response.py">Optional[AppListResponse]</a></code>
- <code title="delete /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun/resources/devices/apps.py">delete</a>(package_name, \*, device_id) -> None</code>
- <code title="post /devices/{deviceId}/apps">client.devices.apps.<a href="./src/mobilerun/resources/devices/apps.py">install</a>(device_id, \*\*<a href="src/mobilerun/types/devices/app_install_params.py">params</a>) -> None</code>
- <code title="put /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun/resources/devices/apps.py">start</a>(package_name, \*, device_id, \*\*<a href="src/mobilerun/types/devices/app_start_params.py">params</a>) -> None</code>

## Packages

Types:

```python
from mobilerun.types.devices import PackageListResponse
```

Methods:

- <code title="get /devices/{deviceId}/packages">client.devices.packages.<a href="./src/mobilerun/resources/devices/packages.py">list</a>(device_id, \*\*<a href="src/mobilerun/types/devices/package_list_params.py">params</a>) -> <a href="./src/mobilerun/types/devices/package_list_response.py">Optional[PackageListResponse]</a></code>

## Keyboard

Methods:

- <code title="delete /devices/{deviceId}/keyboard">client.devices.keyboard.<a href="./src/mobilerun/resources/devices/keyboard.py">clear</a>(device_id) -> None</code>
- <code title="put /devices/{deviceId}/keyboard">client.devices.keyboard.<a href="./src/mobilerun/resources/devices/keyboard.py">key</a>(device_id, \*\*<a href="src/mobilerun/types/devices/keyboard_key_params.py">params</a>) -> None</code>
- <code title="post /devices/{deviceId}/keyboard">client.devices.keyboard.<a href="./src/mobilerun/resources/devices/keyboard.py">write</a>(device_id, \*\*<a href="src/mobilerun/types/devices/keyboard_write_params.py">params</a>) -> None</code>

## Tasks

Types:

```python
from mobilerun.types.devices import TaskListResponse
```

Methods:

- <code title="get /devices/{deviceId}/tasks">client.devices.tasks.<a href="./src/mobilerun/resources/devices/tasks.py">list</a>(device_id, \*\*<a href="src/mobilerun/types/devices/task_list_params.py">params</a>) -> <a href="./src/mobilerun/types/devices/task_list_response.py">TaskListResponse</a></code>

# Apps

Types:

```python
from mobilerun.types import AppListResponse
```

Methods:

- <code title="get /apps">client.apps.<a href="./src/mobilerun/resources/apps.py">list</a>(\*\*<a href="src/mobilerun/types/app_list_params.py">params</a>) -> <a href="./src/mobilerun/types/app_list_response.py">AppListResponse</a></code>

# Credentials

Types:

```python
from mobilerun.types import CredentialListResponse
```

Methods:

- <code title="get /credentials">client.credentials.<a href="./src/mobilerun/resources/credentials/credentials.py">list</a>(\*\*<a href="src/mobilerun/types/credential_list_params.py">params</a>) -> <a href="./src/mobilerun/types/credential_list_response.py">CredentialListResponse</a></code>

## Packages

Types:

```python
from mobilerun.types.credentials import PackageCreateResponse, PackageListResponse
```

Methods:

- <code title="post /credentials/packages">client.credentials.packages.<a href="./src/mobilerun/resources/credentials/packages/packages.py">create</a>(\*\*<a href="src/mobilerun/types/credentials/package_create_params.py">params</a>) -> <a href="./src/mobilerun/types/credentials/package_create_response.py">PackageCreateResponse</a></code>
- <code title="get /credentials/packages/{packageName}">client.credentials.packages.<a href="./src/mobilerun/resources/credentials/packages/packages.py">list</a>(package_name) -> <a href="./src/mobilerun/types/credentials/package_list_response.py">PackageListResponse</a></code>

### Credentials

Types:

```python
from mobilerun.types.credentials.packages import (
    Credential,
    CredentialCreateResponse,
    CredentialRetrieveResponse,
    CredentialDeleteResponse,
)
```

Methods:

- <code title="post /credentials/packages/{packageName}">client.credentials.packages.credentials.<a href="./src/mobilerun/resources/credentials/packages/credentials/credentials.py">create</a>(package_name, \*\*<a href="src/mobilerun/types/credentials/packages/credential_create_params.py">params</a>) -> <a href="./src/mobilerun/types/credentials/packages/credential_create_response.py">CredentialCreateResponse</a></code>
- <code title="get /credentials/packages/{packageName}/credentials/{credentialName}">client.credentials.packages.credentials.<a href="./src/mobilerun/resources/credentials/packages/credentials/credentials.py">retrieve</a>(credential_name, \*, package_name) -> <a href="./src/mobilerun/types/credentials/packages/credential_retrieve_response.py">CredentialRetrieveResponse</a></code>
- <code title="delete /credentials/packages/{packageName}/credentials/{credentialName}">client.credentials.packages.credentials.<a href="./src/mobilerun/resources/credentials/packages/credentials/credentials.py">delete</a>(credential_name, \*, package_name) -> <a href="./src/mobilerun/types/credentials/packages/credential_delete_response.py">CredentialDeleteResponse</a></code>

#### Fields

Types:

```python
from mobilerun.types.credentials.packages.credentials import (
    FieldCreateResponse,
    FieldUpdateResponse,
    FieldDeleteResponse,
)
```

Methods:

- <code title="post /credentials/packages/{packageName}/credentials/{credentialName}/fields">client.credentials.packages.credentials.fields.<a href="./src/mobilerun/resources/credentials/packages/credentials/fields.py">create</a>(credential_name, \*, package_name, \*\*<a href="src/mobilerun/types/credentials/packages/credentials/field_create_params.py">params</a>) -> <a href="./src/mobilerun/types/credentials/packages/credentials/field_create_response.py">FieldCreateResponse</a></code>
- <code title="patch /credentials/packages/{packageName}/credentials/{credentialName}/fields/{fieldType}">client.credentials.packages.credentials.fields.<a href="./src/mobilerun/resources/credentials/packages/credentials/fields.py">update</a>(field_type, \*, package_name, credential_name, \*\*<a href="src/mobilerun/types/credentials/packages/credentials/field_update_params.py">params</a>) -> <a href="./src/mobilerun/types/credentials/packages/credentials/field_update_response.py">FieldUpdateResponse</a></code>
- <code title="delete /credentials/packages/{packageName}/credentials/{credentialName}/fields/{fieldType}">client.credentials.packages.credentials.fields.<a href="./src/mobilerun/resources/credentials/packages/credentials/fields.py">delete</a>(field_type, \*, package_name, credential_name) -> <a href="./src/mobilerun/types/credentials/packages/credentials/field_delete_response.py">FieldDeleteResponse</a></code>

# Hooks

Types:

```python
from mobilerun.types import (
    HookRetrieveResponse,
    HookUpdateResponse,
    HookListResponse,
    HookGetSampleDataResponse,
    HookPerformResponse,
    HookSubscribeResponse,
    HookUnsubscribeResponse,
)
```

Methods:

- <code title="get /hooks/{hook_id}">client.hooks.<a href="./src/mobilerun/resources/hooks.py">retrieve</a>(hook_id) -> <a href="./src/mobilerun/types/hook_retrieve_response.py">HookRetrieveResponse</a></code>
- <code title="post /hooks/{hook_id}/edit">client.hooks.<a href="./src/mobilerun/resources/hooks.py">update</a>(hook_id, \*\*<a href="src/mobilerun/types/hook_update_params.py">params</a>) -> <a href="./src/mobilerun/types/hook_update_response.py">HookUpdateResponse</a></code>
- <code title="get /hooks">client.hooks.<a href="./src/mobilerun/resources/hooks.py">list</a>(\*\*<a href="src/mobilerun/types/hook_list_params.py">params</a>) -> <a href="./src/mobilerun/types/hook_list_response.py">HookListResponse</a></code>
- <code title="get /hooks/sample">client.hooks.<a href="./src/mobilerun/resources/hooks.py">get_sample_data</a>() -> <a href="./src/mobilerun/types/hook_get_sample_data_response.py">HookGetSampleDataResponse</a></code>
- <code title="post /hooks/perform">client.hooks.<a href="./src/mobilerun/resources/hooks.py">perform</a>(\*\*<a href="src/mobilerun/types/hook_perform_params.py">params</a>) -> <a href="./src/mobilerun/types/hook_perform_response.py">HookPerformResponse</a></code>
- <code title="post /hooks/subscribe">client.hooks.<a href="./src/mobilerun/resources/hooks.py">subscribe</a>(\*\*<a href="src/mobilerun/types/hook_subscribe_params.py">params</a>) -> <a href="./src/mobilerun/types/hook_subscribe_response.py">HookSubscribeResponse</a></code>
- <code title="post /hooks/{hook_id}/unsubscribe">client.hooks.<a href="./src/mobilerun/resources/hooks.py">unsubscribe</a>(hook_id) -> <a href="./src/mobilerun/types/hook_unsubscribe_response.py">HookUnsubscribeResponse</a></code>

# Models

Types:

```python
from mobilerun.types import ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/mobilerun/resources/models.py">list</a>() -> <a href="./src/mobilerun/types/model_list_response.py">ModelListResponse</a></code>
