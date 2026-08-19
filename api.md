# Shared Types

```python
from mobilerun_sdk.types import DeviceCarrier, DeviceIdentifiers, DeviceSpec, Location, Meta, Pagination, PaginationMeta, PermissionSet, Socks5ProxyConfig
```

# Apps

Types:

```python
from mobilerun_sdk.types import AppRetrieveResponse, AppListResponse, AppDeleteResponse, AppConfirmUploadResponse, AppCreateSignedUploadURLResponse, AppListVersionsResponse, AppMarkFailedResponse, AppStorageUsageResponse
```

Methods:

- <code title="get /apps/{id}">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">retrieve</a>(id) -> <a href="./src/mobilerun_sdk/types/app_retrieve_response.py">AppRetrieveResponse</a></code>
- <code title="get /apps">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/app_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/app_list_response.py">AppListResponse</a></code>
- <code title="delete /apps/{id}">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">delete</a>(id) -> <a href="./src/mobilerun_sdk/types/app_delete_response.py">AppDeleteResponse</a></code>
- <code title="post /apps/{id}/confirm-upload">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">confirm_upload</a>(id) -> <a href="./src/mobilerun_sdk/types/app_confirm_upload_response.py">AppConfirmUploadResponse</a></code>
- <code title="post /apps/create-signed-upload-url">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">create_signed_upload_url</a>(\*\*<a href="src/mobilerun_sdk/types/app_create_signed_upload_url_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/app_create_signed_upload_url_response.py">AppCreateSignedUploadURLResponse</a></code>
- <code title="get /apps/{id}/versions">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">list_versions</a>(id) -> <a href="./src/mobilerun_sdk/types/app_list_versions_response.py">AppListVersionsResponse</a></code>
- <code title="post /apps/{id}/mark-failed">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">mark_failed</a>(id) -> <a href="./src/mobilerun_sdk/types/app_mark_failed_response.py">AppMarkFailedResponse</a></code>
- <code title="get /apps/storage-usage">client.apps.<a href="./src/mobilerun_sdk/resources/apps.py">storage_usage</a>() -> <a href="./src/mobilerun_sdk/types/app_storage_usage_response.py">AppStorageUsageResponse</a></code>

# Carriers

Types:

```python
from mobilerun_sdk.types import CarrierCreateResponse, CarrierRetrieveResponse, CarrierUpdateResponse, CarrierListResponse, CarrierDeleteResponse, CarrierLookupResponse
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
from mobilerun_sdk.types.credentials import PackageCreateResponse, PackageListResponse, PackageListAllResponse
```

Methods:

- <code title="post /credentials/packages">client.credentials.packages.<a href="./src/mobilerun_sdk/resources/credentials/packages/packages.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/credentials/package_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credentials/package_create_response.py">PackageCreateResponse</a></code>
- <code title="get /credentials/packages/{packageName}">client.credentials.packages.<a href="./src/mobilerun_sdk/resources/credentials/packages/packages.py">list</a>(package_name) -> <a href="./src/mobilerun_sdk/types/credentials/package_list_response.py">PackageListResponse</a></code>
- <code title="get /credentials/packages">client.credentials.packages.<a href="./src/mobilerun_sdk/resources/credentials/packages/packages.py">list_all</a>() -> <a href="./src/mobilerun_sdk/types/credentials/package_list_all_response.py">PackageListAllResponse</a></code>

### Credentials

Types:

```python
from mobilerun_sdk.types.credentials.packages import CredentialCreateResponse, CredentialRetrieveResponse, CredentialDeleteResponse
```

Methods:

- <code title="post /credentials/packages/{packageName}">client.credentials.packages.credentials.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/credentials.py">create</a>(package_name, \*\*<a href="src/mobilerun_sdk/types/credentials/packages/credential_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credential_create_response.py">CredentialCreateResponse</a></code>
- <code title="get /credentials/packages/{packageName}/credentials/{credentialName}">client.credentials.packages.credentials.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/credentials.py">retrieve</a>(credential_name, \*, package_name) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credential_retrieve_response.py">CredentialRetrieveResponse</a></code>
- <code title="delete /credentials/packages/{packageName}/credentials/{credentialName}">client.credentials.packages.credentials.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/credentials.py">delete</a>(credential_name, \*, package_name) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credential_delete_response.py">CredentialDeleteResponse</a></code>

#### Fields

Types:

```python
from mobilerun_sdk.types.credentials.packages.credentials import FieldCreateResponse, FieldUpdateResponse, FieldDeleteResponse
```

Methods:

