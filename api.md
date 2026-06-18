# Shared Types

```python
from mobilerun_sdk.types import (
    DeviceCarrier,
    DeviceIdentifiers,
    DeviceSpec,
    Location,
    Meta,
    Pagination,
    PaginationMeta,
    PermissionSet,
    Socks5,
)
```

# Apps

Types:

```python
from mobilerun_sdk.types import (
    AppRetrieveResponse,
    AppListResponse,
    AppDeleteResponse,
    AppConfirmUploadResponse,
    AppCreateSignedUploadURLResponse,
    AppListVersionsResponse,
    AppMarkFailedResponse,
)
```

Methods:

- <code title="get /apps/{id}">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">retrieve</a>(id) -> <a href="./src/mobilerun_sdk/types/app_retrieve_response.py">AppRetrieveResponse</a></code>
- <code title="get /apps">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/app_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/app_list_response.py">AppListResponse</a></code>
- <code title="delete /apps/{id}">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">delete</a>(id) -> <a href="./src/mobilerun_sdk/types/app_delete_response.py">AppDeleteResponse</a></code>
- <code title="post /apps/{id}/confirm-upload">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">confirm_upload</a>(id) -> <a href="./src/mobilerun_sdk/types/app_confirm_upload_response.py">AppConfirmUploadResponse</a></code>
- <code title="post /apps/create-signed-upload-url">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">create_signed_upload_url</a>(\*\*<a href="src/mobilerun_sdk/types/app_create_signed_upload_url_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/app_create_signed_upload_url_response.py">AppCreateSignedUploadURLResponse</a></code>
- <code title="get /apps/{id}/versions">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">list_versions</a>(id) -> <a href="./src/mobilerun_sdk/types/app_list_versions_response.py">AppListVersionsResponse</a></code>
- <code title="post /apps/{id}/mark-failed">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">mark_failed</a>(id) -> <a href="./src/mobilerun_sdk/types/app_mark_failed_response.py">AppMarkFailedResponse</a></code>

# Carriers

Types:

```python
from mobilerun_sdk.types import (
    CarrierCreateResponse,
    CarrierRetrieveResponse,
    CarrierUpdateResponse,
    CarrierListResponse,
    CarrierDeleteResponse,
    CarrierLookupResponse,
)
```

Methods:

- <code title="post /carriers">client.carriers.<a href="./src/mobilerun_sdk/resources/carriers.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/carrier_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/carrier_create_response.py">CarrierCreateResponse</a></code>
- <code title="get /carriers/{carrierId}">client.carriers.<a href="./src/mobilerun_sdk/resources/carriers.py">retrieve</a>(carrier_id) -> <a href="./src/mobilerun_sdk/types/carrier_retrieve_response.py">CarrierRetrieveResponse</a></code>
- <code title="patch /carriers/{carrierId}">client.carriers.<a href="./src/mobilerun_sdk/resources/carriers.py">update</a>(carrier_id, \*\*<a href="src/mobilerun_sdk/types/carrier_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/carrier_update_response.py">CarrierUpdateResponse</a></code>
- <code title="get /carriers">client.carriers.<a href="./src/mobilerun_sdk/resources/carriers.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/carrier_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/carrier_list_response.py">CarrierListResponse</a></code>
- <code title="delete /carriers/{carrierId}">client.carriers.<a href="./src/mobilerun_sdk/resources/carriers.py">delete</a>(carrier_id) -> <a href="./src/mobilerun_sdk/types/carrier_delete_response.py">CarrierDeleteResponse</a></code>
- <code title="get /carriers/lookup">client.carriers.<a href="./src/mobilerun_sdk/resources/carriers.py">lookup</a>(\*\*<a href="src/mobilerun_sdk/types/carrier_lookup_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/carrier_lookup_response.py">CarrierLookupResponse</a></code>

# Credentials

Types:

```python
from mobilerun_sdk.types import CredentialListResponse
```

Methods:

- <code title="get /credentials">client.credentials.<a href="./src/mobilerun_sdk/resources/credentials/credentials.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/credential_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credential_list_response.py">CredentialListResponse</a></code>

## Packages

Types:

```python
from mobilerun_sdk.types.credentials import PackageCreateResponse, PackageListResponse
```

Methods:

- <code title="post /credentials/packages">client.credentials.packages.<a href="./src/mobilerun_sdk/resources/credentials/packages/packages.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/credentials/package_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credentials/package_create_response.py">PackageCreateResponse</a></code>
- <code title="get /credentials/packages/{packageName}">client.credentials.packages.<a href="./src/mobilerun_sdk/resources/credentials/packages/packages.py">list</a>(package_name) -> <a href="./src/mobilerun_sdk/types/credentials/package_list_response.py">PackageListResponse</a></code>

### Credentials

Types:

```python
from mobilerun_sdk.types.credentials.packages import (
    Credential,
    CredentialCreateResponse,
    CredentialRetrieveResponse,
    CredentialDeleteResponse,
)
```

Methods:

- <code title="post /credentials/packages/{packageName}">client.credentials.packages.credentials.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/credentials.py">create</a>(package_name, \*\*<a href="src/mobilerun_sdk/types/credentials/packages/credential_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credential_create_response.py">CredentialCreateResponse</a></code>
- <code title="get /credentials/packages/{packageName}/credentials/{credentialName}">client.credentials.packages.credentials.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/credentials.py">retrieve</a>(credential_name, \*, package_name) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credential_retrieve_response.py">CredentialRetrieveResponse</a></code>
- <code title="delete /credentials/packages/{packageName}/credentials/{credentialName}">client.credentials.packages.credentials.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/credentials.py">delete</a>(credential_name, \*, package_name) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credential_delete_response.py">CredentialDeleteResponse</a></code>

#### Fields

Types:

```python
from mobilerun_sdk.types.credentials.packages.credentials import (
    FieldCreateResponse,
    FieldUpdateResponse,
    FieldDeleteResponse,
)
```

Methods:

- <code title="post /credentials/packages/{packageName}/credentials/{credentialName}/fields">client.credentials.packages.credentials.fields.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/fields.py">create</a>(credential_name, \*, package_name, \*\*<a href="src/mobilerun_sdk/types/credentials/packages/credentials/field_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credentials/field_create_response.py">FieldCreateResponse</a></code>
- <code title="patch /credentials/packages/{packageName}/credentials/{credentialName}/fields/{fieldType}">client.credentials.packages.credentials.fields.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/fields.py">update</a>(field_type, \*, package_name, credential_name, \*\*<a href="src/mobilerun_sdk/types/credentials/packages/credentials/field_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credentials/field_update_response.py">FieldUpdateResponse</a></code>
- <code title="delete /credentials/packages/{packageName}/credentials/{credentialName}/fields/{fieldType}">client.credentials.packages.credentials.fields.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/fields.py">delete</a>(field_type, \*, package_name, credential_name) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credentials/field_delete_response.py">FieldDeleteResponse</a></code>

# Devices

Types:

```python
from mobilerun_sdk.types import (
    Device,
    DeviceListResponse,
    DeviceCountResponse,
    DeviceFingerprintResponse,
)
```

Methods:

- <code title="post /devices">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/device_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/device.py">Device</a></code>
- <code title="get /devices/{deviceId}">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">retrieve</a>(device_id) -> <a href="./src/mobilerun_sdk/types/device.py">Device</a></code>
- <code title="get /devices">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/device_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/device_list_response.py">DeviceListResponse</a></code>
- <code title="get /devices/count">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">count</a>() -> <a href="./src/mobilerun_sdk/types/device_count_response.py">DeviceCountResponse</a></code>
- <code title="get /devices/{deviceId}/fingerprint">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">fingerprint</a>(device_id) -> <a href="./src/mobilerun_sdk/types/device_fingerprint_response.py">DeviceFingerprintResponse</a></code>
- <code title="post /devices/{deviceId}/reboot">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">reboot</a>(device_id) -> None</code>
- <code title="post /devices/{deviceId}/reset">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">reset</a>(device_id) -> None</code>
- <code title="put /devices/{deviceId}/name">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">set_name</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/device_set_name_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/device.py">Device</a></code>
- <code title="delete /devices/{deviceId}">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">terminate</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/device_terminate_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/wait">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">wait_ready</a>(device_id) -> <a href="./src/mobilerun_sdk/types/device.py">Device</a></code>

## Actions

Types:

```python
from mobilerun_sdk.types.devices import ActionOverlayVisibleResponse
```

Methods:

- <code title="post /devices/{deviceId}/global">client.devices.actions.<a href="./src/mobilerun_sdk/resources/devices/actions.py">global\_</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/action_global_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/overlay">client.devices.actions.<a href="./src/mobilerun_sdk/resources/devices/actions.py">overlay_visible</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/action_overlay_visible_response.py">ActionOverlayVisibleResponse</a></code>
- <code title="post /devices/{deviceId}/overlay">client.devices.actions.<a href="./src/mobilerun_sdk/resources/devices/actions.py">set_overlay_visible</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/action_set_overlay_visible_params.py">params</a>) -> None</code>
- <code title="post /devices/{deviceId}/swipe">client.devices.actions.<a href="./src/mobilerun_sdk/resources/devices/actions.py">swipe</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/action_swipe_params.py">params</a>) -> None</code>
- <code title="post /devices/{deviceId}/tap">client.devices.actions.<a href="./src/mobilerun_sdk/resources/devices/actions.py">tap</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/action_tap_params.py">params</a>) -> None</code>

## Apps

Types:

```python
from mobilerun_sdk.types.devices import AppListResponse
```

Methods:

- <code title="get /devices/{deviceId}/apps">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">list</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/app_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/app_list_response.py">Optional[AppListResponse]</a></code>
- <code title="delete /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">delete</a>(package_name, \*, device_id) -> None</code>
- <code title="post /devices/{deviceId}/apps">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">install</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/app_install_params.py">params</a>) -> None</code>
- <code title="put /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">start</a>(package_name, \*, device_id, \*\*<a href="src/mobilerun_sdk/types/devices/app_start_params.py">params</a>) -> None</code>
- <code title="patch /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">stop</a>(package_name, \*, device_id) -> None</code>

## Esim

Types:

```python
from mobilerun_sdk.types.devices import EsimListResponse, EsimActivateResponse
```

Methods:

- <code title="get /devices/{deviceId}/esim">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim.py">list</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/esim_list_response.py">Optional[EsimListResponse]</a></code>
- <code title="post /devices/{deviceId}/esim">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim.py">activate</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim_activate_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/esim_activate_response.py">EsimActivateResponse</a></code>
- <code title="put /devices/{deviceId}/esim">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim.py">enable</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim_enable_params.py">params</a>) -> None</code>
- <code title="delete /devices/{deviceId}/esim">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim.py">remove</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim_remove_params.py">params</a>) -> None</code>

