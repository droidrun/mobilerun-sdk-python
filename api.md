# Shared Types

```python
from mobilerun_sdk.types import Pagination, PaginationMeta
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

# Models

Types:

```python
from mobilerun_sdk.types import ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/mobilerun_sdk/resources/models.py">list</a>() -> <a href="./src/mobilerun_sdk/types/model_list_response.py">ModelListResponse</a></code>

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
)
```

Methods:

- <code title="post /proxies">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">create</a>(\*\*<a href="src/mobilerun_sdk/types/proxy_create_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/proxy_create_response.py">ProxyCreateResponse</a></code>
- <code title="get /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">retrieve</a>(proxy_id) -> <a href="./src/mobilerun_sdk/types/proxy_retrieve_response.py">ProxyRetrieveResponse</a></code>
- <code title="put /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">update</a>(proxy_id, \*\*<a href="src/mobilerun_sdk/types/proxy_update_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/proxy_update_response.py">ProxyUpdateResponse</a></code>
- <code title="get /proxies">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/proxy_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/proxy_list_response.py">ProxyListResponse</a></code>
- <code title="delete /proxies/{proxyId}">client.proxies.<a href="./src/mobilerun_sdk/resources/proxies.py">delete</a>(proxy_id) -> <a href="./src/mobilerun_sdk/types/proxy_delete_response.py">ProxyDeleteResponse</a></code>

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

- <code title="post /events/dry-run">client.workflows.events.<a href="./src/mobilerun_sdk/resources/workflows/events.py">dry_run</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/event_dry_run_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/event_dry_run_response.py">EventDryRunResponse</a></code>
- <code title="post /events/ingest">client.workflows.events.<a href="./src/mobilerun_sdk/resources/workflows/events.py">ingest</a>(\*\*<a href="src/mobilerun_sdk/types/workflows/event_ingest_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/workflows/event_ingest_response.py">EventIngestResponse</a></code>

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

# Webhooks

Types:

```python
from mobilerun_sdk.types import (
    WebhookCreateResponse,
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookEventTypesResponse,
    WebhookRotateSecretResponse,
    WebhookTestDeliveryResponse,
)
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
from mobilerun_sdk.types.webhooks import (
    DeliveryListResponse,
    DeliveryListForWebhookResponse,
    DeliveryRetrieveAttemptsResponse,
    DeliveryStatsResponse,
)
```

Methods:

- <code title="get /webhooks/deliveries">client.webhooks.deliveries.<a href="./src/mobilerun_sdk/resources/webhooks/deliveries.py">list</a>(\*\*<a href="src/mobilerun_sdk/types/webhooks/delivery_list_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhooks/delivery_list_response.py">DeliveryListResponse</a></code>
- <code title="get /webhooks/{id}/deliveries">client.webhooks.deliveries.<a href="./src/mobilerun_sdk/resources/webhooks/deliveries.py">list_for_webhook</a>(id, \*\*<a href="src/mobilerun_sdk/types/webhooks/delivery_list_for_webhook_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhooks/delivery_list_for_webhook_response.py">DeliveryListForWebhookResponse</a></code>
- <code title="get /webhooks/{id}/deliveries/{deliveryId}">client.webhooks.deliveries.<a href="./src/mobilerun_sdk/resources/webhooks/deliveries.py">retrieve_attempts</a>(delivery_id, \*, id) -> <a href="./src/mobilerun_sdk/types/webhooks/delivery_retrieve_attempts_response.py">DeliveryRetrieveAttemptsResponse</a></code>
- <code title="get /webhooks/deliveries/stats">client.webhooks.deliveries.<a href="./src/mobilerun_sdk/resources/webhooks/deliveries.py">stats</a>(\*\*<a href="src/mobilerun_sdk/types/webhooks/delivery_stats_params.py">params</a>) -> <a href="./src/mobilerun_sdk/types/webhooks/delivery_stats_response.py">DeliveryStatsResponse</a></code>