- <code title="post /credentials/packages/{packageName}/credentials/{credentialName}/fields">client.credentials.packages.credentials.fields.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/fields.py">create</a>(credential_name, \*, package_name, \*\*<a href="src/mobilerun_sdk/types/credentials/packages/credentials/field_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credentials/field_create_response.py">FieldCreateResponse</a></code>
- <code title="patch /credentials/packages/{packageName}/credentials/{credentialName}/fields/{fieldType}">client.credentials.packages.credentials.fields.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/fields.py">update</a>(field_type, \*, package_name, credential_name, \*\*<a href="src/mobilerun_sdk/types/credentials/packages/credentials/field_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credentials/field_update_response.py">FieldUpdateResponse</a></code>
- <code title="delete /credentials/packages/{packageName}/credentials/{credentialName}/fields/{fieldType}">client.credentials.packages.credentials.fields.<a href="./src/mobilerun_sdk/resources/credentials/packages/credentials/fields.py">delete</a>(field_type, \*, package_name, credential_name) -> <a href="./src/mobilerun_sdk/types/credentials/packages/credentials/field_delete_response.py">FieldDeleteResponse</a></code>

# Devices

Types:

```python
from mobilerun_sdk.types import DeviceCreateResponse, DeviceRetrieveResponse, DeviceListResponse, DeviceCountResponse, DeviceFingerprintResponse, DeviceRetrieveCapabilitiesResponse, DeviceSetNameResponse, DeviceWaitReadyResponse
```

Methods:

- <code title="post /devices">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/device_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/device_create_response.py">DeviceCreateResponse</a></code>
- <code title="get /devices/{deviceId}">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">retrieve</a>(device_id) -> <a href="./src/mobilerun_sdk/types/device_retrieve_response.py">DeviceRetrieveResponse</a></code>
- <code title="get /devices">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/device_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/device_list_response.py">DeviceListResponse</a></code>
- <code title="get /devices/count">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">count</a>() -> <a href="./src/mobilerun_sdk/types/device_count_response.py">DeviceCountResponse</a></code>
- <code title="get /devices/{deviceId}/fingerprint">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">fingerprint</a>(device_id) -> <a href="./src/mobilerun_sdk/types/device_fingerprint_response.py">DeviceFingerprintResponse</a></code>
- <code title="post /devices/{deviceId}/reboot">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">reboot</a>(device_id) -> None</code>
- <code title="post /devices/{deviceId}/reset">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">reset</a>(device_id) -> None</code>
- <code title="post /devices/{deviceId}/resume">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">resume</a>(device_id) -> None</code>
- <code title="get /devices/{deviceId}/capabilities">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">retrieve_capabilities</a>(device_id) -> <a href="./src/mobilerun_sdk/types/device_retrieve_capabilities_response.py">DeviceRetrieveCapabilitiesResponse</a></code>
- <code title="put /devices/{deviceId}/name">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">set_name</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/device_set_name_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/device_set_name_response.py">DeviceSetNameResponse</a></code>
- <code title="post /devices/{deviceId}/stop">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">stop</a>(device_id) -> None</code>
- <code title="delete /devices/{deviceId}">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">terminate</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/device_terminate_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/wait">client.devices.<a href="./src/mobilerun_sdk/resources/devices/devices.py">wait_ready</a>(device_id) -> <a href="./src/mobilerun_sdk/types/device_wait_ready_response.py">DeviceWaitReadyResponse</a></code>

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
from mobilerun_sdk.types.devices import AppListResponse, AppListInstallsResponse
```

Methods:

- <code title="get /devices/{deviceId}/apps">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">list</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/app_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/app_list_response.py">Optional[AppListResponse]</a></code>
- <code title="delete /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">delete</a>(package_name, \*, device_id) -> None</code>
- <code title="put /devices/{deviceId}/apps/{packageName}/permissions/{permission}">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">grant_permission</a>(permission, \*, device_id, package_name) -> None</code>
- <code title="post /devices/{deviceId}/apps">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">install</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/app_install_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/apps/installs">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">list_installs</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/app_list_installs_response.py">AppListInstallsResponse</a></code>
- <code title="delete /devices/{deviceId}/apps/{packageName}/permissions/{permission}">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">revoke_permission</a>(permission, \*, device_id, package_name) -> None</code>
- <code title="put /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">start</a>(package_name, \*, device_id, \*\*<a href="src/mobilerun_sdk/types/devices/app_start_params.py">params</a>) -> None</code>
- <code title="patch /devices/{deviceId}/apps/{packageName}">client.devices.apps.<a href="./src/mobilerun_sdk/resources/devices/apps.py">stop</a>(package_name, \*, device_id, \*\*<a href="src/mobilerun_sdk/types/devices/app_stop_params.py">params</a>) -> None</code>

## Esim

Types:

```python
from mobilerun_sdk.types.devices import EsimListResponse, EsimActivateResponse, EsimStatusResponse
```

Methods:

- <code title="get /devices/{deviceId}/esim">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim/esim.py">list</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/esim_list_response.py">Optional[EsimListResponse]</a></code>
- <code title="post /devices/{deviceId}/esim">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim/esim.py">activate</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim_activate_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/esim_activate_response.py">EsimActivateResponse</a></code>
- <code title="put /devices/{deviceId}/esim">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim/esim.py">enable</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim_enable_params.py">params</a>) -> None</code>
- <code title="delete /devices/{deviceId}/esim">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim/esim.py">remove</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim_remove_params.py">params</a>) -> None</code>
- <code title="put /devices/{deviceId}/esim/roaming">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim/esim.py">set_roaming</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim_set_roaming_params.py">params</a>) -> None</code>
- <code title="get /devices/{deviceId}/esim/status">client.devices.esim.<a href="./src/mobilerun_sdk/resources/devices/esim/esim.py">status</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/esim_status_response.py">Optional[EsimStatusResponse]</a></code>

### Apn

Types:

```python
from mobilerun_sdk.types.devices.esim import ApnListResponse
```

Methods:

- <code title="get /devices/{deviceId}/esim/apn">client.devices.esim.apn.<a href="./src/mobilerun_sdk/resources/devices/esim/apn.py">list</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/esim/apn_list_response.py">Optional[ApnListResponse]</a></code>
- <code title="put /devices/{deviceId}/esim/apn">client.devices.esim.apn.<a href="./src/mobilerun_sdk/resources/devices/esim/apn.py">select</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim/apn_select_params.py">params</a>) -> None</code>
- <code title="post /devices/{deviceId}/esim/apn">client.devices.esim.apn.<a href="./src/mobilerun_sdk/resources/devices/esim/apn.py">set</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/esim/apn_set_params.py">params</a>) -> None</code>

## Files

Types:

```python
from mobilerun_sdk.types.devices import FileListResponse, FileDownloadResponse
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
- <code title="delete /devices/{deviceId}/location">client.devices.location.<a href="./src/mobilerun_sdk/resources/devices/location.py">reset</a>(device_id) -> None</code>
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
from mobilerun_sdk.types.devices import A11YNode, StateScreenshotResponse, StateTimeResponse, StateUiResponse
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