## Files

Types:

```python
from mobilerun_sdk.types.devices import FileInfo, FileListResponse, FileDownloadResponse
```

Methods:

- <code title="get /devices/{deviceId}/files">client.devices.files.<a href="./src/mobilerun_sdk/resources/devices/files.py">list</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/file_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/file_list_response.py">FileListResponse</a></code>
- <code title="delete /devices/{deviceId}/files">client.devices.files.<a href="./src/mobilerun_sdk/resources/devices/files.py">delete</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/file_delete_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/files/download">client.devices.files.<a href="./src/mobilerun_sdk/resources/devices/files.py">download</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/file_download_params.py">params</a>) -> str</code>
- <code title="post /devices/{deviceId}/files">client.devices.files.<a href="./src/mobilerun_sdk/resources/devices/files.py">upload</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/file_upload_params.py">params</a>) -> None</code>

## Keyboard

Methods:

- <code title="delete /devices/{deviceId}/keyboard">client.devices.keyboard.<a href="./src/mobilerun_sdk/resources/devices/keyboard.py">clear</a>(device_id) -> None</code>
- <code title="put /devices/{deviceId}/keyboard">client.devices.keyboard.<a href="./src/mobilerun_sdk/resources/devices/keyboard.py">key</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/keyboard_key_params.py">params</a>) -> None</code>
- <code title="post /devices/{deviceId}/keyboard">client.devices.keyboard.<a href="./src/mobilerun_sdk/resources/devices/keyboard.py">write</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/keyboard_write_params.py">params</a>) -> None</code>

## Location

Methods:

- <code title="get /devices/{deviceId}/location">client.devices.location.<a href="./src/mobilerun_sdk/resources/devices/location.py">get</a>(device_id) -> <a href="./src/mobilerun_sdk/types/shared/location.py">Location</a></code>
- <code title="post /devices/{deviceId}/location">client.devices.location.<a href="./src/mobilerun_sdk/resources/devices/location.py">set</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/location_set_params.py">params</a>) -> None</code>

## Packages

Types:

```python
from mobilerun_sdk.types.devices import PackageListResponse
```

Methods:

- <code title="get /devices/{deviceId}/packages">client.devices.packages.<a href="./src/mobilerun_sdk/resources/devices/packages.py">list</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/package_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/package_list_response.py">Optional[PackageListResponse]</a></code>

## Profile

Methods:

- <code title="put /devices/{deviceId}/profile">client.devices.profile.<a href="./src/mobilerun_sdk/resources/devices/profile.py">update</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/profile_update_params.py">params</a>) -> None</code>

## Proxy

Types:

```python
from mobilerun_sdk.types.devices import ProxyStatusResponse
```

Methods:

- <code title="post /devices/{deviceId}/proxy">client.devices.proxy.<a href="./src/mobilerun_sdk/resources/devices/proxy.py">connect</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/proxy_connect_params.py">params</a>) -> None</code>
- <code title="delete /devices/{deviceId}/proxy">client.devices.proxy.<a href="./src/mobilerun_sdk/resources/devices/proxy.py">disconnect</a>(device_id) -> None</code>
- <code title="get /devices/{deviceId}/proxy">client.devices.proxy.<a href="./src/mobilerun_sdk/resources/devices/proxy.py">status</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/proxy_status_response.py">ProxyStatusResponse</a></code>

## State

Types:

```python
from mobilerun_sdk.types.devices import (
    A11YNode,
    Rect,
    StateScreenshotResponse,
    StateTimeResponse,
    StateUiResponse,
)
```

Methods:

- <code title="get /devices/{deviceId}/screenshot">client.devices.state.<a href="./src/mobilerun_sdk/resources/devices/state.py">screenshot</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/state_screenshot_params.py">params</a>) -> str</code>
- <code title="get /devices/{deviceId}/time">client.devices.state.<a href="./src/mobilerun_sdk/resources/devices/state.py">time</a>(device_id) -> str</code>
- <code title="get /devices/{deviceId}/ui-state">client.devices.state.<a href="./src/mobilerun_sdk/resources/devices/state.py">ui</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/state_ui_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/state_ui_response.py">StateUiResponse</a></code>

