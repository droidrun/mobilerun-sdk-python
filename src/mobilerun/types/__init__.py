# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import devices, element_node
from .. import _compat
from .task import Task as Task
from .device import Device as Device
from .llm_model import LlmModel as LlmModel
from .task_status import TaskStatus as TaskStatus
from .element_node import ElementNode as ElementNode
from .app_list_params import AppListParams as AppListParams
from .task_run_params import TaskRunParams as TaskRunParams
from .hook_list_params import HookListParams as HookListParams
from .task_list_params import TaskListParams as TaskListParams
from .app_list_response import AppListResponse as AppListResponse
from .task_run_response import TaskRunResponse as TaskRunResponse
from .device_list_params import DeviceListParams as DeviceListParams
from .hook_list_response import HookListResponse as HookListResponse
from .hook_update_params import HookUpdateParams as HookUpdateParams
from .task_list_response import TaskListResponse as TaskListResponse
from .task_stop_response import TaskStopResponse as TaskStopResponse
from .device_create_params import DeviceCreateParams as DeviceCreateParams
from .device_list_response import DeviceListResponse as DeviceListResponse
from .hook_update_response import HookUpdateResponse as HookUpdateResponse
from .hook_perform_response import HookPerformResponse as HookPerformResponse
from .hook_subscribe_params import HookSubscribeParams as HookSubscribeParams
from .hook_retrieve_response import HookRetrieveResponse as HookRetrieveResponse
from .task_retrieve_response import TaskRetrieveResponse as TaskRetrieveResponse
from .hook_subscribe_response import HookSubscribeResponse as HookSubscribeResponse
from .credential_list_response import CredentialListResponse as CredentialListResponse
from .task_get_status_response import TaskGetStatusResponse as TaskGetStatusResponse
from .task_run_streamed_params import TaskRunStreamedParams as TaskRunStreamedParams
from .hook_unsubscribe_response import HookUnsubscribeResponse as HookUnsubscribeResponse
from .task_get_trajectory_response import TaskGetTrajectoryResponse as TaskGetTrajectoryResponse
from .hook_get_sample_data_response import HookGetSampleDataResponse as HookGetSampleDataResponse

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    element_node.ElementNode.update_forward_refs()  # type: ignore
    devices.state_ui_response.StateUiResponse.update_forward_refs()  # type: ignore
else:
    element_node.ElementNode.model_rebuild(_parent_namespace_depth=0)
    devices.state_ui_response.StateUiResponse.model_rebuild(_parent_namespace_depth=0)