## DeepLink

Methods:

- <code title="post /devices/{deviceId}/apps/open-deep-link">client.devices.deep_link.<a href="./src/mobilerun_sdk/resources/devices/deep_link.py">execute_deep_link</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/deep_link_execute_deep_link_params.py">params</a>) -> None</code>

## Browser

Types:

```python
from mobilerun_sdk.types.devices import BrowserExecuteScriptResponse
```

Methods:

- <code title="post /devices/{deviceId}/browser/execute-script">client.devices.browser.<a href="./src/mobilerun_sdk/resources/devices/browser.py">execute_script</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/browser_execute_script_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/browser_execute_script_response.py">BrowserExecuteScriptResponse</a></code>

## Kiosk

Methods:

- <code title="delete /devices/{deviceId}/kiosk">client.devices.kiosk.<a href="./src/mobilerun_sdk/resources/devices/kiosk.py">disable</a>(device_id) -> None</code>
- <code title="put /devices/{deviceId}/kiosk">client.devices.kiosk.<a href="./src/mobilerun_sdk/resources/devices/kiosk.py">enable</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/kiosk_enable_params.py">params</a>) -> None</code>

## MediaSessions

Types:

```python
from mobilerun_sdk.types.devices import MediaSessionCreateResponse, MediaSessionActivateResponse, MediaSessionRetrieveCurrentResponse
```

Methods:

- <code title="post /devices/{deviceId}/media-sessions">client.devices.media_sessions.<a href="./src/mobilerun_sdk/resources/devices/media_sessions.py">create</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/media_session_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/media_session_create_response.py">MediaSessionCreateResponse</a></code>
- <code title="delete /devices/{deviceId}/media-sessions/{sessionId}">client.devices.media_sessions.<a href="./src/mobilerun_sdk/resources/devices/media_sessions.py">delete</a>(session_id, \*, device_id) -> None</code>
- <code title="post /devices/{deviceId}/media-sessions/{sessionId}/activate">client.devices.media_sessions.<a href="./src/mobilerun_sdk/resources/devices/media_sessions.py">activate</a>(session_id, \*, device_id) -> <a href="./src/mobilerun_sdk/types/devices/media_session_activate_response.py">MediaSessionActivateResponse</a></code>
- <code title="get /devices/{deviceId}/media-sessions/current">client.devices.media_sessions.<a href="./src/mobilerun_sdk/resources/devices/media_sessions.py">retrieve_current</a>(device_id) -> <a href="./src/mobilerun_sdk/types/devices/media_session_retrieve_current_response.py">MediaSessionRetrieveCurrentResponse</a></code>

## Recordings

Types:

```python
from mobilerun_sdk.types.devices import RecordingListResponse, RecordingStartResponse, RecordingStatusResponse, RecordingStopResponse
```

Methods:

- <code title="get /devices/{deviceId}/recordings">client.devices.recordings.<a href="./src/mobilerun_sdk/resources/devices/recordings.py">list</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/recording_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/recording_list_response.py">Optional[RecordingListResponse]</a></code>
- <code title="delete /devices/{deviceId}/recordings/{recordingId}">client.devices.recordings.<a href="./src/mobilerun_sdk/resources/devices/recordings.py">delete</a>(recording_id, \*, device_id) -> None</code>
- <code title="post /devices/{deviceId}/recordings">client.devices.recordings.<a href="./src/mobilerun_sdk/resources/devices/recordings.py">start</a>(device_id, \*\*<a href="src/mobilerun_sdk/types/devices/recording_start_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/devices/recording_start_response.py">RecordingStartResponse</a></code>
- <code title="get /devices/{deviceId}/recordings/{recordingId}">client.devices.recordings.<a href="./src/mobilerun_sdk/resources/devices/recordings.py">status</a>(recording_id, \*, device_id) -> <a href="./src/mobilerun_sdk/types/devices/recording_status_response.py">RecordingStatusResponse</a></code>
- <code title="post /devices/{deviceId}/recordings/{recordingId}">client.devices.recordings.<a href="./src/mobilerun_sdk/resources/devices/recordings.py">stop</a>(recording_id, \*, device_id) -> <a href="./src/mobilerun_sdk/types/devices/recording_stop_response.py">RecordingStopResponse</a></code>
- <code title="get /devices/{deviceId}/recordings/{recordingId}/trajectory">client.devices.recordings.<a href="./src/mobilerun_sdk/resources/devices/recordings.py">trajectory</a>(recording_id, \*, device_id) -> None</code>
- <code title="get /devices/{deviceId}/recordings/{recordingId}/video">client.devices.recordings.<a href="./src/mobilerun_sdk/resources/devices/recordings.py">video</a>(recording_id, \*, device_id) -> None</code>

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
from mobilerun_sdk.types import ProfileCreateResponse, ProfileRetrieveResponse, ProfileUpdateResponse, ProfileListResponse, ProfileDeleteResponse
```

Methods:

- <code title="post /profiles">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/profile_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/profile_create_response.py">ProfileCreateResponse</a></code>
- <code title="get /profiles/{profileId}">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">retrieve</a>(profile_id) -> <a href="./src/mobilerun_sdk/types/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="put /profiles/{profileId}">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">update</a>(profile_id, \*\*<a href="src/mobilerun_sdk/types/profile_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/profile_update_response.py">ProfileUpdateResponse</a></code>
- <code title="get /profiles">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/profile_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /profiles/{profileId}">client.profiles.<a href="./src/mobilerun_sdk/resources/profiles.py">delete</a>(profile_id) -> <a href="./src/mobilerun_sdk/types/profile_delete_response.py">ProfileDeleteResponse</a></code>

# Proxies

Types:

```python
from mobilerun_sdk.types import ProxyCreateResponse, ProxyRetrieveResponse, ProxyUpdateResponse, ProxyListResponse, ProxyDeleteResponse, ProxyLookupResponse
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
from mobilerun_sdk.types.connect import ProxyRetrieveResponse, ProxyListResponse, ProxyBuyResponse, ProxyListConnectionsResponse, ProxyPingResponse
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
from mobilerun_sdk.types.connect import UserCreateResponse, UserRetrieveResponse, UserUpdateResponse, UserListResponse, UserListConnectionsResponse
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
from mobilerun_sdk.types import TaskRetrieveResponse, TaskListResponse, TaskGetStatusResponse, TaskGetTrajectoryResponse, TaskRunResponse, TaskSendMessageResponse, TaskStopResponse
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
from mobilerun_sdk.types.tasks import ScreenshotRetrieveResponse, ScreenshotListResponse
```

Methods:

- <code title="get /tasks/{task_id}/screenshots/{index}">client.tasks.screenshots.<a href="./src/mobilerun_sdk/resources/tasks/screenshots.py">retrieve</a>(index, \*, task_id) -> <a href="./src/mobilerun_sdk/types/tasks/screenshot_retrieve_response.py">ScreenshotRetrieveResponse</a></code>
- <code title="get /tasks/{task_id}/screenshots">client.tasks.screenshots.<a href="./src/mobilerun_sdk/resources/tasks/screenshots.py">list</a>(task_id) -> <a href="./src/mobilerun_sdk/types/tasks/screenshot_list_response.py">ScreenshotListResponse</a></code>

## UiStates

Types:

```python
from mobilerun_sdk.types.tasks import UiStateRetrieveResponse, UiStateListResponse
```

Methods:

- <code title="get /tasks/{task_id}/ui_states/{index}">client.tasks.ui_states.<a href="./src/mobilerun_sdk/resources/tasks/ui_states.py">retrieve</a>(index, \*, task_id) -> <a href="./src/mobilerun_sdk/types/tasks/ui_state_retrieve_response.py">UiStateRetrieveResponse</a></code>
- <code title="get /tasks/{task_id}/ui_states">client.tasks.ui_states.<a href="./src/mobilerun_sdk/resources/tasks/ui_states.py">list</a>(task_id) -> <a href="./src/mobilerun_sdk/types/tasks/ui_state_list_response.py">UiStateListResponse</a></code>

# Workflows

## Triggers

Types:

```python
from mobilerun_sdk.types.workflows import TriggerCreateResponse, TriggerRetrieveResponse, TriggerUpdateResponse, TriggerListResponse, TriggerDeleteResponse, TriggerFireResponse
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
from mobilerun_sdk.types.workflows import ActionCatalogRetrieveResponse, ActionCatalogListResponse
```

Methods:

- <code title="get /action-catalog/{catalogEntryId}">client.workflows.action_catalog.<a href="./src/mobilerun_sdk/resources/workflows/action_catalog.py">retrieve</a>(catalog_entry_id) -> <a href="./src/mobilerun_sdk/types/workflows/action_catalog_retrieve_response.py">ActionCatalogRetrieveResponse</a></code>
- <code title="get /action-catalog">client.workflows.action_catalog.<a href="./src/mobilerun_sdk/resources/workflows/action_catalog.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/action_catalog_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/action_catalog_list_response.py">ActionCatalogListResponse</a></code>

## Actions

Types:

```python
from mobilerun_sdk.types.workflows import ActionCreateResponse, ActionRetrieveResponse, ActionUpdateResponse, ActionListResponse, ActionDeleteResponse
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
from mobilerun_sdk.types.workflows import FlowCreateResponse, FlowRetrieveResponse, FlowUpdateResponse, FlowListResponse, FlowDeleteResponse, FlowCloneResponse, FlowDryRunResponse, FlowListRepairsResponse, FlowUnblockResponse
```

Methods:

- <code title="post /flows">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/flow_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_create_response.py">FlowCreateResponse</a></code>
- <code title="get /flows/{flowId}">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">retrieve</a>(flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flow_retrieve_response.py">FlowRetrieveResponse</a></code>
- <code title="patch /flows/{flowId}">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">update</a>(flow_id, \*\*<a href="src/mobilerun_sdk/types/workflows/flow_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_update_response.py">FlowUpdateResponse</a></code>
- <code title="get /flows">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/flow_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_list_response.py">FlowListResponse</a></code>
- <code title="delete /flows/{flowId}">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">delete</a>(flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flow_delete_response.py">FlowDeleteResponse</a></code>
- <code title="post /flows/{flowId}/clone">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">clone</a>(flow_id, \*\*<a href="src/mobilerun_sdk/types/workflows/flow_clone_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_clone_response.py">FlowCloneResponse</a></code>
- <code title="post /flows/{flowId}/dry-run">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">dry_run</a>(flow_id, \*\*<a href="src/mobilerun_sdk/types/workflows/flow_dry_run_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/flow_dry_run_response.py">FlowDryRunResponse</a></code>
- <code title="get /flows/{flowId}/repairs">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">list_repairs</a>(flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flow_list_repairs_response.py">FlowListRepairsResponse</a></code>
- <code title="post /flows/{flowId}/unblock">client.workflows.flows.<a href="./src/mobilerun_sdk/resources/workflows/flows/flows.py">unblock</a>(flow_id) -> <a href="./src/mobilerun_sdk/types/workflows/flow_unblock_response.py">FlowUnblockResponse</a></code>

### Actions

Types:

```python
from mobilerun_sdk.types.workflows.flows import ActionListResponse, ActionAddResponse, ActionRemoveResponse, ActionReplaceResponse
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

- <code title="post /events/dry-run">client.workflows.events.<a href="./src/mobilerun_sdk/resources/workflows/events.py">dry_run</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/event_dry_run_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/event_dry_run_response.py">EventDryRunResponse</a></code>
- <code title="post /events/ingest">client.workflows.events.<a href="./src/mobilerun_sdk/resources/workflows/events.py">ingest</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/event_ingest_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/event_ingest_response.py">EventIngestResponse</a></code>

## Executions

Types:

```python
from mobilerun_sdk.types.workflows import ExecutionRetrieveResponse, ExecutionListResponse, ExecutionAbortResponse, ExecutionGetMetricsResponse
```

Methods:

- <code title="get /executions/{executionId}">client.workflows.executions.<a href="./src/mobilerun_sdk/resources/workflows/executions.py">retrieve</a>(execution_id) -> <a href="./src/mobilerun_sdk/types/workflows/execution_retrieve_response.py">ExecutionRetrieveResponse</a></code>
- <code title="get /executions">client.workflows.executions.<a href="./src/mobilerun_sdk/resources/workflows/executions.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/execution_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/execution_list_response.py">ExecutionListResponse</a></code>
- <code title="post /executions/{executionId}/abort">client.workflows.executions.<a href="./src/mobilerun_sdk/resources/workflows/executions.py">abort</a>(execution_id) -> <a href="./src/mobilerun_sdk/types/workflows/execution_abort_response.py">ExecutionAbortResponse</a></code>
- <code title="get /executions/metrics">client.workflows.executions.<a href="./src/mobilerun_sdk/resources/workflows/executions.py">get_metrics</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/execution_get_metrics_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/execution_get_metrics_response.py">ExecutionGetMetricsResponse</a></code>

## Timezones

Types:

```python
from mobilerun_sdk.types.workflows import TimezoneListResponse
```

Methods:

- <code title="get /timezones">client.workflows.timezones.<a href="./src/mobilerun_sdk/resources/workflows/timezones.py">list</a>() -> <a href="./src/mobilerun_sdk/types/workflows/timezone_list_response.py">TimezoneListResponse</a></code>

# Webhooks

Types:

```python
from mobilerun_sdk.types import WebhookCreateResponse, WebhookRetrieveResponse, WebhookUpdateResponse, WebhookListResponse, WebhookEventTypesResponse, WebhookRotateSecretResponse, WebhookTestDeliveryResponse
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/mobilerun_sdk/resources/webhooks/webhooks.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/webhook_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /webhooks/{id}">client.webhooks.<a href="./src/mobilerun_sdk/resources/webhooks/webhooks.py">retrieve</a>(id) -> <a href="./src/mobilerun_sdk/types/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="patch /webhooks/{id}">client.webhooks.<a href="./src/mobilerun_sdk/resources/webhooks/webhooks.py">update</a>(id, \*\*<a href="src/mobilerun_sdk/types/webhook_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/mobilerun_sdk/resources/webhooks/webhooks.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/webhook_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{id}">client.webhooks.<a href="./src/mobilerun_sdk/resources/webhooks/webhooks.py">delete</a>(id) -> None</code>
- <code title="get /event-types">client.webhooks.<a href="./src/mobilerun_sdk/resources/webhooks/webhooks.py">event_types</a>() -> <a href="./src/mobilerun_sdk/types/webhook_event_types_response.py">WebhookEventTypesResponse</a></code>
- <code title="post /webhooks/{id}/rotate-secret">client.webhooks.<a href="./src/mobilerun_sdk/resources/webhooks/webhooks.py">rotate_secret</a>(id) -> <a href="./src/mobilerun_sdk/types/webhook_rotate_secret_response.py">WebhookRotateSecretResponse</a></code>
- <code title="post /webhooks/{id}/test">client.webhooks.<a href="./src/mobilerun_sdk/resources/webhooks/webhooks.py">test_delivery</a>(id) -> <a href="./src/mobilerun_sdk/types/webhook_test_delivery_response.py">WebhookTestDeliveryResponse</a></code>

## Deliveries

Types:

```python
from mobilerun_sdk.types.webhooks import DeliveryListResponse, DeliveryListForWebhookResponse, DeliveryRetrieveAttemptsResponse, DeliveryStatsResponse
```

Methods:

- <code title="get /webhooks/deliveries">client.webhooks.deliveries.<a href="./src/mobilerun_sdk/resources/webhooks/deliveries.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/webhooks/delivery_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhooks/delivery_list_response.py">DeliveryListResponse</a></code>
- <code title="get /webhooks/{id}/deliveries">client.webhooks.deliveries.<a href="./src/mobilerun_sdk/resources/webhooks/deliveries.py">list_for_webhook</a>(id, \*\*<a href="src/mobilerun_sdk/types/webhooks/delivery_list_for_webhook_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhooks/delivery_list_for_webhook_response.py">DeliveryListForWebhookResponse</a></code>
- <code title="get /webhooks/{id}/deliveries/{deliveryId}">client.webhooks.deliveries.<a href="./src/mobilerun_sdk/resources/webhooks/deliveries.py">retrieve_attempts</a>(delivery_id, \*, id) -> <a href="./src/mobilerun_sdk/types/webhooks/delivery_retrieve_attempts_response.py">DeliveryRetrieveAttemptsResponse</a></code>
- <code title="get /webhooks/deliveries/stats">client.webhooks.deliveries.<a href="./src/mobilerun_sdk/resources/webhooks/deliveries.py">stats</a>(\*\*<a href="src/mobilerun_sdk/types/webhooks/delivery_stats_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhooks/delivery_stats_response.py">DeliveryStatsResponse</a></code>

# Agents

Types:

```python
from mobilerun_sdk.types import AgentListResponse
```

Methods:

- <code title="get /agents">client.agents.<a href="./src/mobilerun_sdk/resources/agents.py">list</a>() -> <a href="./src/mobilerun_sdk/types/agent_list_response.py">AgentListResponse</a></code>

# AppEvents

Types:

```python
from mobilerun_sdk.types import AppEventRetrieveResponse, AppEventListResponse
```

Methods:

- <code title="get /app-events/{id}">client.app_events.<a href="./src/mobilerun_sdk/resources/app_events/app_events.py">retrieve</a>(id) -> <a href="./src/mobilerun_sdk/types/app_event_retrieve_response.py">AppEventRetrieveResponse</a></code>
- <code title="get /app-events">client.app_events.<a href="./src/mobilerun_sdk/resources/app_events/app_events.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/app_event_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/app_event_list_response.py">AppEventListResponse</a></code>

## Catalog

Types:

```python
from mobilerun_sdk.types.app_events import CatalogRetrieveResponse, CatalogListResponse
```

Methods:

- <code title="get /app-events/catalog/{appEventType}">client.app_events.catalog.<a href="./src/mobilerun_sdk/resources/app_events/catalog.py">retrieve</a>(app_event_type) -> <a href="./src/mobilerun_sdk/types/app_events/catalog_retrieve_response.py">CatalogRetrieveResponse</a></code>
- <code title="get /app-events/catalog">client.app_events.catalog.<a href="./src/mobilerun_sdk/resources/app_events/catalog.py">list</a>() -> <a href="./src/mobilerun_sdk/types/app_events/catalog_list_response.py">CatalogListResponse</a></code>

# Notifications

Types:

```python
from mobilerun_sdk.types import NotificationCatalogResponse, NotificationGetPreferencesResponse, NotificationUpdatePreferencesResponse
```

Methods:

- <code title="get /notifications/catalog">client.notifications.<a href="./src/mobilerun_sdk/resources/notifications.py">catalog</a>() -> <a href="./src/mobilerun_sdk/types/notification_catalog_response.py">NotificationCatalogResponse</a></code>
- <code title="get /notifications/preferences">client.notifications.<a href="./src/mobilerun_sdk/resources/notifications.py">get_preferences</a>() -> <a href="./src/mobilerun_sdk/types/notification_get_preferences_response.py">NotificationGetPreferencesResponse</a></code>
- <code title="patch /notifications/preferences">client.notifications.<a href="./src/mobilerun_sdk/resources/notifications.py">update_preferences</a>(\*\*<a href="src/mobilerun_sdk/types/notification_update_preferences_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/notification_update_preferences_response.py">NotificationUpdatePreferencesResponse</a></code>

# Esims

Types:

```python
from mobilerun_sdk.types import EsimCreateResponse, EsimRetrieveResponse, EsimUpdateResponse, EsimListResponse, EsimCapacityResponse, EsimConfirmPaymentResponse, EsimImportResponse, EsimInstallResponse, EsimInstallStatusResponse, EsimSelectorResponse
```

Methods:

- <code title="post /numbers/esims">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/esim_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/esim_create_response.py">EsimCreateResponse</a></code>
- <code title="get /numbers/esims/{id}">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">retrieve</a>(id) -> <a href="./src/mobilerun_sdk/types/esim_retrieve_response.py">EsimRetrieveResponse</a></code>
- <code title="patch /numbers/esims/{id}">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">update</a>(id, \*\*<a href="src/mobilerun_sdk/types/esim_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/esim_update_response.py">EsimUpdateResponse</a></code>
- <code title="get /numbers/esims">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/esim_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/esim_list_response.py">EsimListResponse</a></code>
- <code title="delete /numbers/esims/{id}">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">delete</a>(id) -> None</code>
- <code title="get /numbers/esims/capacity">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">capacity</a>() -> <a href="./src/mobilerun_sdk/types/esim_capacity_response.py">EsimCapacityResponse</a></code>
- <code title="post /numbers/esims/{id}/confirm-payment">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">confirm_payment</a>(id) -> <a href="./src/mobilerun_sdk/types/esim_confirm_payment_response.py">EsimConfirmPaymentResponse</a></code>
- <code title="post /numbers/esims/import">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">import\_</a>(\*\*<a href="src/mobilerun_sdk/types/esim_import_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/esim_import_response.py">EsimImportResponse</a></code>
- <code title="post /numbers/esims/{id}/install">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">install</a>(id, \*\*<a href="src/mobilerun_sdk/types/esim_install_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/esim_install_response.py">EsimInstallResponse</a></code>
- <code title="get /numbers/esims/{id}/install-status">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">install_status</a>(id) -> <a href="./src/mobilerun_sdk/types/esim_install_status_response.py">EsimInstallStatusResponse</a></code>
- <code title="get /numbers/esims/selector">client.esims.<a href="./src/mobilerun_sdk/resources/esims/esims.py">selector</a>() -> <a href="./src/mobilerun_sdk/types/esim_selector_response.py">EsimSelectorResponse</a></code>

## Messages

Types:

```python
from mobilerun_sdk.types.esims import MessageListResponse, MessageSendResponse
```

Methods:

- <code title="get /numbers/esims/{id}/messages">client.esims.messages.<a href="./src/mobilerun_sdk/resources/esims/messages.py">list</a>(id, \*\*<a href="src/mobilerun_sdk/types/esims/message_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/esims/message_list_response.py">MessageListResponse</a></code>
- <code title="post /numbers/esims/{id}/messages">client.esims.messages.<a href="./src/mobilerun_sdk/resources/esims/messages.py">send</a>(id, \*\*<a href="src/mobilerun_sdk/types/esims/message_send_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/esims/message_send_response.py">MessageSendResponse</a></code>

# Messages

Types:

```python
from mobilerun_sdk.types import MessageListResponse
```

Methods:

- <code title="get /numbers/messages">client.messages.<a href="./src/mobilerun_sdk/resources/messages/messages.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/message_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/message_list_response.py">MessageListResponse</a></code>

## Conversations

Types:

```python
from mobilerun_sdk.types.messages import ConversationListResponse, ConversationMarkReadResponse
```

Methods:

- <code title="get /numbers/messages/conversations">client.messages.conversations.<a href="./src/mobilerun_sdk/resources/messages/conversations.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/messages/conversation_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/messages/conversation_list_response.py">ConversationListResponse</a></code>
- <code title="post /numbers/messages/conversations/read">client.messages.conversations.<a href="./src/mobilerun_sdk/resources/messages/conversations.py">mark_read</a>(\*\*<a href="src/mobilerun_sdk/types/messages/conversation_mark_read_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/messages/conversation_mark_read_response.py">ConversationMarkReadResponse</a></code>

# Numbers

Types:

```python
from mobilerun_sdk.types import NumberCreateResponse, NumberRetrieveResponse, NumberListResponse, NumberDeleteResponse, NumberCountriesResponse, NumberPurposesResponse
```

Methods:

- <code title="post /numbers/phones">client.numbers.<a href="./src/mobilerun_sdk/resources/numbers/numbers.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/number_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/number_create_response.py">NumberCreateResponse</a></code>
- <code title="get /numbers/phones/{id}">client.numbers.<a href="./src/mobilerun_sdk/resources/numbers/numbers.py">retrieve</a>(id) -> <a href="./src/mobilerun_sdk/types/number_retrieve_response.py">NumberRetrieveResponse</a></code>
- <code title="get /numbers/phones">client.numbers.<a href="./src/mobilerun_sdk/resources/numbers/numbers.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/number_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/number_list_response.py">NumberListResponse</a></code>
- <code title="delete /numbers/phones/{id}">client.numbers.<a href="./src/mobilerun_sdk/resources/numbers/numbers.py">delete</a>(id) -> <a href="./src/mobilerun_sdk/types/number_delete_response.py">NumberDeleteResponse</a></code>
- <code title="get /numbers/phones/countries">client.numbers.<a href="./src/mobilerun_sdk/resources/numbers/numbers.py">countries</a>() -> <a href="./src/mobilerun_sdk/types/number_countries_response.py">NumberCountriesResponse</a></code>
- <code title="get /numbers/phones/purposes">client.numbers.<a href="./src/mobilerun_sdk/resources/numbers/numbers.py">purposes</a>() -> <a href="./src/mobilerun_sdk/types/number_purposes_response.py">NumberPurposesResponse</a></code>

## Messages

Types:

```python
from mobilerun_sdk.types.numbers import MessageListResponse
```

Methods:

- <code title="get /numbers/phones/{id}/messages">client.numbers.messages.<a href="./src/mobilerun_sdk/resources/numbers/messages.py">list</a>(id, \*\*<a href="src/mobilerun_sdk/types/numbers/message_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/numbers/message_list_response.py">MessageListResponse</a></code>

# Store

Types:

```python
from mobilerun_sdk.types import StoreCategoriesResponse
```

Methods:

- <code title="get /store/categories">client.store.<a href="./src/mobilerun_sdk/resources/store/store.py">categories</a>() -> <a href="./src/mobilerun_sdk/types/store_categories_response.py">StoreCategoriesResponse</a></code>

## Apps

Types:

```python
from mobilerun_sdk.types.store import AppRetrieveResponse, AppListResponse, AppAddToWorkspaceResponse
```

Methods:

- <code title="get /store/apps/{appId}">client.store.apps.<a href="./src/mobilerun_sdk/resources/store/apps.py">retrieve</a>(app_id) -> <a href="./src/mobilerun_sdk/types/store/app_retrieve_response.py">AppRetrieveResponse</a></code>
- <code title="get /store/apps">client.store.apps.<a href="./src/mobilerun_sdk/resources/store/apps.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/store/app_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/store/app_list_response.py">AppListResponse</a></code>
- <code title="post /store/apps/{appId}/add">client.store.apps.<a href="./src/mobilerun_sdk/resources/store/apps.py">add_to_workspace</a>(app_id) -> <a href="./src/mobilerun_sdk/types/store/app_add_to_workspace_response.py">AppAddToWorkspaceResponse</a></code>