## Tasks

Types:

```python
from mobilerun_sdk.types.devices import TaskListResponse
```

Methods:

- <code title="get /devices/{deviceId}/tasks">client.devices.tasks.<a href="./src/mobilerun_sdk/resources/devices/tasks.py">list</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/task_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/task_list_response.py">TaskListResponse</a></code>

## Timezone

Types:

```python
from mobilerun_sdk.types.devices import TimezoneGetResponse
```

Methods:

- <code title="get /devices/{deviceId}/timezone">client.devices.timezone.<a href="./src/mobilerun_sdk/resources/devices/timezone.py">get</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/timezone_get_response.py">TimezoneGetResponse</a></code>
- <code title="post /devices/{deviceId}/timezone">client.devices.timezone.<a href="./src/mobilerun_sdk/resources/devices/timezone.py">set</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/timezone_set_params.py">params</a>) -> None</code>

## Language

Types:

```python
from mobilerun_sdk.types.devices import LanguageGetResponse
```

Methods:

- <code title="get /devices/{deviceId}/language">client.devices.language.<a href="./src/mobilerun_sdk/resources/devices/language.py">get</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/language_get_response.py">LanguageGetResponse</a></code>
- <code title="post /devices/{deviceId}/language">client.devices.language.<a href="./src/mobilerun_sdk/resources/devices/language.py">set</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/language_set_params.py">params</a>) -> None</code>

# Hooks

Types:

```python
from mobilerun_sdk.types import (
    HookRetrieveResponse,
    HookUpdateResponse,
    HookListResponse,
    HookGetSampleDataResponse,
    HookPerformResponse,
    HookSubscribeResponse,
    HookTestResponse,
    HookUnsubscribeResponse,
)
```

Methods:

- <code title="get /hooks/{hook_id}">client.hooks.<a href="./src/mobilerun_sdk/resources/hooks.py">retrieve</a>(hook_id) -> <a href="./src/mobilerun_sdk/types/hook_retrieve_response.py">HookRetrieveResponse</a></code>
- <code title="post /hooks/{hook_id}/edit">client.hooks.<a href="./src/mobilerun_sdk/resources/hooks.py">update</a>(hook_id, \*\*<a href="src/mobilerun_sdk/types/hook_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/hook_update_response.py">HookUpdateResponse</a></code>
- <code title="get /hooks">client.hooks.<a href="./src/mobilerun_sdk/resources/hooks.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/hook_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/hook_list_response.py">HookListResponse</a></code>
- <code title="get /hooks/sample">client.hooks.<a href="./src/mobilerun_sdk/resources/hooks.py">get_sample_data</a>() -> <a href="./src/mobilerun_sdk/types/hook_get_sample_data_response.py">HookGetSampleDataResponse</a></code>
- <code title="post /hooks/perform">client.hooks.<a href="./src/mobilerun_sdk/resources/hooks.py">perform</a>(\*\*<a href="src/mobilerun_sdk/types/hook_perform_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/hook_perform_response.py">HookPerformResponse</a></code>
- <code title="post /hooks/subscribe">client.hooks.<a href="./src/mobilerun_sdk/resources/hooks.py">subscribe</a>(\*\*<a href="src/mobilerun_sdk/types/hook_subscribe_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/hook_subscribe_response.py">HookSubscribeResponse</a></code>
- <code title="post /hooks/{hook_id}/test">client.hooks.<a href="./src/mobilerun_sdk/resources/hooks.py">test</a>(hook_id, \*\*<a href="src/mobilerun_sdk/types/hook_test_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/hook_test_response.py">HookTestResponse</a></code>
- <code title="post /hooks/{hook_id}/unsubscribe">client.hooks.<a href="./src/mobilerun_sdk/resources/hooks.py">unsubscribe</a>(hook_id) -> <a href="./src/mobilerun_sdk/types/hook_unsubscribe_response.py">HookUnsubscribeResponse</a></code>

# Models

Types:

```python
from mobilerun_sdk.types import ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/mobilerun_sdk/resources/models.py">list</a>() -> <a href="./src/mobilerun_sdk/types/model_list_response.py">ModelListResponse</a></code>

# Profiles

Types:

```python
from mobilerun_sdk.types import Profile, ProfileListResponse, ProfileDeleteResponse
```

Methods:

- <code title="post /profiles">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/profile_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/profile.py">Profile</a></code>
- <code title="get /profiles/{profileId}">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">retrieve</a>(profile_id) -> <a href="./src/mobilerun_sdk/types/profile.py">Profile</a></code>
- <code title="put /profiles/{profileId}">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">update</a>(profile_id, \*\*<a href="src/mobilerun_sdk/types/profile_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/profile.py">Profile</a></code>
- <code title="get /profiles">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/profile_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /profiles/{profileId}">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">delete</a>(profile_id) -> <a href="./src/mobilerun_sdk/types/profile_delete_response.py">ProfileDeleteResponse</a></code>

# Proxies

Types:

```python
from mobilerun_sdk.types import (
    ProxyConfig,
    ProxyCreateResponse,
    ProxyRetrieveResponse,
    ProxyUpdateResponse,
    ProxyListResponse,
    ProxyDeleteResponse,
    ProxyLookupResponse,
)
```

Methods:

- <code title="post /proxies">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/proxy_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/proxy_create_response.py">ProxyCreateResponse</a></code>
- <code title="get /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">retrieve</a>(proxy_id) -> <a href="./src/mobilerun_sdk/types/proxy_retrieve_response.py">ProxyRetrieveResponse</a></code>
- <code title="put /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">update</a>(proxy_id, \*\*<a href="src/mobilerun_sdk/types/proxy_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/proxy_update_response.py">ProxyUpdateResponse</a></code>
- <code title="get /proxies">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/proxy_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/proxy_list_response.py">ProxyListResponse</a></code>
- <code title="delete /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">delete</a>(proxy_id) -> <a href="./src/mobilerun_sdk/types/proxy_delete_response.py">ProxyDeleteResponse</a></code>
- <code title="post /proxies/lookup">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">lookup</a>(\*\*<a href="src/mobilerun_sdk/types/proxy_lookup_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/proxy_lookup_response.py">ProxyLookupResponse</a></code>

# Connect

## Countries

Types:

```python
from mobilerun_sdk.types.connect import CountryListResponse
```

Methods:

- <code title="get /connect/countries">client.connect.countries.<a href="./src/mobilerun_sdk/resources/connect/countries.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/connect/country_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/connect/country_list_response.py">CountryListResponse</a></code>

## Proxies

Types:

```python
from mobilerun_sdk.types.connect import (
    ProxyRetrieveResponse,
    ProxyListResponse,
    ProxyBuyResponse,
    ProxyListConnectionsResponse,
    ProxyPingResponse,
)
```

Methods:

- <code title="get /connect/proxies/{id}">client.connect.proxies.<a href="./src/mobilerun_sdk/resources/connect/proxies.py">retrieve</a>(id) -> <a href="./src/mobilerun_sdk/types/connect/proxy_retrieve_response.py">ProxyRetrieveResponse</a></code>
- <code title="get /connect/proxies">client.connect.proxies.<a href="./src/mobilerun_sdk/resources/connect/proxies.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/connect/proxy_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/connect/proxy_list_response.py">ProxyListResponse</a></code>
- <code title="post /connect/proxies">client.connect.proxies.<a href="./src/mobilerun_sdk/resources/connect/proxies.py">buy</a>(\*\*<a href="src/mobilerun_sdk/types/connect/proxy_buy_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/connect/proxy_buy_response.py">ProxyBuyResponse</a></code>
- <code title="delete /connect/proxies/{id}">client.connect.proxies.<a href="./src/mobilerun_sdk/resources/connect/proxies.py">cancel</a>(id) -> None</code>
- <code title="get /connect/proxies/{id}/connections">client.connect.proxies.<a href="./src/mobilerun_sdk/resources/connect/proxies.py">list_connections</a>(id, \*\*<a href="src/mobilerun_sdk/types/connect/proxy_list_connections_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/connect/proxy_list_connections_response.py">ProxyListConnectionsResponse</a></code>
- <code title="get /connect/proxies/{id}/ping">client.connect.proxies.<a href="./src/mobilerun_sdk/resources/connect/proxies.py">ping</a>(id) -> <a href="./src/mobilerun_sdk/types/connect/proxy_ping_response.py">ProxyPingResponse</a></code>

## Users

Types:

```python
from mobilerun_sdk.types.connect import (
    UserCreateResponse,
    UserRetrieveResponse,
    UserUpdateResponse,
    UserListResponse,
    UserListConnectionsResponse,
)
```

Methods:

- <code title="post /connect/users">client.connect.users.<a href="./src/mobilerun_sdk/resources/connect/users.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/connect/user_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/connect/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /connect/users/{id}">client.connect.users.<a href="./src/mobilerun_sdk/resources/connect/users.py">retrieve</a>(id) -> <a href="./src/mobilerun_sdk/types/connect/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="patch /connect/users/{id}">client.connect.users.<a href="./src/mobilerun_sdk/resources/connect/users.py">update</a>(id, \*\*<a href="src/mobilerun_sdk/types/connect/user_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/connect/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /connect/users">client.connect.users.<a href="./src/mobilerun_sdk/resources/connect/users.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/connect/user_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/connect/user_list_response.py">UserListResponse</a></code>
- <code title="delete /connect/users/{id}">client.connect.users.<a href="./src/mobilerun_sdk/resources/connect/users.py">delete</a>(id) -> None</code>
- <code title="get /connect/users/{id}/connections">client.connect.users.<a href="./src/mobilerun_sdk/resources/connect/users.py">list_connections</a>(id, \*\*<a href="src/mobilerun_sdk/types/connect/user_list_connections_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/connect/user_list_connections_response.py">UserListConnectionsResponse</a></code>

# Tasks

Types:

```python
from mobilerun_sdk.types import (
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

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">retrieve</a>(task_id) -> <a href="./src/mobilerun_sdk/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="get /tasks">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/task_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/task_list_response.py">TaskListResponse</a></code>
- <code title="get /tasks/{task_id}/attach">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">attach</a>(task_id) -> None</code>
- <code title="get /tasks/{task_id}/status">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">get_status</a>(task_id) -> <a href="./src/mobilerun_sdk/types/task_get_status_response.py">TaskGetStatusResponse</a></code>
- <code title="get /tasks/{task_id}/trajectory">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">get_trajectory</a>(task_id) -> <a href="./src/mobilerun_sdk/types/task_get_trajectory_response.py">TaskGetTrajectoryResponse</a></code>
- <code title="post /tasks">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">run</a>(\*\*<a href="src/mobilerun_sdk/types/task_run_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/task_run_response.py">TaskRunResponse</a></code>
- <code title="post /tasks/stream">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">run_streamed</a>(\*\*<a href="src/mobilerun_sdk/types/task_run_streamed_params.py">params</a>) -> object</code>
- <code title="post /tasks/{task_id}/message">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">send_message</a>(task_id, \*\*<a href="src/mobilerun_sdk/types/task_send_message_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/task_send_message_response.py">TaskSendMessageResponse</a></code>
- <code title="post /tasks/{task_id}/cancel">client.tasks.<a href="./src/mobilerun_sdk/resources/tasks/tasks.py">stop</a>(task_id) -> <a href="./src/mobilerun_sdk/types/task_stop_response.py">TaskStopResponse</a></code>

## Screenshots

Types:

```python
from mobilerun_sdk.types.tasks import MediaResponse, ScreenshotListResponse
```

Methods:

- <code title="get /tasks/{task_id}/screenshots/{index}">client.tasks.screenshots.<a href="./src/mobilerun_sdk/resources/tasks/screenshots.py">retrieve</a>(index, \*, task_id) -> <a href="./src/mobilerun_sdk/types/tasks/media_response.py">MediaResponse</a></code>
- <code title="get /tasks/{task_id}/screenshots">client.tasks.screenshots.<a href="./src/mobilerun_sdk/resources/tasks/screenshots.py">list</a>(task_id) -> <a href="./src/mobilerun_sdk/types/tasks/screenshot_list_response.py">ScreenshotListResponse</a></code>

## UiStates

Types:

```python
from mobilerun_sdk.types.tasks import UiStateListResponse
```

Methods:

- <code title="get /tasks/{task_id}/ui_states/{index}">client.tasks.ui_states.<a href="./src/mobilerun_sdk/resources/tasks/ui_states.py">retrieve</a>(index, \*, task_id) -> <a href="./src/mobilerun_sdk/types/tasks/media_response.py">MediaResponse</a></code>
- <code title="get /tasks/{task_id}/ui_states">client.tasks.ui_states.<a href="./src/mobilerun_sdk/resources/tasks/ui_states.py">list</a>(task_id) -> <a href="./src/mobilerun_sdk/types/tasks/ui_state_list_response.py">UiStateListResponse</a></code>

# Workflows

Types:

```python
from mobilerun_sdk.types import Flow
```

## Triggers

Types:

```python
from mobilerun_sdk.types.workflows import (
    TriggerCreateResponse,
    TriggerRetrieveResponse,
    TriggerUpdateResponse,
    TriggerListResponse,
    TriggerDeleteResponse,
    TriggerFireResponse,
)
```

Methods:

- <code title="post /triggers">client.workflows.triggers.<a href="./src/mobilerun_sdk/resources/workflows/triggers.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/trigger_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/trigger_create_response.py">TriggerCreateResponse</a></code>
- <code title="get /triggers/{triggerId}">client.workflows.triggers.<a href="./src/mobilerun_sdk/resources/workflows/triggers.py">retrieve</a>(trigger_id) -> <a href="./src/mobilerun_sdk/types/workflows/trigger_retrieve_response.py">TriggerRetrieveResponse</a></code>
- <code title="patch /triggers/{triggerId}">client.workflows.triggers.<a href="./src/mobilerun_sdk/resources/workflows/triggers.py">update</a>(trigger_id, \*\*<a href="src/mobilerun_sdk/types/workflows/trigger_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/trigger_update_response.py">TriggerUpdateResponse</a></code>
- <code title="get /triggers">client.workflows.triggers.<a href="./src/mobilerun_sdk/resources/workflows/triggers.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/trigger_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/trigger_list_response.py">TriggerListResponse</a></code>
- <code title="delete /triggers/{triggerId}">client.workflows.triggers.<a href="./src/mobilerun_sdk/resources/workflows/triggers.py">delete</a>(trigger_id) -> <a href="./src/mobilerun_sdk/types/workflows/trigger_delete_response.py">TriggerDeleteResponse</a></code>
- <code title="post /triggers/{triggerId}/fire">client.workflows.triggers.<a href="./src/mobilerun_sdk/resources/workflows/triggers.py">fire</a>(trigger_id, \*\*<a href="src/mobilerun_sdk/types/workflows/trigger_fire_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/trigger_fire_response.py">TriggerFireResponse</a></code>

## ActionCatalog

Types:

```python
from mobilerun_sdk.types.workflows import (
    ActionCatalogEntry,
    ActionCatalogRetrieveResponse,
    ActionCatalogListResponse,
)
```

Methods:

- <code title="get /action-catalog/{catalogEntryId}">client.workflows.action_catalog.<a href="./src/mobilerun_sdk/resources/workflows/action_catalog.py">retrieve</a>(catalog_entry_id) -> <a href="./src/mobilerun_sdk/types/workflows/action_catalog_retrieve_response.py">ActionCatalogRetrieveResponse</a></code>
- <code title="get /action-catalog">client.workflows.action_catalog.<a href="./src/mobilerun_sdk/resources/workflows/action_catalog.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/action_catalog_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/action_catalog_list_response.py">ActionCatalogListResponse</a></code>

## Actions

Types:

```python
from mobilerun_sdk.types.workflows import (
    Action,
    ActionCreateResponse,
    ActionRetrieveResponse,
    ActionUpdateResponse,
    ActionListResponse,
    ActionDeleteResponse,
)
```

Methods:

- <code title="post /actions">client.workflows.actions.<a href="./src/mobilerun_sdk/resources/workflows/actions/actions.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/action_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/action_create_response.py">ActionCreateResponse</a></code>
- <code title="get /actions/{actionId}">client.workflows.actions.<a href="./src/mobilerun_sdk/resources/workflows/actions/actions.py">retrieve</a>(action_id) -> <a href="./src/mobilerun_sdk/types/workflows/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="patch /actions/{actionId}">client.workflows.actions.<a href="./src/mobilerun_sdk/resources/workflows/actions/actions.py">update</a>(action_id, \*\*<a href="src/mobilerun_sdk/types/workflows/action_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/action_update_response.py">ActionUpdateResponse</a></code>
- <code title="get /actions">client.workflows.actions.<a href="./src/mobilerun_sdk/resources/workflows/actions/actions.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/action_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/action_list_response.py">ActionListResponse</a></code>
- <code title="delete /actions/{actionId}">client.workflows.actions.<a href="./src/mobilerun_sdk/resources/workflows/actions/actions.py">delete</a>(action_id) -> <a href="./src/mobilerun_sdk/types/workflows/action_delete_response.py">ActionDeleteResponse</a></code>

### Services

Types:

```python
from mobilerun_sdk.types.workflows.actions import ServiceListResponse, ServiceListMethodsResponse
```

Methods:

- <code title="get /actions/services">client.workflows.actions.services.<a href="./src/mobilerun_sdk/resources/workflows/actions/services.py">list</a>() -> <a href="./src/mobilerun_sdk/types/workflows/actions/service_list_response.py">ServiceListResponse</a></code>
- <code title="get /actions/services/{service}/methods">client.workflows.actions.services.<a href="./src/mobilerun_sdk/resources/workflows/actions/services.py">list_methods</a>(service) -> <a href="./src/mobilerun_sdk/types/workflows/actions/service_list_methods_response.py">ServiceListMethodsResponse</a></code>

## Flows

Types:

```python
from mobilerun_sdk.types.workflows import (
    FlowActionOverrides,
    FlowChildActionInput,
    FlowCreateResponse,
    FlowRetrieveResponse,
    FlowUpdateResponse,
    FlowListResponse,
    FlowDeleteResponse,
    FlowCloneResponse,
    FlowUnblockResponse,
)
```

Methods:

- <code title="post /flows">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/flow_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_create_response.py">FlowCreateResponse</a></code>
- <code title="get /flows/{flowId}">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">retrieve</a>(flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flow_retrieve_response.py">FlowRetrieveResponse</a></code>
- <code title="patch /flows/{flowId}">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">update</a>(flow_id, \*\*<a href="src/mobilerun_sdk/types/workflows/flow_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_update_response.py">FlowUpdateResponse</a></code>
- <code title="get /flows">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/flow_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_list_response.py">FlowListResponse</a></code>
- <code title="delete /flows/{flowId}">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">delete</a>(flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flow_delete_response.py">FlowDeleteResponse</a></code>
- <code title="post /flows/{flowId}/clone">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">clone</a>(flow_id, \*\*<a href="src/mobilerun_sdk/types/workflows/flow_clone_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_clone_response.py">FlowCloneResponse</a></code>
- <code title="post /flows/{flowId}/unblock">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">unblock</a>(flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flow_unblock_response.py">FlowUnblockResponse</a></code>

### Actions

Types:

```python
from mobilerun_sdk.types.workflows.flows import (
    FlowAction,
    ActionListResponse,
    ActionAddResponse,
    ActionRemoveResponse,
    ActionReplaceResponse,
)
```

Methods:

- <code title="get /flows/{flowId}/actions">client.workflows.flows.actions.<a href="./src/mobilerun_sdk/resources/workflows/flows/actions.py">list</a>(flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flows/action_list_response.py">ActionListResponse</a></code>
- <code title="post /flows/{flowId}/actions">client.workflows.flows.actions.<a href="./src/mobilerun_sdk/resources/workflows/flows/actions.py">add</a>(flow_id, \*\*<a href="src/mobilerun_sdk/types/workflows/flows/action_add_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flows/action_add_response.py">ActionAddResponse</a></code>
- <code title="delete /flows/{flowId}/actions/{flowActionId}">client.workflows.flows.actions.<a href="./src/mobilerun_sdk/resources/workflows/flows/actions.py">remove</a>(flow_action_id, \*, flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flows/action_remove_response.py">ActionRemoveResponse</a></code>
- <code title="put /flows/{flowId}/actions">client.workflows.flows.actions.<a href="./src/mobilerun_sdk/resources/workflows/flows/actions.py">replace</a>(flow_id, \*\*<a href="src/mobilerun_sdk/types/workflows/flows/action_replace_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flows/action_replace_response.py">ActionReplaceResponse</a></code>

## Events

Types:

```python
from mobilerun_sdk.types.workflows import EventDryRunResponse, EventIngestResponse
```

Methods:

- <code title="post /events/dry-run">client.workflows.events.<a href="./src/mobilerun_sdk/resources/workflows/events/events.py">dry_run</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/event_dry_run_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/event_dry_run_response.py">EventDryRunResponse</a></code>
- <code title="post /events/ingest">client.workflows.events.<a href="./src/mobilerun_sdk/resources/workflows/events/events.py">ingest</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/event_ingest_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/event_ingest_response.py">EventIngestResponse</a></code>

### Catalog

Types:

```python
from mobilerun_sdk.types.workflows.events import CatalogListResponse, CatalogRegisterResponse
```

Methods:

- <code title="get /events/catalog">client.workflows.events.catalog.<a href="./src/mobilerun_sdk/resources/workflows/events/catalog.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/events/catalog_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/events/catalog_list_response.py">CatalogListResponse</a></code>
- <code title="post /events/catalog/register">client.workflows.events.catalog.<a href="./src/mobilerun_sdk/resources/workflows/events/catalog.py">register</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/events/catalog_register_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/events/catalog_register_response.py">CatalogRegisterResponse</a></code>

## Executions

Types:

```python
from mobilerun_sdk.types.workflows import (
    FlowExecution,
    ExecutionRetrieveResponse,
    ExecutionListResponse,
    ExecutionGetMetricsResponse,
)
```

Methods:

- <code title="get /executions/{executionId}">client.workflows.executions.<a href="./src/mobilerun_sdk/resources/workflows/executions.py">retrieve</a>(execution_id) -> <a href="./src/mobilerun_sdk/types/workflows/execution_retrieve_response.py">ExecutionRetrieveResponse</a></code>
- <code title="get /executions">client.workflows.executions.<a href="./src/mobilerun_sdk/resources/workflows/executions.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/execution_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/execution_list_response.py">ExecutionListResponse</a></code>
- <code title="get /executions/metrics">client.workflows.executions.<a href="./src/mobilerun_sdk/resources/workflows/executions.py">get_metrics</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/execution_get_metrics_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/execution_get_metrics_response.py">ExecutionGetMetricsResponse</a></code>

## Timezones

Types:

```python
from mobilerun_sdk.types.workflows import TimezoneListResponse
```

Methods:

- <code title="get /timezones">client.workflows.timezones.<a href="./src/mobilerun_sdk/resources/workflows/timezones.py">list</a>() -> <a href="./src/mobilerun_sdk/types/workflows/timezone_list_response.py">TimezoneListResponse</a></code>

## Secrets

Types:

```python
from mobilerun_sdk.types.workflows import (
    UserSecret,
    SecretCreateResponse,
    SecretListResponse,
    SecretDeleteResponse,
)
```

Methods:

- <code title="post /secrets">client.workflows.secrets.<a href="./src/mobilerun_sdk/resources/workflows/secrets.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/secret_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/secret_create_response.py">SecretCreateResponse</a></code>
- <code title="get /secrets">client.workflows.secrets.<a href="./src/mobilerun_sdk/resources/workflows/secrets.py">list</a>() -> <a href="./src/mobilerun_sdk/types/workflows/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /secrets/{secretId}">client.workflows.secrets.<a href="./src/mobilerun_sdk/resources/workflows/secrets.py">delete</a>(secret_id) -> <a href="./src/mobilerun_sdk/types/workflows/secret_delete_response.py">SecretDeleteResponse</a></code>
