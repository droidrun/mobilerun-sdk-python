# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import devices
from .. import _compat
from .flow import Flow as Flow
from .task import Task as Task
from .device import Device as Device
from .shared import (
    Meta as Meta,
    Socks5 as Socks5,
    Location as Location,
    DeviceSpec as DeviceSpec,
    Pagination as Pagination,
    DeviceCarrier as DeviceCarrier,
    PermissionSet as PermissionSet,
    PaginationMeta as PaginationMeta,
    DeviceIdentifiers as DeviceIdentifiers,
)
from .profile import Profile as Profile
from .task_status import TaskStatus as TaskStatus
from .proxy_config import ProxyConfig as ProxyConfig
from .usage_result import UsageResult as UsageResult
from .app_list_params import AppListParams as AppListParams
from .task_run_params import TaskRunParams as TaskRunParams
from .task_list_params import TaskListParams as TaskListParams
from .app_list_response import AppListResponse as AppListResponse
from .proxy_list_params import ProxyListParams as ProxyListParams
from .task_run_response import TaskRunResponse as TaskRunResponse
from .device_list_params import DeviceListParams as DeviceListParams
from .task_list_response import TaskListResponse as TaskListResponse
from .task_stop_response import TaskStopResponse as TaskStopResponse
from .app_delete_response import AppDeleteResponse as AppDeleteResponse
from .carrier_list_params import CarrierListParams as CarrierListParams
from .model_list_response import ModelListResponse as ModelListResponse
from .package_credentials import PackageCredentials as PackageCredentials
from .profile_list_params import ProfileListParams as ProfileListParams
from .proxy_create_params import ProxyCreateParams as ProxyCreateParams
from .proxy_list_response import ProxyListResponse as ProxyListResponse
from .proxy_lookup_params import ProxyLookupParams as ProxyLookupParams
from .proxy_update_params import ProxyUpdateParams as ProxyUpdateParams
from .webhook_list_params import WebhookListParams as WebhookListParams
from .device_create_params import DeviceCreateParams as DeviceCreateParams
from .device_list_response import DeviceListResponse as DeviceListResponse
from .app_retrieve_response import AppRetrieveResponse as AppRetrieveResponse
from .carrier_create_params import CarrierCreateParams as CarrierCreateParams
from .carrier_list_response import CarrierListResponse as CarrierListResponse
from .carrier_lookup_params import CarrierLookupParams as CarrierLookupParams
from .carrier_update_params import CarrierUpdateParams as CarrierUpdateParams
from .device_count_response import DeviceCountResponse as DeviceCountResponse
from .profile_create_params import ProfileCreateParams as ProfileCreateParams
from .profile_list_response import ProfileListResponse as ProfileListResponse
from .profile_update_params import ProfileUpdateParams as ProfileUpdateParams
from .proxy_create_response import ProxyCreateResponse as ProxyCreateResponse
from .proxy_delete_response import ProxyDeleteResponse as ProxyDeleteResponse
from .proxy_lookup_response import ProxyLookupResponse as ProxyLookupResponse
from .proxy_update_response import ProxyUpdateResponse as ProxyUpdateResponse
from .webhook_create_params import WebhookCreateParams as WebhookCreateParams
from .webhook_list_response import WebhookListResponse as WebhookListResponse
from .webhook_update_params import WebhookUpdateParams as WebhookUpdateParams
from .credential_list_params import CredentialListParams as CredentialListParams
from .device_set_name_params import DeviceSetNameParams as DeviceSetNameParams
from .task_retrieve_response import TaskRetrieveResponse as TaskRetrieveResponse
from .carrier_create_response import CarrierCreateResponse as CarrierCreateResponse
from .carrier_delete_response import CarrierDeleteResponse as CarrierDeleteResponse
from .carrier_lookup_response import CarrierLookupResponse as CarrierLookupResponse
from .carrier_update_response import CarrierUpdateResponse as CarrierUpdateResponse
from .device_terminate_params import DeviceTerminateParams as DeviceTerminateParams
from .profile_delete_response import ProfileDeleteResponse as ProfileDeleteResponse
from .proxy_retrieve_response import ProxyRetrieveResponse as ProxyRetrieveResponse
from .webhook_create_response import WebhookCreateResponse as WebhookCreateResponse
from .webhook_update_response import WebhookUpdateResponse as WebhookUpdateResponse
from .app_mark_failed_response import AppMarkFailedResponse as AppMarkFailedResponse
from .credential_list_response import CredentialListResponse as CredentialListResponse
from .task_get_status_response import TaskGetStatusResponse as TaskGetStatusResponse
from .task_run_streamed_params import TaskRunStreamedParams as TaskRunStreamedParams
from .task_send_message_params import TaskSendMessageParams as TaskSendMessageParams
from .carrier_retrieve_response import CarrierRetrieveResponse as CarrierRetrieveResponse
from .package_credentials_param import PackageCredentialsParam as PackageCredentialsParam
from .webhook_retrieve_response import WebhookRetrieveResponse as WebhookRetrieveResponse
from .app_list_versions_response import AppListVersionsResponse as AppListVersionsResponse
from .task_send_message_response import TaskSendMessageResponse as TaskSendMessageResponse
from .app_confirm_upload_response import AppConfirmUploadResponse as AppConfirmUploadResponse
from .device_fingerprint_response import DeviceFingerprintResponse as DeviceFingerprintResponse
from .task_get_trajectory_response import TaskGetTrajectoryResponse as TaskGetTrajectoryResponse
from .webhook_event_types_response import WebhookEventTypesResponse as WebhookEventTypesResponse
from .webhook_rotate_secret_response import WebhookRotateSecretResponse as WebhookRotateSecretResponse
from .webhook_test_delivery_response import WebhookTestDeliveryResponse as WebhookTestDeliveryResponse
from .app_create_signed_upload_url_params import AppCreateSignedUploadURLParams as AppCreateSignedUploadURLParams
from .app_create_signed_upload_url_response import AppCreateSignedUploadURLResponse as AppCreateSignedUploadURLResponse

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    devices.a11_y_node.A11YNode.update_forward_refs()  # type: ignore
    devices.state_ui_response.StateUiResponse.update_forward_refs()  # type: ignore
else:
    devices.a11_y_node.A11YNode.model_rebuild(_parent_namespace_depth=0)
    devices.state_ui_response.StateUiResponse.model_rebuild(_parent_namespace_depth=0)
