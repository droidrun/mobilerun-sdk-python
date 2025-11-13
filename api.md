# Tasks

Types:

```python
from droidrun_cloud.types import (
    LlmModel,
    Task,
    TaskCreate,
    TaskStatus,
    TaskRetrieveResponse,
    TaskListResponse,
    TaskGetStatusResponse,
    TaskGetTrajectoryResponse,
    TaskRunResponse,
    TaskStopResponse,
)
```

Methods:

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">retrieve</a>(task_id) -> <a href="./src/droidrun_cloud/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="get /tasks/">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">list</a>(\*\*<a href="src/droidrun_cloud/types/task_list_params.py">params</a>) -> <a href="./src/droidrun_cloud/types/task_list_response.py">TaskListResponse</a></code>
- <code title="get /tasks/{task_id}/attach">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">attach</a>(task_id) -> None</code>
- <code title="get /tasks/{task_id}/gif">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">get_gif</a>(task_id) -> <a href="./src/droidrun_cloud/types/tasks/media_response.py">MediaResponse</a></code>
- <code title="get /tasks/{task_id}/status">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">get_status</a>(task_id) -> <a href="./src/droidrun_cloud/types/task_get_status_response.py">TaskGetStatusResponse</a></code>
- <code title="get /tasks/{task_id}/trajectory">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">get_trajectory</a>(task_id) -> <a href="./src/droidrun_cloud/types/task_get_trajectory_response.py">TaskGetTrajectoryResponse</a></code>
- <code title="post /tasks/">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">run</a>(\*\*<a href="src/droidrun_cloud/types/task_run_params.py">params</a>) -> <a href="./src/droidrun_cloud/types/task_run_response.py">TaskRunResponse</a></code>
- <code title="post /tasks/stream">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">run_streamed</a>(\*\*<a href="src/droidrun_cloud/types/task_run_streamed_params.py">params</a>) -> None</code>
- <code title="post /tasks/{task_id}/cancel">client.tasks.<a href="./src/droidrun_cloud/resources/tasks/tasks.py">stop</a>(task_id) -> <a href="./src/droidrun_cloud/types/task_stop_response.py">TaskStopResponse</a></code>

## Screenshots

Types:

```python
from droidrun_cloud.types.tasks import MediaResponse, ScreenshotListResponse
```

Methods:

- <code title="get /tasks/{task_id}/screenshots/{index}">client.tasks.screenshots.<a href="./src/droidrun_cloud/resources/tasks/screenshots.py">retrieve</a>(index, \*, task_id) -> <a href="./src/droidrun_cloud/types/tasks/media_response.py">MediaResponse</a></code>
- <code title="get /tasks/{task_id}/screenshots">client.tasks.screenshots.<a href="./src/droidrun_cloud/resources/tasks/screenshots.py">list</a>(task_id) -> <a href="./src/droidrun_cloud/types/tasks/screenshot_list_response.py">ScreenshotListResponse</a></code>

# Apps

Types:

```python
from droidrun_cloud.types import AppListResponse
```

Methods:

- <code title="get /apps">client.apps.<a href="./src/droidrun_cloud/resources/apps.py">list</a>(\*\*<a href="src/droidrun_cloud/types/app_list_params.py">params</a>) -> <a href="./src/droidrun_cloud/types/app_list_response.py">AppListResponse</a></code>

# Credentials

Types:

```python
from droidrun_cloud.types import CredentialListResponse
```

Methods:

- <code title="get /credentials">client.credentials.<a href="./src/droidrun_cloud/resources/credentials/credentials.py">list</a>() -> <a href="./src/droidrun_cloud/types/credential_list_response.py">CredentialListResponse</a></code>

## Packages

Types:

```python
from droidrun_cloud.types.credentials import PackageCreateResponse, PackageListResponse
```

Methods:

- <code title="post /credentials/packages">client.credentials.packages.<a href="./src/droidrun_cloud/resources/credentials/packages/packages.py">create</a>(\*\*<a href="src/droidrun_cloud/types/credentials/package_create_params.py">params</a>) -> <a href="./src/droidrun_cloud/types/credentials/package_create_response.py">PackageCreateResponse</a></code>
- <code title="get /credentials/packages/{packageName}">client.credentials.packages.<a href="./src/droidrun_cloud/resources/credentials/packages/packages.py">list</a>(package_name) -> <a href="./src/droidrun_cloud/types/credentials/package_list_response.py">PackageListResponse</a></code>

### Credentials

Types:

```python
from droidrun_cloud.types.credentials.packages import (
    Credential,
    CredentialCreateResponse,
    CredentialRetrieveResponse,
    CredentialDeleteResponse,
)
```

Methods:

- <code title="post /credentials/packages/{packageName}">client.credentials.packages.credentials.<a href="./src/droidrun_cloud/resources/credentials/packages/credentials/credentials.py">create</a>(package_name, \*\*<a href="src/droidrun_cloud/types/credentials/packages/credential_create_params.py">params</a>) -> <a href="./src/droidrun_cloud/types/credentials/packages/credential_create_response.py">CredentialCreateResponse</a></code>
- <code title="get /credentials/packages/{packageName}/credentials/{credentialName}">client.credentials.packages.credentials.<a href="./src/droidrun_cloud/resources/credentials/packages/credentials/credentials.py">retrieve</a>(credential_name, \*, package_name) -> <a href="./src/droidrun_cloud/types/credentials/packages/credential_retrieve_response.py">CredentialRetrieveResponse</a></code>
- <code title="delete /credentials/packages/{packageName}/credentials/{credentialName}">client.credentials.packages.credentials.<a href="./src/droidrun_cloud/resources/credentials/packages/credentials/credentials.py">delete</a>(credential_name, \*, package_name) -> <a href="./src/droidrun_cloud/types/credentials/packages/credential_delete_response.py">CredentialDeleteResponse</a></code>

#### Fields

Types:

```python
from droidrun_cloud.types.credentials.packages.credentials import (
    FieldCreateResponse,
    FieldUpdateResponse,
    FieldDeleteResponse,
)
```

Methods:

- <code title="post /credentials/packages/{packageName}/credentials/{credentialName}/fields">client.credentials.packages.credentials.fields.<a href="./src/droidrun_cloud/resources/credentials/packages/credentials/fields.py">create</a>(credential_name, \*, package_name, \*\*<a href="src/droidrun_cloud/types/credentials/packages/credentials/field_create_params.py">params</a>) -> <a href="./src/droidrun_cloud/types/credentials/packages/credentials/field_create_response.py">FieldCreateResponse</a></code>
- <code title="patch /credentials/packages/{packageName}/credentials/{credentialName}/fields/{fieldType}">client.credentials.packages.credentials.fields.<a href="./src/droidrun_cloud/resources/credentials/packages/credentials/fields.py">update</a>(field_type, \*, package_name, credential_name, \*\*<a href="src/droidrun_cloud/types/credentials/packages/credentials/field_update_params.py">params</a>) -> <a href="./src/droidrun_cloud/types/credentials/packages/credentials/field_update_response.py">FieldUpdateResponse</a></code>
- <code title="delete /credentials/packages/{packageName}/credentials/{credentialName}/fields/{fieldType}">client.credentials.packages.credentials.fields.<a href="./src/droidrun_cloud/resources/credentials/packages/credentials/fields.py">delete</a>(field_type, \*, package_name, credential_name) -> <a href="./src/droidrun_cloud/types/credentials/packages/credentials/field_delete_response.py">FieldDeleteResponse</a></code>
