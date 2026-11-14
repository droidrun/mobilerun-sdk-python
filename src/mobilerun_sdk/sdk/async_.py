# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from types import TracebackType
from typing import (
    Any,
    Dict,
    List,
    Union,
    Generic,
    Mapping,
    Callable,
    Iterable,
    Optional,
    Sequence,
    Awaitable,
    cast,
)
from datetime import datetime, timezone
from typing_extensions import Literal, overload, override

import anyio
import httpx
from httpx import Timeout
from pydantic import BaseModel

from ..types import (
    task_run_params,
    app_list_response as __types_app_list_response,
    file_list_response as __types_file_list_response,
    task_list_response as __types_task_list_response,
    agent_list_response as __types_agent_list_response,
    proxy_list_response as __types_proxy_list_response,
    device_create_params,
    device_list_response as __types_device_list_response,
    number_list_response as __types_number_list_response,
    mailbox_list_response as __types_mailbox_list_response,
    message_list_response as __types_message_list_response,
    webhook_create_params,
    webhook_list_response as __types_webhook_list_response,
    task_run_streamed_params,
    app_create_signed_upload_url_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from ._common import (
    SINGLE_CALL_INTERVAL,
    ObjectPage,
    Screenshot,
    WaitOutput,
    UploadError,
    UploadInput,
    AsyncObjectPage,
    AsyncObjectPager,
    ObjectReadyError,
    _ModelT,
    _OutputT,
    read_path,
    check_wait,
    wait_async,
    bound_extra,
    ready_async,
    upload_urls,
    parse_output,
    record_field,
    condition_met,
    output_parser,
    prepare_upload,
    verify_webhook,
    next_object_page,
    put_upload_async,
    next_object_cursor,
    model_output_schema,
    attach_cleanup_error,
    definite_confirm_failure,
)
from .._client import AsyncMobilerun
from .._constants import DEFAULT_MAX_RETRIES
from ..types.agents import (
    file_list_response as __types_agents_file_list_response,
    profile_update_params,
    request_list_response as __types_agents_request_list_response,
    routine_create_params,
    request_list_for_agent_response as __types_agents_request_list_for_agent_response,
)
from ..types.connect import (
    user_list_response as __types_connect_user_list_response,
    proxy_list_response as __types_connect_proxy_list_response,
)
from ..types.devices import (
    task_list_response as __types_devices_task_list_response,
    proxy_connect_params,
    recording_list_response as __types_devices_recording_list_response,
    screenshot_list_response as __types_devices_screenshot_list_response,
    traffic_session_list_response as __types_devices_traffic_session_list_response,
)
from ..types.numbers import message_list_response as __types_numbers_message_list_response
from ..types.webhooks import delivery_list_for_webhook_response as __types_webhooks_delivery_list_for_webhook_response
from ..types.mailboxes import message_list_response as __types_mailboxes_message_list_response
from ..types.workflows import (
    flow_create_params,
    flow_list_response as __types_workflows_flow_list_response,
    flow_update_params,
    action_list_response as __types_workflows_action_list_response,
    flow_validate_params,
    trigger_create_params,
    trigger_list_response as __types_workflows_trigger_list_response,
    trigger_update_params,
    execution_list_response as __types_workflows_execution_list_response,
    action_catalog_list_response as __types_workflows_action_catalog_list_response,
)
from ..types.credentials import (
    package_list_response as __types_credentials_package_list_response,
    package_list_all_response as __types_credentials_package_list_all_response,
)
from ..types.shared.location import Location as SharedLocation
from ..types.workflows.flows import action_add_params, action_replace_params
from ..types.app_list_response import AppListResponse as TypesAppListResponse
from ..types.task_run_response import TaskRunResponse
from ..types.file_list_response import FileListResponse as TypesFileListResponse
from ..types.task_list_response import TaskListResponse as TypesTaskListResponse
from ..types.task_stop_response import TaskStopResponse
from ..types.agent_list_response import AgentListResponse
from ..types.app_delete_response import AppDeleteResponse
from ..types.proxy_list_response import ProxyListResponse as TypesProxyListResponse
from ..types.credentials.packages import link_create_params, credential_create_params
from ..types.device_list_response import DeviceListResponse
from ..types.file_delete_response import FileDeleteResponse
from ..types.file_update_response import FileUpdateResponse
from ..types.mailbox_otp_response import Data, MailboxOtpResponse
from ..types.number_list_response import NumberListResponse
from ..types.agent_create_response import AgentCreateResponse
from ..types.app_retrieve_response import AppRetrieveResponse
from ..types.file_confirm_response import FileConfirmResponse
from ..types.mailbox_list_response import MailboxListResponse
from ..types.message_list_response import MessageListResponse as TypesMessageListResponse
from ..types.proxy_create_response import ProxyCreateResponse
from ..types.proxy_delete_response import ProxyDeleteResponse
from ..types.proxy_update_response import ProxyUpdateResponse as TypesProxyUpdateResponse
from ..types.webhook_list_response import WebhookListResponse
from ..types.device_create_response import DeviceCreateResponse
from ..types.number_create_response import NumberCreateResponse
from ..types.number_delete_response import NumberDeleteResponse
from ..types.number_update_response import NumberUpdateResponse
from ..types.shared_params.location import Location as SharedParamsLocation
from ..types.task_retrieve_response import TaskRetrieveResponse
from ..types.device_summary_response import DeviceSummaryResponse
from ..types.mailbox_create_response import MailboxCreateResponse
from ..types.mailbox_delete_response import MailboxDeleteResponse
from ..types.mailbox_update_response import MailboxUpdateResponse
from ..types.proxy_retrieve_response import ProxyRetrieveResponse as TypesProxyRetrieveResponse
from ..types.webhook_create_response import WebhookCreateResponse
from ..types.webhook_update_response import WebhookUpdateResponse
from ..types.credential_list_response import CredentialListResponse
from ..types.device_retrieve_response import DeviceRetrieveResponse
from ..types.device_set_name_response import DeviceSetNameResponse
from ..types.file_upload_url_response import FileUploadURLResponse
from ..types.mailbox_restart_response import MailboxRestartResponse
from ..types.number_capacity_response import NumberCapacityResponse
from ..types.number_retrieve_response import NumberRetrieveResponse as TypesNumberRetrieveResponse
from ..types.task_get_status_response import TaskGetStatusResponse
from ..types.agents.file_list_response import FileListResponse as AgentsFileListResponse
from ..types.devices.app_list_response import AppListResponse as DevicesAppListResponse
from ..types.devices.state_ui_response import StateUiResponse
from ..types.mailbox_capacity_response import MailboxCapacityResponse
from ..types.mailbox_retrieve_response import MailboxRetrieveResponse
from ..types.mailbox_uncancel_response import MailboxUncancelResponse
from ..types.message_retrieve_response import MessageRetrieveResponse as TypesMessageRetrieveResponse
from ..types.number_countries_response import NumberCountriesResponse
from ..types.webhook_retrieve_response import WebhookRetrieveResponse
from ..types.app_list_versions_response import AppListVersionsResponse
from ..types.app_storage_usage_response import AppStorageUsageResponse
from ..types.connect.proxy_buy_response import ProxyBuyResponse
from ..types.connect.user_list_response import UserListResponse
from ..types.device_wait_ready_response import DeviceWaitReadyResponse
from ..types.devices.esim_list_response import EsimListResponse
from ..types.devices.file_list_response import FileListResponse as DevicesFileListResponse
from ..types.devices.task_list_response import TaskListResponse as DevicesTaskListResponse
from ..types.task_send_message_response import TaskSendMessageResponse
from ..types.connect.proxy_list_response import ProxyListResponse as ConnectProxyListResponse
from ..types.connect.proxy_ping_response import ProxyPingResponse
from ..types.device_fingerprint_response import DeviceFingerprintResponse
from ..types.mailbox_disconnect_response import MailboxDisconnectResponse
from ..types.workflows.flow_run_response import FlowRunResponse
from ..types.agents.request_list_response import RequestListResponse
from ..types.connect.user_create_response import UserCreateResponse
from ..types.connect.user_update_response import UserUpdateResponse
from ..types.devices.esim_status_response import EsimStatusResponse
from ..types.devices.number_bind_response import NumberBindResponse
from ..types.file_cancel_pending_response import FileCancelPendingResponse
from ..types.shared_params.device_carrier import DeviceCarrier
from ..types.task_get_trajectory_response import TaskGetTrajectoryResponse
from ..types.tasks.ui_state_list_response import UiStateListResponse
from ..types.workflows.flow_list_response import FlowListResponse
from ..types.agent_model_profiles_response import AgentModelProfilesResponse
from ..types.agents.routine_clone_response import RoutineCloneResponse
from ..types.connect.proxy_update_response import ProxyUpdateResponse as ConnectProxyUpdateResponse
from ..types.devices.language_get_response import LanguageGetResponse
from ..types.devices.package_list_response import PackageListResponse as DevicesPackageListResponse
from ..types.devices.proxy_status_response import ProxyStatusResponse
from ..types.devices.timezone_get_response import TimezoneGetResponse
from ..types.numbers.message_list_response import MessageListResponse as NumbersMessageListResponse
from ..types.numbers.message_send_response import MessageSendResponse
from ..types.workflows.flow_clone_response import FlowCloneResponse
from ..types.agents.profile_update_response import ProfileUpdateResponse
from ..types.agents.routine_create_response import RoutineCreateResponse
from ..types.connect.user_retrieve_response import UserRetrieveResponse
from ..types.devices.clipboard_get_response import ClipboardGetResponse
from ..types.devices.esim.apn_list_response import ApnListResponse
from ..types.devices.esim_activate_response import EsimActivateResponse
from ..types.devices.number_unbind_response import NumberUnbindResponse
from ..types.tasks.screenshot_list_response import ScreenshotListResponse as TasksScreenshotListResponse
from ..types.webhook_rotate_secret_response import WebhookRotateSecretResponse
from ..types.webhook_test_delivery_response import WebhookTestDeliveryResponse
from ..types.workflows.action_list_response import ActionListResponse as WorkflowsActionListResponse
from ..types.workflows.flow_create_response import FlowCreateResponse
from ..types.workflows.flow_delete_response import FlowDeleteResponse
from ..types.workflows.flow_update_response import FlowUpdateResponse
from ..types.workflows.flow_verify_response import FlowVerifyResponse
from ..types.connect.proxy_checkout_response import ProxyCheckoutResponse
from ..types.connect.proxy_retrieve_response import ProxyRetrieveResponse as ConnectProxyRetrieveResponse
from ..types.devices.recording_list_response import RecordingListResponse
from ..types.devices.recording_stop_response import RecordingStopResponse
from ..types.mailboxes.message_list_response import MessageListResponse as MailboxesMessageListResponse
from ..types.workflows.flow_dry_run_response import FlowDryRunResponse
from ..types.workflows.flow_unblock_response import FlowUnblockResponse
from ..types.workflows.trigger_fire_response import TriggerFireResponse
from ..types.workflows.trigger_list_response import TriggerListResponse
from ..types.agents.request_retrieve_response import RequestRetrieveResponse
from ..types.devices.number_retrieve_response import NumberRetrieveResponse as DevicesNumberRetrieveResponse
from ..types.devices.recording_start_response import RecordingStartResponse
from ..types.devices.screenshot_list_response import ScreenshotListResponse as DevicesScreenshotListResponse
from ..types.shared_params.device_identifiers import DeviceIdentifiers
from ..types.tasks.ui_state_retrieve_response import UiStateRetrieveResponse
from ..types.workflows.action_create_response import ActionCreateResponse
from ..types.workflows.action_delete_response import ActionDeleteResponse
from ..types.workflows.action_update_response import ActionUpdateResponse
from ..types.workflows.flow_activate_response import FlowActivateResponse
from ..types.workflows.flow_capacity_response import FlowCapacityResponse
from ..types.workflows.flow_retrieve_response import FlowRetrieveResponse
from ..types.workflows.flow_validate_response import FlowValidateResponse
from ..types.agents.conversation_list_response import ConversationListResponse as AgentsConversationListResponse
from ..types.credentials.package_list_response import PackageListResponse as CredentialsPackageListResponse
from ..types.devices.recording_status_response import RecordingStatusResponse
from ..types.workflows.execution_list_response import ExecutionListResponse
from ..types.workflows.trigger_create_response import TriggerCreateResponse
from ..types.workflows.trigger_delete_response import TriggerDeleteResponse
from ..types.workflows.trigger_update_response import TriggerUpdateResponse
from ..types.devices.app_list_installs_response import AppListInstallsResponse
from ..types.tasks.screenshot_retrieve_response import ScreenshotRetrieveResponse
from ..types.webhooks.integration_list_response import IntegrationListResponse
from ..types.workflows.action_retrieve_response import ActionRetrieveResponse
from ..types.workflows.execution_abort_response import ExecutionAbortResponse
from ..types.agents.conversation_create_response import ConversationCreateResponse
from ..types.credentials.package_create_response import PackageCreateResponse
from ..types.mailboxes.message_retrieve_response import MessageRetrieveResponse as MailboxesMessageRetrieveResponse
from ..types.messages.conversation_list_response import ConversationListResponse as MessagesConversationListResponse
from ..types.workflows.flows.action_add_response import ActionAddResponse
from ..types.workflows.flows.state_list_response import StateListResponse
from ..types.workflows.trigger_retrieve_response import TriggerRetrieveResponse
from ..types.devices.number_binding_list_response import NumberBindingListResponse
from ..types.mailboxes.connection_create_response import ConnectionCreateResponse
from ..types.workflows.flow_list_repairs_response import FlowListRepairsResponse
from ..types.workflows.flows.action_list_response import ActionListResponse as FlowsActionListResponse
from ..types.app_create_signed_upload_url_response import AppCreateSignedUploadURLResponse
from ..types.connect.proxy_ensure_healthy_response import ProxyEnsureHealthyResponse
from ..types.credentials.package_list_all_response import PackageListAllResponse
from ..types.device_retrieve_capabilities_response import DeviceRetrieveCapabilitiesResponse
from ..types.devices.traffic_session_list_response import TrafficSessionListResponse
from ..types.workflows.execution_retrieve_response import ExecutionRetrieveResponse
from ..types.workflows.flows.state_delete_response import StateDeleteResponse
from ..types.agents.request_list_for_agent_response import RequestListForAgentResponse
from ..types.connect.user_list_connections_response import UserListConnectionsResponse
from ..types.devices.recording_screenshots_response import RecordingScreenshotsResponse
from ..types.mailboxes.connection_retrieve_response import ConnectionRetrieveResponse
from ..types.workflows.action_catalog_list_response import ActionCatalogListResponse
from ..types.workflows.flows.action_remove_response import ActionRemoveResponse
from ..types.connect.proxy_list_connections_response import ProxyListConnectionsResponse
from ..types.devices.action_overlay_visible_response import ActionOverlayVisibleResponse
from ..types.devices.browser_execute_script_response import BrowserExecuteScriptResponse
from ..types.devices.traffic_session_create_response import TrafficSessionCreateResponse
from ..types.devices.traffic_session_delete_response import TrafficSessionDeleteResponse
from ..types.workflows.actions.service_list_response import ServiceListResponse
from ..types.workflows.flow_retrieve_repair_response import FlowRetrieveRepairResponse
from ..types.workflows.flows.action_replace_response import ActionReplaceResponse
from ..types.messages.conversation_mark_read_response import ConversationMarkReadResponse
from ..types.workflows.execution_get_metrics_response import ExecutionGetMetricsResponse
from ..types.workflows.flow_delivery_options_response import FlowDeliveryOptionsResponse
from ..types.workflows.flow_template_context_response import FlowTemplateContextResponse
from ..types.credentials.packages.link_create_response import LinkCreateResponse
from ..types.devices.traffic_session_retrieve_response import TrafficSessionRetrieveResponse
from ..types.webhooks.integration_list_targets_response import IntegrationListTargetsResponse
from ..types.workflows.action_catalog_retrieve_response import ActionCatalogRetrieveResponse
from ..types.agents.request_retrieve_by_session_response import RequestRetrieveBySessionResponse
from ..types.webhooks.delivery_list_for_webhook_response import DeliveryListForWebhookResponse
from ..types.webhooks.delivery_retrieve_attempts_response import DeliveryRetrieveAttemptsResponse
from ..types.workflows.flows.state_list_versions_response import StateListVersionsResponse
from ..types.credentials.packages.credential_create_response import CredentialCreateResponse
from ..types.credentials.packages.credential_delete_response import CredentialDeleteResponse
from ..types.devices.number_binding_list_candidates_response import NumberBindingListCandidatesResponse
from ..types.workflows.actions.service_list_methods_response import ServiceListMethodsResponse
from ..types.credentials.packages.credentials.field_create_response import FieldCreateResponse
from ..types.credentials.packages.credentials.field_delete_response import FieldDeleteResponse
from ..types.credentials.packages.credentials.field_update_response import FieldUpdateResponse


class AsyncMobilerunSDK:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        http_client: httpx.AsyncClient | None = None,
        _strict_response_validation: bool = False,
    ) -> None:
        self.api = AsyncMobilerun(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
            _strict_response_validation=_strict_response_validation,
        )
        self.apps = AsyncAppManager(self.api)
        self.credentials = _AsyncSDKCredentials(self.api)
        self.devices = AsyncDeviceManager(self.api)
        self.models = self.api.models
        self.proxies = AsyncProxyConfigurationManager(self.api)
        self.connect = _AsyncSDKConnect(self.api)
        self.tasks = AsyncTaskManager(self.api)
        self.workflows = _AsyncSDKWorkflows(self.api)
        self.webhooks = AsyncWebhookManager(self.api)
        self.mailboxes = AsyncMailboxManager(self.api)
        self.files = AsyncAgentFileManager(self.api)
        self.agents = AsyncAgentManager(self.api)
        self.assistant = self.api.assistant
        self.messages = AsyncNumberMessageManager(self.api)
        self.numbers = AsyncPhoneNumberManager(self.api)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class _AsyncSDKCredentials:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self._resource = api.credentials
        self.packages = AsyncCredentialPackageManager(self.api)
        self.onepassword = self.api.credentials.onepassword

    def __getattr__(self, name: str) -> Any:
        return getattr(self._resource, name)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialListResponse:
        """
        Returns a paginated list of all credentials belonging to the authenticated user
        across every package. Accepts standard pagination query parameters and responds
        with the credential items plus pagination metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.credentials.list(
            page=page,
            page_size=page_size,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result


class _AsyncSDKConnect:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self._resource = api.connect
        self.countries = self.api.connect.countries
        self.proxies = AsyncConnectProxyManager(self.api)
        self.users = AsyncConnectUserManager(self.api)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._resource, name)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class _AsyncSDKWorkflows:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self._resource = api.workflows
        self.triggers = AsyncTriggerManager(self.api)
        self.action_catalog = AsyncCatalogEntryManager(self.api)
        self.actions = AsyncWorkflowActionManager(self.api)
        self.flows = AsyncFlowManager(self.api)
        self.events = self.api.workflows.events
        self.executions = AsyncExecutionManager(self.api)
        self.timezones = self.api.workflows.timezones

    def __getattr__(self, name: str) -> Any:
        return getattr(self._resource, name)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class AsyncAppManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncApp:
        return AsyncApp(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncApp:
        info = await self.api.apps.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncApp(self.api, id, info, info_root="data")

    def list(
        self,
        *,
        order: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        platform: Literal["all", "android", "ios"] | Omit = omit,
        query: str | Omit = omit,
        sort_by: Literal["createdAt", "name"] | Omit = omit,
        status: Literal["all", "queued", "available", "failed", "pruned"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncApp, TypesAppListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncApp, TypesAppListResponse]:
            __page = await self.api.apps.list(
                order=order,
                page=page,
                page_size=page_size,
                platform=platform,
                query=query,
                sort_by=sort_by,
                status=status,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncApp(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    async def create_signed_upload_url(
        self,
        *,
        bundle_id: str,
        display_name: str,
        files: Iterable[app_create_signed_upload_url_params.File],
        version_code: float,
        version_name: str,
        country: str | Omit = omit,
        description: str | Omit = omit,
        developer_name: str | Omit = omit,
        icon_url: str | Omit = omit,
        platform: Literal["android", "ios"] | Omit = omit,
        target_sdk: float | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AppCreateSignedUploadURLResponse:
        """
        Creates or updates an app and returns pre-signed upload URLs for each file.
        Honours an optional `Idempotency-Key` header: a retry with the same key and body
        returns the same app and version with freshly signed URLs and
        `Idempotent-Replayed: true`, and never creates a second version. An
        Idempotency-Key is honoured for 7 days; after that it behaves like a fresh
        request. A replay whose version was deleted is a 404; a replay whose version
        already left the queued state is a 409 `idempotency_key_consumed`; a replay that
        cannot get the version lock within 5 s is a 409
        `idempotency_request_in_progress`. Every response produced by a replay,
        including those 404/409 errors, carries `Idempotent-Replayed: true`. A same-key
        request still in flight after a 5 s wait is a 409
        `idempotency_request_in_progress` (retry after `Retry-After`). If signing fails,
        nothing is persisted (with or without a key) and the same request, key included,
        can be retried.

        Args:
          country: Country code for Search Results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.apps.create_signed_upload_url(
            bundle_id=bundle_id,
            display_name=display_name,
            files=files,
            version_code=version_code,
            version_name=version_name,
            country=country,
            description=description,
            developer_name=developer_name,
            icon_url=icon_url,
            platform=platform,
            target_sdk=target_sdk,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def storage_usage(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppStorageUsageResponse:
        """
        Returns the user’s storage allowance in bytes: bytes used, bytes included in the
        plan, the hard maximum (included + max purchasable overage; null = unlimited)
        and whether usage above the included amount is billed as overage. With storage
        billing off there is no limit: only usedBytes is set.
        """
        result = await self.api.apps.storage_usage(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def upload(
        self,
        *,
        files: Sequence[UploadInput],
        bundle_id: str,
        display_name: str,
        version_code: float,
        version_name: str,
        country: str | Omit = omit,
        description: str | Omit = omit,
        developer_name: str | Omit = omit,
        icon_url: str | Omit = omit,
        platform: Literal["android", "ios"] | Omit = omit,
        target_sdk: float | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncApp:
        """Upload to presigned storage, confirm, and return the object. Uses storage quota."""
        prepared = [prepare_upload(file) for file in files]
        if not prepared or len({file.filename for file in prepared}) != len(prepared):
            raise TypeError("Upload needs unique, nonempty file names")
        issued = await self.api.apps.create_signed_upload_url(
            bundle_id=bundle_id,
            display_name=display_name,
            files=cast(Any, [{"file_name": file.filename, "content_type": file.content_type} for file in prepared]),
            version_code=version_code,
            version_name=version_name,
            country=country,
            description=description,
            developer_name=developer_name,
            icon_url=icon_url,
            platform=platform,
            target_sdk=target_sdk,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=bound_extra(
                extra_body,
                {"files": [{"fileName": file.filename, "contentType": file.content_type} for file in prepared]},
            ),
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        confirmed = False
        confirming = False
        try:
            urls = upload_urls(
                issued,
                prepared,
                {
                    "request": "create_signed_upload_url",
                    "files_param": "files",
                    "urls_path": "r2UploadUrls",
                    "url_field": "r2UploadUrl",
                    "name_field": "fileName",
                    "name_param": "fileName",
                    "mime_param": "contentType",
                    "id_path": "versionId",
                    "confirm": "confirm_upload",
                    "fail": "mark_failed",
                    "returns": "App",
                    "get": "retrieve",
                    "get_id_path": "appId",
                },
            )
            for prepared_file, url in zip(prepared, urls, strict=True):
                await put_upload_async(self.api, prepared_file, url, timeout=timeout)
            confirming = True
            await self.api.apps.confirm_upload(
                issued.version_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            )
            confirmed = True
            info = await self.api.apps.retrieve(
                issued.app_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncApp(self.api, info.data.id, info, info_root="data")
        except BaseException as error:
            if not confirmed and (not confirming or definite_confirm_failure(error)):
                try:
                    with anyio.CancelScope(shield=True):
                        with anyio.move_on_after(10):
                            await self.api.apps.mark_failed(
                                issued.version_id,
                                extra_headers=extra_headers,
                                extra_query=extra_query,
                                extra_body=extra_body,
                                timeout=timeout,
                                idempotency_key=idempotency_key,
                            )
                except BaseException:
                    pass
            if not isinstance(error, Exception):
                raise
            raise UploadError() from error


class AsyncCredentialPackageManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncCredentialPackage:
        return AsyncCredentialPackage(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncCredentialPackage:
        info = await self.api.credentials.packages.list(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        rows = info.data or []
        object_id = rows[0].package_name if rows else id
        return AsyncCredentialPackage(self.api, object_id, info)

    async def create(
        self,
        *,
        package_name: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncCredentialPackage:
        """
        Creates a new package (identified by `packageName`) under which credentials can
        be grouped. Returns a conflict if a package with the same name already exists
        for the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.credentials.packages.create(
            package_name=package_name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncCredentialPackage(self.api, info.data.package_name, info, owned=True)

        return object

    def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncCredentialPackage, PackageListAllResponse]:
        async def load() -> AsyncObjectPage[AsyncCredentialPackage, PackageListAllResponse]:
            __page = await self.api.credentials.packages.list_all(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            )
            return AsyncObjectPage(
                [AsyncCredentialPackage(self.api, item.package_name, item) for item in (__page.data or [])], __page
            )

        return AsyncObjectPager(load)


class AsyncCredentialManager:
    def __init__(self, api: AsyncMobilerun, package_name: str) -> None:
        self.api = api
        self._package_name = package_name

    @property
    def package_name(self) -> str:
        return self._package_name

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncCredential:
        return AsyncCredential(self.api, self.package_name, id)

    async def create(
        self,
        *,
        credential_name: str,
        fields: Iterable[credential_create_params.Field],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncCredential:
        """
        Creates a credential under the given package with a `credentialName` and at
        least one field. Each field has a `fieldType` (email, username, password,
        api_token, phone_number, two_factor_secret, or backup_codes) and a value.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.credentials.packages.credentials.create(
            self.package_name,
            credential_name=credential_name,
            fields=fields,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncCredential(
            self.api, self.package_name, info.data.credential_name, info, owned=True, info_root="data"
        )

        return object

    def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncCredential, CredentialsPackageListResponse]:
        async def load() -> AsyncObjectPage[AsyncCredential, CredentialsPackageListResponse]:
            __page = await self.api.credentials.packages.list(
                self.package_name,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [
                    AsyncCredential(self.api, self.package_name, item.credential_name, item, info_root="")
                    for item in (__page.data or [])
                ],
                __page,
            )

        return AsyncObjectPager(load)


class _AsyncDeviceManagerNumberBindings:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberBindingListResponse:
        result = await self.api.devices.number_bindings.list(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def list_candidates(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberBindingListCandidatesResponse:
        result = await self.api.devices.number_bindings.list_candidates(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result


class AsyncDeviceManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self.number_bindings = _AsyncDeviceManagerNumberBindings(api)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncDevice:
        return AsyncDevice(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncDevice:
        info = await self.api.devices.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncDevice(self.api, id, info, info_root="")

    async def create(
        self,
        *,
        billing: Literal["auto", "subscription", "minute"] | Omit = omit,
        body_country: str | Omit = omit,
        device_type: Literal["android_cloud_phone", "ios_phone", "device_slot"] | Omit = omit,
        profile_id: str | Omit = omit,
        template: str | Omit = omit,
        android_version: int | Omit = omit,
        apps: Optional[SequenceNotStr[str]] | Omit = omit,
        carrier: DeviceCarrier | Omit = omit,
        files: Optional[SequenceNotStr[str]] | Omit = omit,
        identifiers: DeviceIdentifiers | Omit = omit,
        locale: str | Omit = omit,
        location: SharedParamsLocation | Omit = omit,
        name: str | Omit = omit,
        proxy: device_create_params.Proxy | Omit = omit,
        timezone: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
        wait_ready: bool = True,
        ready_timeout: float = 300,
        dispose_on_ready_failure: bool = True,
    ) -> AsyncDevice:
        """Starts billing for the device according to the selected billing mode.

        Requests a new device from the specification in the request body.

        Optional query
        parameters select the canonical device type, country, billing mode, and base
        profile. Returns the device, its resolved billing strategy, and its stream
        token.

        Args:
          billing: Billing mode. 'auto' tries subscription first, then minute billing if no
              subscription entitlement exists or all subscription slots are in use, provided
              minute billing is enabled. When subscription billing is disabled, auto uses
              minutes directly. Billing-service failures never trigger fallback.
              'subscription' requires an available subscription slot and never falls back.
              'minute' uses minute billing only, subject to balance and concurrency checks.
              Modes depend on the device type's billing configuration.

          query_country: ISO 3166-1 alpha-2 country code. If omitted the system picks the country with
              the most availability.

          device_type: Device type: android_cloud_phone (cloud Android phone), ios_phone or
              device_slot. Any other value is rejected with 422. Not every device type is
              available for creation; an unavailable type returns DEVICE_TYPE_UNAVAILABLE
              (422).

          profile_id: Profile ID to use as device spec

          template: Optional device template, e.g. onboarding. The device gets the template's
              Android version and preinstalled apps and is ready in seconds when a prepared
              phone is available; otherwise it boots with the same setup. Country, name and
              proxy still come from this request. Cannot be combined with profileId, apps or
              androidVersion. Omit it to create from the request alone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        check_wait(ready_timeout, SINGLE_CALL_INTERVAL)
        info = await self.api.devices.create(
            billing=billing,
            body_country=body_country,
            device_type=device_type,
            profile_id=profile_id,
            template=template,
            android_version=android_version,
            apps=apps,
            carrier=carrier,
            files=files,
            identifiers=identifiers,
            locale=locale,
            location=location,
            name=name,
            proxy=proxy,
            timezone=timezone,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncDevice(self.api, info.id, info, owned=True, info_root="")
        if wait_ready:
            try:
                await object.wait_ready(timeout=ready_timeout)
            except BaseException as cause:
                disposed = False
                cleanup_error: Optional[BaseException] = None
                if dispose_on_ready_failure:
                    try:
                        await object.__aexit__(None, None, None)
                        disposed = True
                    except BaseException as error:
                        cleanup_error = error
                if isinstance(cause, Exception):
                    raise ObjectReadyError(object, object.id, cause, disposed, cleanup_error) from cause
                cast(Any, cause).disposed = disposed
                cast(Any, cause).cleanup_error = cleanup_error
                cast(Any, cause).object = object
                cast(Any, cause).id = object.id
                raise
        return object

    def list(
        self,
        *,
        country: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        created_by: str | Omit = omit,
        mine: bool | Omit = omit,
        name: str | Omit = omit,
        order_by: Literal["id", "createdAt", "updatedAt", "assignedAt", "gridPosition"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        platform: Literal["android", "ios"] | Omit = omit,
        provider_id: str | Omit = omit,
        search: str | Omit = omit,
        state: Optional[
            List[
                Literal[
                    "creating",
                    "assigned",
                    "ready",
                    "rebooting",
                    "migrating",
                    "resetting",
                    "terminated",
                    "maintenance",
                    "stopped",
                    "unknown",
                ]
            ]
        ]
        | Omit = omit,
        type: Literal["android_cloud_phone", "ios_phone", "device_slot"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncDevice, DeviceListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncDevice, DeviceListResponse]:
            __page = await self.api.devices.list(
                country=country,
                created_after=created_after,
                created_before=created_before,
                created_by=created_by,
                mine=mine,
                name=name,
                order_by=order_by,
                order_by_direction=order_by_direction,
                page=page,
                page_size=page_size,
                platform=platform,
                provider_id=provider_id,
                search=search,
                state=state,
                type=type,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncDevice(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    async def summary(
        self,
        *,
        state: Optional[
            List[
                Literal[
                    "creating",
                    "assigned",
                    "ready",
                    "rebooting",
                    "migrating",
                    "resetting",
                    "terminated",
                    "maintenance",
                    "stopped",
                    "unknown",
                ]
            ]
        ]
        | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSummaryResponse:
        """
        Returns the total number of the user's devices and counts grouped by current
        state and device type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.summary(
            state=state, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result


class AsyncSavedScreenshotManager:
    def __init__(self, api: AsyncMobilerun, device_id: str) -> None:
        self.api = api
        self._device_id = device_id

    @property
    def device_id(self) -> str:
        return self._device_id

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncSavedScreenshot:
        return AsyncSavedScreenshot(self.api, self.device_id, id)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncSavedScreenshot, DevicesScreenshotListResponse]:
        async def load(
            __number: int | str | None, visited: set[str] | None = None
        ) -> AsyncObjectPage[AsyncSavedScreenshot, DevicesScreenshotListResponse]:
            seen = set(visited or ())
            if isinstance(__number, str):
                seen.add(__number)
            __page = await self.api.devices.screenshots.list(
                self.device_id,
                cursor=cursor,
                limit=limit,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"cursor": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [
                    AsyncSavedScreenshot(self.api, self.device_id, item.id, item, info_root="")
                    for item in (__page.items or [])
                ],
                __page,
                lambda: next_object_cursor(__page.next_cursor, __number, seen),
                lambda token: load(token, seen),
            )

        return AsyncObjectPager(lambda: load(cursor if isinstance(cursor, str) else None))


class AsyncRecordingManager:
    def __init__(self, api: AsyncMobilerun, device_id: str) -> None:
        self.api = api
        self._device_id = device_id

    @property
    def device_id(self) -> str:
        return self._device_id

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncRecording:
        return AsyncRecording(self.api, self.device_id, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncRecording:
        info = await self.api.devices.recordings.status(
            id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncRecording(self.api, self.device_id, id, info, info_root="")

    async def start(
        self,
        *,
        name: str | Omit = omit,
        quality: int | Omit = omit,
        retention_days: int | Omit = omit,
        types: Optional[SequenceNotStr[str]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncRecording:
        """
        Start a device recording

        Args:
          quality: Capture quality from 1 (lowest) to 10 (full stream quality). Defaults to the
              device's full quality. Honored only by devices that support adjustable capture
              quality.

          types: Artifacts to capture: trajectory (input actions; on some devices only when the
              device announces trajectory capture), video, and audio (captured into the video
              artifact, so it requires video; honored only by devices that support audio
              capture). Defaults to trajectory and video, narrowed to what the device
              produces.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.devices.recordings.start(
            self.device_id,
            name=name,
            quality=quality,
            retention_days=retention_days,
            types=types,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncRecording(self.api, self.device_id, info.id, info, owned=True, info_root="")

        return object

    def list(
        self,
        *,
        status: str | Omit = omit,
        type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncRecording, Optional[RecordingListResponse]]:
        async def load() -> AsyncObjectPage[AsyncRecording, Optional[RecordingListResponse]]:
            __page = await self.api.devices.recordings.list(
                self.device_id,
                status=status,
                type=type,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncRecording(self.api, self.device_id, item.id, item, info_root="") for item in (__page or [])],
                __page,
            )

        return AsyncObjectPager(load)


class AsyncTrafficSessionManager:
    def __init__(self, api: AsyncMobilerun, device_id: str) -> None:
        self.api = api
        self._device_id = device_id

    @property
    def device_id(self) -> str:
        return self._device_id

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncTrafficSession:
        return AsyncTrafficSession(self.api, self.device_id, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncTrafficSession:
        info = await self.api.devices.traffic_sessions.retrieve(
            id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncTrafficSession(self.api, self.device_id, id, info, info_root="")

    async def create(
        self,
        *,
        expires_in_seconds: int | Omit = omit,
        max_body_bytes: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncTrafficSession:
        """
        Starts one live-only decoded HTTP/1.1, HTTP/2, HTTP/3 and WebSocket traffic
        session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.devices.traffic_sessions.create(
            self.device_id,
            expires_in_seconds=expires_in_seconds,
            max_body_bytes=max_body_bytes,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncTrafficSession(self.api, self.device_id, info.id, info, owned=True, info_root="")

        return object

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncTrafficSession, TrafficSessionListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncTrafficSession, TrafficSessionListResponse]:
            __page = await self.api.devices.traffic_sessions.list(
                self.device_id,
                page=page,
                page_size=page_size,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [
                    AsyncTrafficSession(self.api, self.device_id, item.id, item, info_root="")
                    for item in (__page.items or [])
                ],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


class AsyncProxyConfigurationManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncProxyConfiguration:
        return AsyncProxyConfiguration(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncProxyConfiguration:
        info = await self.api.proxies.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncProxyConfiguration(self.api, id, info, info_root="data")

    async def create(
        self,
        *,
        host: str | Omit = omit,
        name: str,
        password: str | Omit = omit,
        port: int | Omit = omit,
        protocol: Literal["socks5"] | Literal["wireguard"],
        user: str | Omit = omit,
        config: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncProxyConfiguration:
        """Creates a proxy config.

        The body is a discriminated union on `protocol`:
        `socks5` requires name, host, port, user, and password, while `wireguard`
        requires name and a config string. Returns the created config with its generated
        `proxyId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await cast(Callable[..., Awaitable[ProxyCreateResponse]], self.api.proxies.create)(
            host=host,
            name=name,
            password=password,
            port=port,
            protocol=protocol,
            user=user,
            config=config,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncProxyConfiguration(self.api, info.data.proxy_id, info, owned=True, info_root="data")

        return object

    def list(
        self,
        *,
        protocol: Literal["socks5", "wireguard"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncProxyConfiguration, TypesProxyListResponse]:
        async def load() -> AsyncObjectPage[AsyncProxyConfiguration, TypesProxyListResponse]:
            __page = await self.api.proxies.list(
                protocol=protocol,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncProxyConfiguration(self.api, item.proxy_id, item, info_root="") for item in (__page.data or [])],
                __page,
            )

        return AsyncObjectPager(load)


class AsyncConnectProxyManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncConnectProxy:
        return AsyncConnectProxy(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncConnectProxy:
        info = await self.api.connect.proxies.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncConnectProxy(self.api, id, info, info_root="")

    def list(
        self,
        *,
        country: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncConnectProxy, ConnectProxyListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncConnectProxy, ConnectProxyListResponse]:
            __page = await self.api.connect.proxies.list(
                country=country,
                page=page,
                page_size=page_size,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncConnectProxy(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    async def buy(
        self,
        *,
        country: str,
        type: Literal["dedicated_residential", "residential", "mobile"],
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncConnectProxy:
        """Purchases a proxy; may incur charges or require checkout.


        Provisions a proxy of the requested type for the caller in the selected country.

        Args:
          country: ISO 3166-1 alpha-2 country code to provision the proxy in.

          name: Display name for the proxy, up to 64 characters excluding surrounding
              whitespace, and containing no NUL. Omit it (or send only whitespace) to get a
              generated label built from the country, type, and id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.connect.proxies.buy(
            country=country,
            type=type,
            name=name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return AsyncConnectProxy(self.api, result.id, result, info_root="")


class AsyncConnectUserManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncConnectUser:
        return AsyncConnectUser(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncConnectUser:
        info = await self.api.connect.users.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncConnectUser(self.api, id, info, info_root="")

    async def create(
        self,
        *,
        password: str | Omit = omit,
        proxy_id: str | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncConnectUser:
        """
        Creates a SOCKS5 credential, optionally bound to a proxy for dedicated routing.
        Username and password are generated when omitted.

        Args:
          password: Desired SOCKS5 password, 1-255 bytes (RFC 1929). Generated when omitted.

          proxy_id: Proxy to bind the user to for dedicated routing.

          username: Desired SOCKS5 username, 1-255 bytes (RFC 1929). Generated when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.connect.users.create(
            password=password,
            proxy_id=proxy_id,
            username=username,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncConnectUser(self.api, info.id, info, owned=True, info_root="")

        return object

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        proxy_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncConnectUser, UserListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncConnectUser, UserListResponse]:
            __page = await self.api.connect.users.list(
                page=page,
                page_size=page_size,
                proxy_id=proxy_id,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncConnectUser(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


class AsyncTaskManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncTask:
        return AsyncTask(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncTask:
        info = await self.api.tasks.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncTask(self.api, id, info, info_root="task")

    def list(
        self,
        *,
        created_by: Optional[str] | Omit = omit,
        mine: bool | Omit = omit,
        order_by: Optional[Literal["id", "createdAt", "finishedAt", "status"]] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        source: Optional[Literal["api", "agent"]] | Omit = omit,
        status: Optional[
            Literal["prepared", "queued", "created", "running", "cancelling", "completed", "failed", "cancelled"]
        ]
        | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncTask, TypesTaskListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncTask, TypesTaskListResponse]:
            __page = await self.api.tasks.list(
                created_by=created_by,
                mine=mine,
                order_by=order_by,
                order_by_direction=order_by_direction,
                page=page,
                page_size=page_size,
                query=query,
                source=source,
                status=status,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncTask(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    async def run_streamed(
        self,
        *,
        device_id: str,
        task: str,
        accessibility: bool | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        continue_on_failure: bool | Omit = omit,
        credentials: Iterable[task_run_streamed_params.Credential] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        humanize: bool | Omit = omit,
        internal: bool | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reasoning: bool | Omit = omit,
        recording_enabled: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        system_prompt: Optional[str] | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> object:
        """
        Create and dispatch a new agent task, returning an SSE stream of task events.
        Cancels the task if the client disconnects.

        Args:
          device_id: The ID of the device to run the task on.

          display_id: The display ID of the device to run the task on.

          execution_timeout: Maximum agent execution time in seconds (1–2700).

          humanize: Request human-like input where supported by the device. Replaces the deprecated
              stealth field; both must agree when supplied together.

          internal: Mark a task started by an agent or worker on the user's behalf. It is listed as
              source='agent' (excluded from source='api' lists) and its events carry
              internal=true so user-facing notifications and webhooks skip it. It is still
              billed, controllable and retrievable by id.

          llm_model: The LLM model identifier to use for the task (e.g.
              'mobilerun/mobile-agent-fast'). When omitted with reasoning=false, the fast-mode
              default model is used.

          recording_enabled: Record device video for the whole task and persist a retrievable reference

          stealth: Deprecated: use humanize. Both names must agree when supplied together.

          subagent_model: LLM model used by sub-agent roles: executor, app_opener, structured_output

          system_prompt: Optional custom behavioral overlay applied on top of the agent's default system
              prompts. Never echoed back in responses or errors.

          temperature: Deprecated and ignored. Sampling behavior is controlled by the model provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.tasks.run_streamed(
            device_id=device_id,
            task=task,
            accessibility=accessibility,
            apps=apps,
            continue_on_failure=continue_on_failure,
            credentials=credentials,
            display_id=display_id,
            execution_timeout=execution_timeout,
            files=files,
            humanize=humanize,
            internal=internal,
            llm_model=llm_model,
            max_steps=max_steps,
            output_schema=output_schema,
            reasoning=reasoning,
            recording_enabled=recording_enabled,
            stealth=stealth,
            subagent_model=subagent_model,
            system_prompt=system_prompt,
            temperature=temperature,
            vision=vision,
            vpn_country=vpn_country,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    @overload
    async def run(
        self,
        *,
        device_id: str,
        task: str,
        accessibility: bool | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        continue_on_failure: bool | Omit = omit,
        credentials: Iterable[task_run_params.Credential] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        humanize: bool | Omit = omit,
        internal: bool | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: builtins.type[_ModelT],
        reasoning: bool | Omit = omit,
        recording_enabled: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        system_prompt: Optional[str] | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncTask[_ModelT]: ...

    @overload
    async def run(
        self,
        *,
        device_id: str,
        task: str,
        accessibility: bool | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        continue_on_failure: bool | Omit = omit,
        credentials: Iterable[task_run_params.Credential] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        humanize: bool | Omit = omit,
        internal: bool | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reasoning: bool | Omit = omit,
        recording_enabled: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        system_prompt: Optional[str] | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncTask[None]: ...

    async def run(
        self,
        *,
        device_id: str,
        task: str,
        accessibility: bool | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        continue_on_failure: bool | Omit = omit,
        credentials: Iterable[task_run_params.Credential] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        humanize: bool | Omit = omit,
        internal: bool | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Union[Optional[Dict[str, object]], builtins.type[BaseModel]] | Omit = omit,
        reasoning: bool | Omit = omit,
        recording_enabled: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        system_prompt: Optional[str] | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncTask[Any]:
        """Create and dispatch a new agent task.

        Returns the task ID and device stream
        details.

        Args:
          device_id: The ID of the device to run the task on.

          display_id: The display ID of the device to run the task on.

          execution_timeout: Maximum agent execution time in seconds (1–2700).

          humanize: Request human-like input where supported by the device. Replaces the deprecated
              stealth field; both must agree when supplied together.

          internal: Mark a task started by an agent or worker on the user's behalf. It is listed as
              source='agent' (excluded from source='api' lists) and its events carry
              internal=true so user-facing notifications and webhooks skip it. It is still
              billed, controllable and retrievable by id.

          llm_model: The LLM model identifier to use for the task (e.g.
              'mobilerun/mobile-agent-fast'). When omitted with reasoning=false, the fast-mode
              default model is used.

          recording_enabled: Record device video for the whole task and persist a retrievable reference

          stealth: Deprecated: use humanize. Both names must agree when supplied together.

          subagent_model: LLM model used by sub-agent roles: executor, app_opener, structured_output

          system_prompt: Optional custom behavioral overlay applied on top of the agent's default system
              prompts. Never echoed back in responses or errors.

          temperature: Deprecated and ignored. Sampling behavior is controlled by the model provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.tasks.run(
            device_id=device_id,
            task=task,
            accessibility=accessibility,
            apps=apps,
            continue_on_failure=continue_on_failure,
            credentials=credentials,
            display_id=display_id,
            execution_timeout=execution_timeout,
            files=files,
            humanize=humanize,
            internal=internal,
            llm_model=llm_model,
            max_steps=max_steps,
            output_schema=model_output_schema(output_schema),
            reasoning=reasoning,
            recording_enabled=recording_enabled,
            stealth=stealth,
            subagent_model=subagent_model,
            system_prompt=system_prompt,
            temperature=temperature,
            vision=vision,
            vpn_country=vpn_country,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return AsyncTask(self.api, result.id, result, output_parser=output_parser(output_schema), info_root="")


class AsyncTriggerManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncTrigger:
        return AsyncTrigger(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncTrigger:
        info = await self.api.workflows.triggers.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncTrigger(self.api, id, info, info_root="data")

    async def create(
        self,
        *,
        activation: Literal["event", "schedule", "custom"],
        name: str,
        conditions: trigger_create_params.Conditions | Omit = omit,
        custom_payload_schema: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        event_type: str | Omit = omit,
        payload: Dict[str, object] | Omit = omit,
        schedule_rule: trigger_create_params.ScheduleRule | Omit = omit,
        timezone: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncTrigger:
        """
        Create a trigger with an activation type of `event`, `schedule`, or `custom`.
        Each type requires its own fields (e.g. `eventType` and optional `conditions`
        for events, `scheduleRule` and `timezone` for schedules, `customPayloadSchema`
        for custom or schedule triggers); mismatched fields are rejected. Schedule
        triggers may store an optional JSON object `payload` (at most 1 MiB); it
        requires `customPayloadSchema`, is validated against it (422 on mismatch), and
        is available as `event.payload` on every scheduled, manual, or verification run.
        When a schema is configured, omitted payload values are validated as an empty
        object.

        Supports an optional `Idempotency-Key` header (1-255 printable ASCII
        characters). Replays with the same key and an identical body return the original
        201; a changed body under the same key returns 422 `idempotency_key_reused`.

        Args:
          custom_payload_schema: Optional JSON Schema for validating payloads for custom or schedule triggers

          payload: Stored input values for schedule triggers (maximum 1 MiB of JSON). Requires
              customPayloadSchema; available as event.payload on every run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.workflows.triggers.create(
            activation=activation,
            name=name,
            conditions=conditions,
            custom_payload_schema=custom_payload_schema,
            description=description,
            event_type=event_type,
            payload=payload,
            schedule_rule=schedule_rule,
            timezone=timezone,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncTrigger(self.api, info.data.id, info, owned=True, info_root="data")

        return object

    def list(
        self,
        *,
        activation: Literal["event", "schedule", "custom"] | Omit = omit,
        event_type: str | Omit = omit,
        order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncTrigger, TriggerListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncTrigger, TriggerListResponse]:
            __page = await self.api.workflows.triggers.list(
                activation=activation,
                event_type=event_type,
                order_by=order_by,
                order_by_direction=order_by_direction,
                page=page,
                page_size=page_size,
                search=search,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncTrigger(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


class AsyncCatalogEntryManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncCatalogEntry:
        return AsyncCatalogEntry(self.api, id)

    async def get(
        self,
        id: str,
        *,
        profile: Literal["agent_routine"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncCatalogEntry:
        info = await self.api.workflows.action_catalog.retrieve(
            id,
            profile=profile,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncCatalogEntry(self.api, id, info, info_root="data")

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        profile: Literal["agent_routine"] | Omit = omit,
        service: Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api"]
        | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncCatalogEntry, ActionCatalogListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncCatalogEntry, ActionCatalogListResponse]:
            __page = await self.api.workflows.action_catalog.list(
                page=page,
                page_size=page_size,
                profile=profile,
                service=service,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncCatalogEntry(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


class _AsyncWorkflowActionManagerServices:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceListResponse:
        """Return the names of the services that actions can be built against.

        Use these
        values to look up each service's allowed methods.
        """
        result = await self.api.workflows.actions.services.list(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def list_methods(
        self,
        service: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceListMethodsResponse:
        """
        Return the methods allowed for the given service, each with its parameter
        definitions (name, type, whether required, description, and optional
        default/example). Returns 404 if the service is unknown.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.workflows.actions.services.list_methods(
            service, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result


class AsyncWorkflowActionManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self.services = _AsyncWorkflowActionManagerServices(api)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncWorkflowAction:
        return AsyncWorkflowAction(self.api, id)

    async def get(
        self,
        id: str,
        *,
        profile: Literal["agent_routine"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncWorkflowAction:
        info = await self.api.workflows.actions.retrieve(
            id,
            profile=profile,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncWorkflowAction(self.api, id, info, info_root="data")

    async def create(
        self,
        *,
        catalog_entry_id: str,
        name: str,
        description: str | Omit = omit,
        params: Dict[str, object] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncWorkflowAction:
        """
        Create a reusable action from a catalog entry (`catalogEntryId`), with an
        optional `params` object supplying the values for that entry's service method.
        Returns 400 if the params are invalid for the chosen catalog entry.

        Supports an optional `Idempotency-Key` header (1-255 printable ASCII
        characters). Replays with the same key and an identical body return the original
        201; a changed body under the same key returns 422 `idempotency_key_reused`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.workflows.actions.create(
            catalog_entry_id=catalog_entry_id,
            name=name,
            description=description,
            params=params,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncWorkflowAction(self.api, info.data.id, info, owned=True, info_root="data")

        return object

    def list(
        self,
        *,
        order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        profile: Literal["agent_routine"] | Omit = omit,
        search: str | Omit = omit,
        service: Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api"]
        | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncWorkflowAction, WorkflowsActionListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncWorkflowAction, WorkflowsActionListResponse]:
            __page = await self.api.workflows.actions.list(
                order_by=order_by,
                order_by_direction=order_by_direction,
                page=page,
                page_size=page_size,
                profile=profile,
                search=search,
                service=service,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncWorkflowAction(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


class AsyncFlowManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncFlow:
        return AsyncFlow(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncFlow:
        info = await self.api.workflows.flows.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncFlow(self.api, id, info, info_root="data")

    async def create(
        self,
        *,
        actions: Iterable[flow_create_params.Action],
        name: str,
        trigger_id: str,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        delivery: flow_create_params.Delivery | Omit = omit,
        description: str | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        health_monitoring_enabled: bool | Omit = omit,
        notify_on_failure: bool | Omit = omit,
        notify_on_success: bool | Omit = omit,
        notify_webhook_id: Optional[str] | Omit = omit,
        owner_wake: Literal["final", "off"] | Omit = omit,
        recording_enabled: bool | Omit = omit,
        recording_policy: flow_create_params.RecordingPolicy | Omit = omit,
        self_healing_enabled: bool | Omit = omit,
        self_healing_max_attempts: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncFlow:
        """
        Create a flow that binds a trigger (`triggerId`) to an ordered list of actions,
        with at least one action required. Optional settings include target `deviceIds`,
        a cooldown (`cooldownSeconds`/`cooldownScope`), and webhook notifications on
        success or failure.

        Supports an optional `Idempotency-Key` header (1-255 printable ASCII
        characters). Replays with the same key and an identical body return the original
        201; a changed body under the same key returns 422 `idempotency_key_reused`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.workflows.flows.create(
            actions=actions,
            name=name,
            trigger_id=trigger_id,
            cooldown_scope=cooldown_scope,
            cooldown_seconds=cooldown_seconds,
            delivery=delivery,
            description=description,
            device_ids=device_ids,
            enabled=enabled,
            health_monitoring_enabled=health_monitoring_enabled,
            notify_on_failure=notify_on_failure,
            notify_on_success=notify_on_success,
            notify_webhook_id=notify_webhook_id,
            owner_wake=owner_wake,
            recording_enabled=recording_enabled,
            recording_policy=recording_policy,
            self_healing_enabled=self_healing_enabled,
            self_healing_max_attempts=self_healing_max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncFlow(self.api, info.data.id, info, owned=True, info_root="data")

        return object

    def list(
        self,
        *,
        agent_id: Union[str, Literal["unassigned"]] | Omit = omit,
        created_by: str | Omit = omit,
        enabled: Literal["true", "false"] | Omit = omit,
        mine: Literal["true", "false"] | Omit = omit,
        order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: List[Literal["healthy", "failing", "blocked"]] | Omit = omit,
        trigger_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncFlow, FlowListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncFlow, FlowListResponse]:
            __page = await self.api.workflows.flows.list(
                agent_id=agent_id,
                created_by=created_by,
                enabled=enabled,
                mine=mine,
                order_by=order_by,
                order_by_direction=order_by_direction,
                page=page,
                page_size=page_size,
                search=search,
                status=status,
                trigger_id=trigger_id,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncFlow(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    async def capacity(
        self,
        *,
        agent_id: Union[str, Literal["unassigned"]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowCapacityResponse:
        """
        Returns the environment routine limit and remaining capacity for this owner and
        agent bucket, counting enabled and disabled non-deleted flows. Omit agentId (or
        use unassigned) for the unassigned bucket. This is advisory; create and clone
        enforce admission under a bucket lock.

        Args:
          agent_id: Agent bucket UUID or unassigned. Omit on list to include every bucket; omit on
              capacity for unassigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.workflows.flows.capacity(
            agent_id=agent_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def template_context(
        self,
        *,
        template_resolution_version: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowTemplateContextResponse:
        """
        Get flow template context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.workflows.flows.template_context(
            template_resolution_version=template_resolution_version,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    @overload
    async def validate(
        self,
        *,
        actions: Iterable[flow_validate_params.Variant0Action],
        name: str,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        delivery: flow_validate_params.Variant0Delivery | Omit = omit,
        description: str | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        health_monitoring_enabled: bool | Omit = omit,
        notify_on_failure: bool | Omit = omit,
        notify_on_success: bool | Omit = omit,
        notify_webhook_id: Optional[str] | Omit = omit,
        owner_wake: Literal["final", "off"] | Omit = omit,
        recording_enabled: bool | Omit = omit,
        recording_policy: flow_validate_params.Variant0RecordingPolicy | Omit = omit,
        self_healing_enabled: bool | Omit = omit,
        self_healing_max_attempts: int | Omit = omit,
        trigger_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowValidateResponse: ...

    @overload
    async def validate(
        self,
        *,
        draft: flow_validate_params.Variant1Draft,
        agent_id: str | Omit = omit,
        contract: flow_validate_params.Variant1Contract | Omit = omit,
        verify: flow_validate_params.Variant1Verify | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowValidateResponse: ...

    async def validate(
        self,
        *,
        actions: Iterable[flow_validate_params.Variant0Action] | Omit = omit,
        name: str | Omit = omit,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        delivery: flow_validate_params.Variant0Delivery | Omit = omit,
        description: str | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        health_monitoring_enabled: bool | Omit = omit,
        notify_on_failure: bool | Omit = omit,
        notify_on_success: bool | Omit = omit,
        notify_webhook_id: Optional[str] | Omit = omit,
        owner_wake: Literal["final", "off"] | Omit = omit,
        recording_enabled: bool | Omit = omit,
        recording_policy: flow_validate_params.Variant0RecordingPolicy | Omit = omit,
        self_healing_enabled: bool | Omit = omit,
        self_healing_max_attempts: int | Omit = omit,
        trigger_id: str | Omit = omit,
        draft: flow_validate_params.Variant1Draft | Omit = omit,
        agent_id: str | Omit = omit,
        contract: flow_validate_params.Variant1Contract | Omit = omit,
        verify: flow_validate_params.Variant1Verify | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowValidateResponse:
        """
        Validate a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await cast(Callable[..., Awaitable[FlowValidateResponse]], self.api.workflows.flows.validate)(
            actions=actions,
            name=name,
            cooldown_scope=cooldown_scope,
            cooldown_seconds=cooldown_seconds,
            delivery=delivery,
            description=description,
            device_ids=device_ids,
            enabled=enabled,
            health_monitoring_enabled=health_monitoring_enabled,
            notify_on_failure=notify_on_failure,
            notify_on_success=notify_on_success,
            notify_webhook_id=notify_webhook_id,
            owner_wake=owner_wake,
            recording_enabled=recording_enabled,
            recording_policy=recording_policy,
            self_healing_enabled=self_healing_enabled,
            self_healing_max_attempts=self_healing_max_attempts,
            trigger_id=trigger_id,
            draft=draft,
            agent_id=agent_id,
            contract=contract,
            verify=verify,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result


class AsyncExecutionManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncExecution:
        return AsyncExecution(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncExecution:
        info = await self.api.workflows.executions.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncExecution(self.api, id, info, info_root="data")

    def list(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        invocation_id: str | Omit = omit,
        order_by: Literal["startedAt", "finishedAt", "status"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        trigger_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncExecution, ExecutionListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncExecution, ExecutionListResponse]:
            __page = await self.api.workflows.executions.list(
                flow_id=flow_id,
                from_=from_,
                invocation_id=invocation_id,
                order_by=order_by,
                order_by_direction=order_by_direction,
                page=page,
                page_size=page_size,
                search=search,
                status=status,
                to=to,
                trigger_id=trigger_id,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncExecution(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    async def get_metrics(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        trigger_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionGetMetricsResponse:
        """
        Return aggregate execution metrics — total count, counts by status, average
        duration, and the last execution time. Can be scoped by `flowId`, `triggerId`,
        and a `from`/`to` time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.workflows.executions.get_metrics(
            flow_id=flow_id,
            from_=from_,
            to=to,
            trigger_id=trigger_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result


class _AsyncWebhookManagerIntegrations:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListResponse:
        """
        Returns the integrations that can receive webhook events as channel messages
        (e.g. Slack), with your org's connection state for each. Connect an integration
        in the Cloud app before creating a webhook for it.
        """
        result = await self.api.webhooks.integrations.list(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def list_targets(
        self,
        capability_id: str,
        *,
        revision: int,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListTargetsResponse:
        """Returns the live list of targets (e.g.

        Slack channels the connected account is a
        member of) for an integration. Pass a target's `args` together with the
        integration `capability` to `POST /webhooks` with `kind: "integration"`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.webhooks.integrations.list_targets(
            capability_id,
            revision=revision,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result


class AsyncWebhookManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self.integrations = _AsyncWebhookManagerIntegrations(api)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncWebhook:
        return AsyncWebhook(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncWebhook:
        info = await self.api.webhooks.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncWebhook(self.api, id, info, info_root="data")

    async def create(
        self,
        *,
        url: str | Omit = omit,
        description: str | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        kind: Literal["http"] | Literal["integration"] | Omit = omit,
        args: Dict[str, object] | Omit = omit,
        capability: webhook_create_params.Variant1Capability | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncWebhook:
        """
        Creates a webhook subscription and an optional list of event types to subscribe
        to (defaults to all when omitted). `kind: "http"` (the default) delivers signed
        JSON to a URL; the response includes the generated signing secret, which is
        returned only once at creation time and cannot be retrieved later.
        `kind: "integration"` posts each event as a message into a connected integration
        target (e.g. a Slack channel): pick the `capability` from
        `GET /webhooks/integrations` and the `args` from
        `GET /webhooks/integrations/{capabilityId}/targets`. Integration webhooks have
        no signing secret. Send an `Idempotency-Key` header to make the create safe to
        retry: the same key with the same body returns the existing webhook (status 201,
        `Idempotent-Replayed: true`) instead of creating a second one, and the same key
        with a different body is a 422. A replayed create does not return the signing
        secret again; use rotate-secret if the original response was lost. If that
        webhook was deleted in the meantime, the retry is a 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await cast(Callable[..., Awaitable[WebhookCreateResponse]], self.api.webhooks.create)(
            url=url,
            description=description,
            event_types=event_types,
            kind=kind,
            args=args,
            capability=capability,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncWebhook(self.api, info.data.id, info, owned=True, info_root="data")

        return object

    def list(
        self,
        *,
        created_by: str | Omit = omit,
        kind: Literal["http", "integration"] | Omit = omit,
        mine: Literal["true", "false"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["active", "failing", "blocked", "disabled"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncWebhook, WebhookListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncWebhook, WebhookListResponse]:
            __page = await self.api.webhooks.list(
                created_by=created_by,
                kind=kind,
                mine=mine,
                page=page,
                page_size=page_size,
                search=search,
                status=status,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncWebhook(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    def verify(
        self, body: str | bytes, headers: Any, secret: str, *, tolerance: float = 300, now: float | None = None
    ) -> Any:
        return verify_webhook(body, headers, secret, tolerance=tolerance, now=now)


class AsyncWebhookDeliveryManager:
    def __init__(self, api: AsyncMobilerun, webhook_id: str) -> None:
        self.api = api
        self._webhook_id = webhook_id

    @property
    def webhook_id(self) -> str:
        return self._webhook_id

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncWebhookDelivery:
        return AsyncWebhookDelivery(self.api, self.webhook_id, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncWebhookDelivery:
        info = await self.api.webhooks.deliveries.retrieve_attempts(
            id,
            id=self.webhook_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncWebhookDelivery(self.api, self.webhook_id, id, info, info_root="data")

    def list(
        self,
        *,
        event_id: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncWebhookDelivery, DeliveryListForWebhookResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncWebhookDelivery, DeliveryListForWebhookResponse]:
            __page = await self.api.webhooks.deliveries.list_for_webhook(
                self.webhook_id,
                event_id=event_id,
                page=page,
                page_size=page_size,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [
                    AsyncWebhookDelivery(self.api, self.webhook_id, item.id, item, info_root="")
                    for item in (__page.items or [])
                ],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


class AsyncMailboxManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self.connections = AsyncMailboxConnectionManager(api)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncMailbox:
        return AsyncMailbox(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncMailbox:
        info = await self.api.mailboxes.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncMailbox(self.api, id, info, info_root="data")

    async def create(
        self,
        *,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        domain_id: str | Omit = omit,
        label: str | Omit = omit,
        local_part: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncMailbox:
        """Claims or rents a mailbox.

        Included capacity may apply; paid rentals may require checkout.


        Creates a mailbox on the default domain or a connected custom domain.

        An
        optional `localPart` selects the address. Replaying the same Idempotency-Key and
        payload returns the original mailbox. Fresh requests and replays return 202 with
        the current mailbox state. Poll the mailbox when the response does not yet
        include a checkout URL.

        Args:
          billing_preference: included uses package capacity when available and otherwise starts paid
              checkout; included_only fails without creating a paid reservation when no
              included slot remains; rent always starts paid checkout.

          domain_id: Optional active custom mailbox domain owned by the caller. Omit to use the
              system domain.

          local_part: Optional mailbox name before the "@". Omit to generate a random address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.mailboxes.create(
            billing_preference=billing_preference,
            domain_id=domain_id,
            label=label,
            local_part=local_part,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncMailbox(self.api, info.data.id, info, owned=True, info_root="data")

        return object

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncMailbox, MailboxListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncMailbox, MailboxListResponse]:
            __page = await self.api.mailboxes.list(
                page=page,
                page_size=page_size,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncMailbox(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    async def capacity(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxCapacityResponse:
        """Returns the number of mailboxes currently available through included capacity."""
        result = await self.api.mailboxes.capacity(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result


class AsyncMailboxConnectionManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncMailboxConnection:
        return AsyncMailboxConnection(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncMailboxConnection:
        info = await self.api.mailboxes.connections.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncMailboxConnection(self.api, id, info, info_root="")

    async def create(
        self,
        *,
        provider: Literal["gmail"],
        binding_hash: str | Omit = omit,
        label: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncMailboxConnection:
        """Links the caller’s Gmail account.

        Replaying the same Idempotency-Key returns the
        same mailbox. When Gmail is already active, redirectUrl is null and the mailbox
        is usable immediately.

        Args:
          binding_hash: sha256 hex of the browser-held connect binding secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.mailboxes.connections.create(
            provider=provider,
            binding_hash=binding_hash,
            label=label,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncMailboxConnection(self.api, info.connection_id, info, owned=True, info_root="")

        return object


class AsyncMailboxMessageManager:
    def __init__(self, api: AsyncMobilerun, mailbox_id: str) -> None:
        self.api = api
        self._mailbox_id = mailbox_id

    @property
    def mailbox_id(self) -> str:
        return self._mailbox_id

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncMailboxMessage:
        return AsyncMailboxMessage(self.api, self.mailbox_id, id)

    async def get(
        self,
        id: str,
        *,
        include_html: Literal["true", "false"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncMailboxMessage:
        info = await self.api.mailboxes.messages.retrieve(
            id,
            mailbox_id=self.mailbox_id,
            include_html=include_html,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncMailboxMessage(self.api, self.mailbox_id, id, info, info_root="data")

    def list(
        self,
        *,
        after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        has_otp: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        sender: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncMailboxMessage, MailboxesMessageListResponse]:
        async def load(
            __number: int | str | None, visited: set[str] | None = None
        ) -> AsyncObjectPage[AsyncMailboxMessage, MailboxesMessageListResponse]:
            seen = set(visited or ())
            if isinstance(__number, str):
                seen.add(__number)
            __page = await self.api.mailboxes.messages.list(
                self.mailbox_id,
                after=after,
                cursor=cursor,
                has_otp=has_otp,
                limit=limit,
                sender=sender,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"cursor": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [
                    AsyncMailboxMessage(self.api, self.mailbox_id, item.id, item, info_root="")
                    for item in (__page.items or [])
                ],
                __page,
                lambda: next_object_cursor(__page.next_cursor, __number, seen),
                lambda token: load(token, seen),
            )

        return AsyncObjectPager(lambda: load(cursor if isinstance(cursor, str) else None))


class AsyncAgentFileManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncAgentFile:
        return AsyncAgentFile(self.api, id)

    def list(
        self,
        *,
        zone: Literal["user", "agent", "workflow", "skills"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncAgentFile, TypesFileListResponse]:
        async def load() -> AsyncObjectPage[AsyncAgentFile, TypesFileListResponse]:
            __page = await self.api.files.list(
                zone=zone, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            )
            return AsyncObjectPage(
                [AsyncAgentFile(self.api, item.file_id, item, info_root="") for item in (__page.files or [])], __page
            )

        return AsyncObjectPager(load)

    async def upload_url(
        self,
        *,
        filename: str,
        mime_type: str,
        size_bytes: int,
        chat_session_id: str | Omit = omit,
        zone: Literal["user", "skills"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FileUploadURLResponse:
        """
        Mint a presigned PUT URL and a fileId for uploading a user file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.files.upload_url(
            filename=filename,
            mime_type=mime_type,
            size_bytes=size_bytes,
            chat_session_id=chat_session_id,
            zone=zone,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def upload(
        self,
        *,
        file: UploadInput,
        filename: str | None = None,
        mime_type: str | None = None,
        size_bytes: int | None = None,
        chat_session_id: str | Omit = omit,
        zone: Literal["user", "skills"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncAgentFile:
        """Upload to presigned storage, confirm, and return the object. Uses storage quota."""
        prepared = [prepare_upload(file, filename=filename, content_type=mime_type, size=size_bytes)]
        if not prepared or len({file.filename for file in prepared}) != len(prepared):
            raise TypeError("Upload needs unique, nonempty file names")
        issued = await self.api.files.upload_url(
            filename=prepared[0].filename,
            mime_type=prepared[0].content_type,
            size_bytes=prepared[0].size,
            chat_session_id=chat_session_id,
            zone=zone,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=bound_extra(
                extra_body,
                {"filename": prepared[0].filename, "mimeType": prepared[0].content_type, "sizeBytes": prepared[0].size},
            ),
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        confirmed = False
        confirming = False
        try:
            urls = upload_urls(
                issued,
                prepared,
                {
                    "request": "upload_url",
                    "url_path": "putUrl",
                    "name_param": "filename",
                    "mime_param": "mimeType",
                    "size_param": "sizeBytes",
                    "id_path": "fileId",
                    "confirm": "confirm",
                    "fail": "cancel_pending",
                    "returns": "AgentFile",
                },
            )
            for prepared_file, url in zip(prepared, urls, strict=True):
                await put_upload_async(self.api, prepared_file, url, timeout=timeout)
            confirming = True
            info = await self.api.files.confirm(
                issued.file_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            )
            confirmed = True
            return AsyncAgentFile(self.api, info.file_id, info, info_root="")
        except BaseException as error:
            if not confirmed and (not confirming or definite_confirm_failure(error)):
                try:
                    with anyio.CancelScope(shield=True):
                        with anyio.move_on_after(10):
                            await self.api.files.cancel_pending(
                                issued.file_id,
                                extra_headers=extra_headers,
                                extra_query=extra_query,
                                extra_body=extra_body,
                                timeout=timeout,
                                idempotency_key=idempotency_key,
                            )
                except BaseException:
                    pass
            if not isinstance(error, Exception):
                raise
            raise UploadError() from error


class AsyncAgentManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self.requests = AsyncAgentRequestManager(api)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncAgent:
        return AsyncAgent(self.api, id)

    async def create(
        self,
        *,
        display_name: str,
        avatar_seed: Union[str, int] | Omit = omit,
        color: Literal[
            "slate", "red", "orange", "amber", "lime", "green", "teal", "cyan", "blue", "indigo", "violet", "pink"
        ]
        | Omit = omit,
        instructions: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncAgent:
        """
        Creates an Agent directly on the owner runtime, without a chat message or
        approval card. Provisioning runs in the background; the new Agent has no chat
        history. Requires Idempotency-Key; a replay returns the current Agent with the
        original 201 status.

        Args:
          display_name: Single-line name shown for the Agent; surrounding whitespace is trimmed and it
              needs at least one letter or number.

          instructions: The Agent's individual instructions passage; an empty or whitespace-only text
              clears it. Line breaks count three characters toward the rendered size limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.agents.create(
            display_name=display_name,
            avatar_seed=avatar_seed,
            color=color,
            instructions=instructions,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncAgent(self.api, info.agent.id, info, owned=True, info_root="agent")

        return object

    def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncAgent, AgentListResponse]:
        async def load() -> AsyncObjectPage[AsyncAgent, AgentListResponse]:
            __page = await self.api.agents.list(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            )
            return AsyncObjectPage(
                [AsyncAgent(self.api, item.id, item, info_root="") for item in (__page.agents or [])], __page
            )

        return AsyncObjectPager(load)

    async def model_profiles(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentModelProfilesResponse:
        """List the environment model profiles and their default.

        Model routing is managed
        by the server.
        """
        result = await self.api.agents.model_profiles(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result


class AsyncAgentRequestManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncAgentRequest:
        return AsyncAgentRequest(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncAgentRequest:
        info = await self.api.agents.requests.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncAgentRequest(self.api, id, info, info_root="")

    def list(
        self,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncAgentRequest, RequestListResponse]:
        async def load() -> AsyncObjectPage[AsyncAgentRequest, RequestListResponse]:
            __page = await self.api.agents.requests.list(
                before=before,
                limit=limit,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncAgentRequest(self.api, item.id, item, info_root="") for item in (__page.requests or [])], __page
            )

        return AsyncObjectPager(load)

    async def list_for_agent(
        self,
        agent_id: str,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestListForAgentResponse:
        """Owner-scoped.

        Returns newest requests where the Agent is source or target. Use
        nextCursor as before to read older pages. Invalid cursors return 400
        invalid_cursor.

        Args:
          before: Opaque nextCursor from the previous page.

          limit: Maximum number of requests to return (1–100; default 50).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.agents.requests.list_for_agent(
            agent_id,
            before=before,
            limit=limit,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def retrieve_by_session(
        self,
        session_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncAgentRequest:
        """Owner-scoped.

        Returns the Agent-to-Agent request whose target session is
        {sessionId}, including its payloads and event timeline. Unknown sessions,
        source-only sessions, sessions without a request, and another owner's sessions
        return 404 agent_request_not_found.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.agents.requests.retrieve_by_session(
            session_id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncAgentRequest(self.api, result.id, result, info_root="")


class _AsyncNumberMessageManagerConversations:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        cursor_last_message_id: str | Omit = omit,
        cursor_last_occurred_at: Union[str, datetime] | Omit = omit,
        esim_id: str | Omit = omit,
        limit: int | Omit = omit,
        number_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagesConversationListResponse:
        """Lists SMS conversations by recent activity.

        Use both cursor fields from
        `nextCursor` to fetch the next page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.messages.conversations.list(
            cursor_last_message_id=cursor_last_message_id,
            cursor_last_occurred_at=cursor_last_occurred_at,
            esim_id=esim_id,
            limit=limit,
            number_id=number_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def mark_read(
        self,
        *,
        peer_key: str,
        up_to_message_id: str,
        up_to_occurred_at: Union[str, datetime],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ConversationMarkReadResponse:
        """
        Marks inbound messages in a conversation as read through the supplied cursor.
        Repeating the request is safe.

        Args:
          peer_key: The thread's canonical peer key (see GET .../conversations)

          up_to_occurred_at: Mark inbound messages read up to (and including) this occurredAt/upToMessageId
              cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.messages.conversations.mark_read(
            peer_key=peer_key,
            up_to_message_id=up_to_message_id,
            up_to_occurred_at=up_to_occurred_at,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result


class AsyncNumberMessageManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api
        self.conversations = _AsyncNumberMessageManagerConversations(api)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncNumberMessage:
        return AsyncNumberMessage(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncNumberMessage:
        info = await self.api.messages.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncNumberMessage(self.api, id, info, info_root="data")

    def list(
        self,
        *,
        direction: Literal["all", "inbound", "outbound"] | Omit = omit,
        esim_id: str | Omit = omit,
        number_id: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        peer_key: str | Omit = omit,
        peer_number: str | Omit = omit,
        status: Literal[
            "all", "received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"
        ]
        | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncNumberMessage, TypesMessageListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncNumberMessage, TypesMessageListResponse]:
            __page = await self.api.messages.list(
                direction=direction,
                esim_id=esim_id,
                number_id=number_id,
                page=page,
                page_size=page_size,
                peer_key=peer_key,
                peer_number=peer_number,
                status=status,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncNumberMessage(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


class AsyncPhoneNumberManager:
    def __init__(self, api: AsyncMobilerun) -> None:
        self.api = api

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def from_id(self, id: str) -> AsyncPhoneNumber:
        return AsyncPhoneNumber(self.api, id)

    async def get(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPhoneNumber:
        info = await self.api.numbers.retrieve(
            id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return AsyncPhoneNumber(self.api, id, info, info_root="data")

    async def create(
        self,
        *,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        country: str | Omit = omit,
        label: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncPhoneNumber:
        """Purchases a phone number. Poll the returned number for status updates.

        Starts a phone-number purchase.

        Poll the returned phone number for status
        updates.

        Args:
          billing_preference: Use included capacity when available, require included capacity without paid
              fallback (included_only), or start a paid checkout (rent).

          country: Optional ISO 3166-1 alpha-2 country code from GET /numbers/phones/countries.

          label: User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
              code units; an emoji/flag may span several). Display-only, never used for
              routing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        info = await self.api.numbers.create(
            billing_preference=billing_preference,
            country=country,
            label=label,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        object = AsyncPhoneNumber(self.api, info.data.number_id, info, owned=True, info_root="data")

        return object

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncPhoneNumber, NumberListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncPhoneNumber, NumberListResponse]:
            __page = await self.api.numbers.list(
                page=page,
                page_size=page_size,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncPhoneNumber(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))

    async def capacity(
        self,
        *,
        country: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberCapacityResponse:
        """Returns included phone capacity for a country.

        Creating a phone is
        authoritative.

        Args:
          country: ISO 3166-1 alpha-2 country code from GET /numbers/phones/countries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.numbers.capacity(
            country=country,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def countries(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberCountriesResponse:
        """Lists available countries and current phone-number availability."""
        result = await self.api.numbers.countries(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result


AsyncAppInfo = Union[AppRetrieveResponse, __types_app_list_response.Item]


class AsyncApp:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncAppInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncAppInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", display_name={self.display_name!r}, platform={self.platform!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppRetrieveResponse:
        result = await self.api.apps.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def display_name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "displayName"))

    @property
    def platform(self) -> Union[Literal["android", "ios"], None]:
        """Reads the last response without making a request."""
        return cast(Union[Literal["android", "ios"], None], record_field(self.info, self._info_root, "platform"))

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AppDeleteResponse:
        """Deletes an uploaded app by ID. Removes its files and metadata."""
        result = await self.api.apps.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def list_versions(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppListVersionsResponse:
        """
        Retrieves all versions of an app visible to the user (own uploads + system
        versions)
        """
        result = await self.api.apps.list_versions(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def __aenter__(self) -> AsyncApp:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


class _AsyncCredentialPackageLinks:
    def __init__(self, api: AsyncMobilerun, owner: AsyncCredentialPackage) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def create(
        self,
        *,
        credential_name: str,
        field_map: Iterable[link_create_params.FieldMap],
        item_id: str,
        vault_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
        """
        Link a 1Password item to a credential

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.credentials.packages.links.create(
            self._owner.id,
            credential_name=credential_name,
            field_map=field_map,
            item_id=item_id,
            vault_id=vault_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result


AsyncCredentialPackageInfo = Union[
    PackageCreateResponse, CredentialsPackageListResponse, __types_credentials_package_list_all_response.Data
]


class AsyncCredentialPackage:
    "A package identified by its name. get preserves the credentials-array response in info."

    def __init__(
        self, api: AsyncMobilerun, id: str, info: Optional[AsyncCredentialPackageInfo] = None, *, owned: bool = False
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncCredentialPackageInfo] = info
        self._owned = owned
        owner = self
        self.credentials = AsyncCredentialManager(api, owner.id)
        self.links = _AsyncCredentialPackageLinks(api, owner)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialsPackageListResponse:
        result = await self.api.credentials.packages.list(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        return result

    async def __aenter__(self) -> AsyncCredentialPackage:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


class _AsyncCredentialFields:
    def __init__(self, api: AsyncMobilerun, owner: AsyncCredential) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def create(
        self,
        *,
        field_type: Literal[
            "email", "username", "password", "api_token", "phone_number", "two_factor_secret", "backup_codes"
        ],
        value: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FieldCreateResponse:
        """Adds a single field to an existing credential.

        The body specifies a `fieldType`
        (one of the supported field types) and its value. Returns a conflict if a field
        of that type already exists on the credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.credentials.packages.credentials.fields.create(
            self._owner.id,
            package_name=self._owner.package_name,
            field_type=field_type,
            value=value,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def update(
        self,
        field_type: Literal[
            "email", "username", "password", "api_token", "phone_number", "two_factor_secret", "backup_codes"
        ],
        *,
        value: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FieldUpdateResponse:
        """
        Updates the value of an existing field on a credential, identified by
        `packageName`, `credentialName`, and `fieldType` in the path. The body carries
        the new value and returns the updated credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.credentials.packages.credentials.fields.update(
            field_type,
            package_name=self._owner.package_name,
            credential_name=self._owner.id,
            value=value,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        field_type: Literal[
            "email", "username", "password", "api_token", "phone_number", "two_factor_secret", "backup_codes"
        ],
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FieldDeleteResponse:
        """
        Removes a single field of the given `fieldType` from the specified credential
        while leaving the credential itself intact. Returns the updated credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.credentials.packages.credentials.fields.delete(
            field_type,
            package_name=self._owner.package_name,
            credential_name=self._owner.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result


AsyncCredentialInfo = Union[CredentialCreateResponse, __types_credentials_package_list_response.Data]


class AsyncCredential:
    def __init__(
        self,
        api: AsyncMobilerun,
        package_name: str,
        id: str,
        info: Optional[AsyncCredentialInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self._package_name = package_name
        self.info: Optional[AsyncCredentialInfo] = info
        self._info_root = info_root
        self._owned = owned
        owner = self
        self.fields = _AsyncCredentialFields(api, owner)

    @override
    def __repr__(self) -> str:
        fields = f", source={self.source!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    @property
    def package_name(self) -> str:
        return self._package_name

    @property
    def source(self) -> Union[Literal["mobilerun", "onepassword"], None]:
        """Reads only the last create/list snapshot without making a request; fromId/from_id handles have no data."""
        return cast(
            Union[Literal["mobilerun", "onepassword"], None], record_field(self.info, self._info_root, "source")
        )

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CredentialDeleteResponse:
        """
        Permanently deletes the credential identified by `packageName` and
        `credentialName`, removing all of its fields. Returns the deleted credential.
        """
        result = await self.api.credentials.packages.credentials.delete(
            self.id,
            package_name=self.package_name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def __aenter__(self) -> AsyncCredential:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


class _AsyncDeviceActions:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def global_(
        self,
        *,
        action: int,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Performs a global system action on the device, such as navigating back or going
        to the home screen, identified by an action code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.actions.global_(
            self._owner.id,
            action=action,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def overlay_visible(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionOverlayVisibleResponse:
        """
        Returns whether the accessibility overlay is currently visible on the device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.actions.overlay_visible(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def set_overlay_visible(
        self,
        *,
        visible: bool,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Shows or hides the accessibility overlay on the device based on the visibility
        flag in the request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.actions.set_overlay_visible(
            self._owner.id,
            visible=visible,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceApps:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        include_protected_apps: bool | Omit = omit,
        include_system_apps: bool | Omit = omit,
        include_updates: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DevicesAppListResponse]:
        """
        Returns detailed information about apps installed on the device, including
        package name and label. System and protected apps are excluded unless the
        corresponding query parameters are set.

        Args:
          include_updates: Resolve availableUpdate for Android user apps (one library lookup per app). Off
              by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.apps.list(
            self._owner.id,
            include_protected_apps=include_protected_apps,
            include_system_apps=include_system_apps,
            include_updates=include_updates,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def delete(
        self,
        package_name: str,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Uninstalls the app identified by the path package name from the device.
        Protected packages cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.apps.delete(
            package_name,
            device_id=self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def grant_permission(
        self,
        permission: Literal["POST_NOTIFICATIONS"],
        *,
        package_name: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Grants an Android runtime permission to the package named in the path.

        The
        permission is given by its short name (e.g. POST_NOTIFICATIONS).

        Args:
          permission: Android runtime permission, short name (e.g. POST_NOTIFICATIONS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.apps.grant_permission(
            permission,
            device_id=self._owner.id,
            package_name=package_name,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    @overload
    async def install(
        self,
        *,
        bundle_id: str,
        background: bool | Omit = omit,
        country: str | Omit = omit,
        package_name: str | Omit = omit,
        version_code: int | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None: ...

    @overload
    async def install(
        self,
        *,
        package_name: str,
        background: bool | Omit = omit,
        bundle_id: str | Omit = omit,
        country: str | Omit = omit,
        version_code: int | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None: ...

    async def install(
        self,
        *,
        bundle_id: str | Omit = omit,
        background: bool | Omit = omit,
        country: str | Omit = omit,
        package_name: str | Omit = omit,
        version_code: int | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Requests an app install on the device.

        The request body must supply exactly one
        of an Android packageName or an iOS bundleId. For packageName installs, optional
        country and versionCode select an exact regional uploaded Android version, and
        protected packages are rejected. background (default false) selects the response
        contract: false installs inline and returns the outcome directly (200 on
        success, an error status on failure); true accepts the request and runs the
        download + install in the background, returning 202 immediately — poll
        list-app-installs for the backend's view of that attempt's status. Refuses with
        409 once 2 other installs are already running on the device, in either mode; a
        repeat request for an app that already has an install running is also refused
        with 409 rather than superseding it — retry once that attempt reaches a terminal
        state. Synchronous failures report APP_DOWNLOAD_FAILED (502) when the app file
        cannot be downloaded or APP_INSTALL_TIMEOUT (504) when the install times out.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await cast(Callable[..., Awaitable[None]], self.api.devices.apps.install)(
            self._owner.id,
            bundle_id=bundle_id,
            background=background,
            country=country,
            package_name=package_name,
            version_code=version_code,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def list_installs(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppListInstallsResponse:
        """
        Reports the backend's durable view of background app-install attempts on this
        device — status reflects the install ATTEMPT, not device ground truth; list-apps
        remains authoritative for what is actually installed. Terminal and projected
        timeout records are kept ~15 minutes. Not gated on device readiness, so it also
        answers while the device is offline or crashed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.apps.list_installs(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def revoke_permission(
        self,
        permission: Literal["POST_NOTIFICATIONS"],
        *,
        package_name: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Revokes an Android runtime permission from the package named in the path.

        The
        permission is given by its short name (e.g. POST_NOTIFICATIONS).

        Args:
          permission: Android runtime permission, short name (e.g. POST_NOTIFICATIONS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.apps.revoke_permission(
            permission,
            device_id=self._owner.id,
            package_name=package_name,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceEsimApn:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApnListResponse]:
        """
        Returns the access point names (APNs) configured for the device's active eSIM
        subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.esim.apn.list(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def select(
        self,
        *,
        apn_id: int,
        sub_id: int,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Marks an existing APN, identified by apnId, as the preferred APN for the given
        eSIM subscription in the request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.esim.apn.select(
            self._owner.id,
            apn_id=apn_id,
            sub_id=sub_id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def set(
        self,
        *,
        apn: str,
        mcc: str,
        mnc: str,
        name: str,
        protocol: str,
        roaming_protocol: str,
        sub_id: int,
        type: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Creates an access point name (APN) from the request body and applies it to the
        given eSIM subscription. Type, protocol, and roaming protocol default to common
        values when omitted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.esim.apn.set(
            self._owner.id,
            apn=apn,
            mcc=mcc,
            mnc=mnc,
            name=name,
            protocol=protocol,
            roaming_protocol=roaming_protocol,
            sub_id=sub_id,
            type=type,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceEsim:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner
        self.apn = _AsyncDeviceEsimApn(api, owner)

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[EsimListResponse]:
        """
        Returns the eSIM subscriptions currently provisioned on the device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.esim.list(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def activate(
        self,
        *,
        enable: bool,
        sm_dp_addr: str,
        confirmation_code: str | Omit = omit,
        matching_id: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EsimActivateResponse:
        """
        Download profile and/or enable subscription.

        Args:
          confirmation_code: Optional carrier-issued confirmation code (the 4th LPA segment). Required only
              for plans whose SM-DP+ challenges the device for one. Requires matchingId — the
              LPA spec only interprets segment 4 when segment 3 is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.devices.esim.activate(
            self._owner.id,
            enable=enable,
            sm_dp_addr=sm_dp_addr,
            confirmation_code=confirmation_code,
            matching_id=matching_id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def enable(
        self,
        *,
        sub_id: int,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Enables the eSIM subscription identified by the subId in the request body so it
        becomes the active subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.esim.enable(
            self._owner.id,
            sub_id=sub_id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def remove(
        self,
        *,
        sub_id: int,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes the eSIM subscription identified by the subId query parameter from the
        device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.esim.remove(
            self._owner.id,
            sub_id=sub_id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def set_roaming(
        self,
        *,
        enabled: bool,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Enables or disables data roaming for the device's eSIM based on the enabled flag
        in the request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.esim.set_roaming(
            self._owner.id,
            enabled=enabled,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def status(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[EsimStatusResponse]:
        """
        Returns the connectivity status of the device's eSIM subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.esim.status(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result


class _AsyncDeviceFiles:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        path: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DevicesFileListResponse:
        """
        Lists the files at the directory path given in the path query parameter,
        returning each entry's metadata along with the path and total count.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.files.list(
            self._owner.id,
            path=path,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def delete(
        self,
        *,
        path: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes the file at the path given in the path query parameter from the device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.files.delete(
            self._owner.id,
            path=path,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def download(
        self,
        *,
        path: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Pulls the file at the given path query parameter from the device and returns its
        raw bytes as an octet-stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.files.download(
            self._owner.id,
            path=path,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def upload(
        self,
        *,
        path: str,
        file: FileTypes,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Uploads a file to the device via multipart form data, writing it into the
        directory given by the path query parameter using the uploaded file's name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.files.upload(
            self._owner.id,
            path=path,
            file=file,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceKeyboard:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def clear(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Clears the contents of the currently focused text input field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.keyboard.clear(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceLocation:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def get(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedLocation:
        """
        Returns the device's current simulated GPS location as latitude and longitude.
        Devices without geo support return an unsupported-feature error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.location.get(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def reset(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Clears any simulated GPS location and restores the device's default location
        behavior. Devices without geo support return an unsupported-feature error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.location.reset(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def set(
        self,
        *,
        latitude: float,
        longitude: float,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Sets the device's simulated GPS location to the latitude and longitude in the
        request body. Devices without geo support return an unsupported-feature error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.location.set(
            self._owner.id,
            latitude=latitude,
            longitude=longitude,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDevicePackages:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        include_protected_packages: bool | Omit = omit,
        include_system_packages: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DevicesPackageListResponse]:
        """Returns the package names of apps installed on the device.

        System and protected
        packages are excluded unless the corresponding query parameters are set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.packages.list(
            self._owner.id,
            include_protected_packages=include_protected_packages,
            include_system_packages=include_system_packages,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result


class _AsyncDeviceProfile:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def update(
        self,
        *,
        profile_id: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Apply a profile to a device

        Args:
          profile_id: ID of the profile to apply

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.profile.update(
            self._owner.id,
            profile_id=profile_id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceProxy:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def connect(
        self,
        *,
        connect: proxy_connect_params.Connect | Omit = omit,
        host: str | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        port: int | Omit = omit,
        smart_ip: bool | Omit = omit,
        socks5: proxy_connect_params.Socks5 | Omit = omit,
        user: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Routes the device's traffic through a SOCKS5 proxy supplied in the request body,
        replacing any existing connection. A smartIp option can be used to select an IP
        automatically; the legacy flat host/port/user/password fields remain supported.

        Args:
          connect: Mobilerun Connect proxy — pass exactly one of id (use an existing proxy's
              credentials) or country (provision or reuse a rotating residential proxy for the
              device).

          name: Proxy name

          socks5: SOCKS5 proxy configuration (required for socks5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.proxy.connect(
            self._owner.id,
            connect=connect,
            host=host,
            name=name,
            password=password,
            port=port,
            smart_ip=smart_ip,
            socks5=socks5,
            user=user,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def disconnect(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Disconnects the device's active proxy connection and clears its stored proxy
        state. Returns successfully if no proxy is connected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.proxy.disconnect(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def status(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyStatusResponse:
        """
        Returns the device's current proxy connection state, including whether a proxy
        is connected and its protocol and name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.proxy.status(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result


class _AsyncDeviceTasks:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def list(
        self,
        *,
        order_by: Literal["id", "createdAt", "updatedAt", "assignedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncTask, DevicesTaskListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncTask, DevicesTaskListResponse]:
            __page = await self.api.devices.tasks.list(
                self._owner.id,
                order_by=order_by,
                order_by_direction=order_by_direction,
                page=page,
                page_size=page_size,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncTask(self.api, item.task_id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


class _AsyncDeviceClipboard:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def get(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClipboardGetResponse:
        """Returns the current text content of the device's clipboard.

        Devices without
        clipboard support return an unsupported-feature error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.clipboard.get(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def set(
        self,
        *,
        text: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Replaces the device's clipboard content with the text in the request body; an
        empty text clears the clipboard. Devices without clipboard support return an
        unsupported-feature error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.clipboard.set(
            self._owner.id,
            text=text,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceTimezone:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def get(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimezoneGetResponse:
        """Returns the device's current timezone identifier.

        Devices that do not support
        timezone control return an unsupported-feature error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.timezone.get(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def set(
        self,
        *,
        timezone: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Sets the device timezone to the identifier in the request body.

        Devices that do
        not support timezone control return an unsupported-feature error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.timezone.set(
            self._owner.id,
            timezone=timezone,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceLanguage:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def get(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LanguageGetResponse:
        """
        Returns the device's current language/locale as a BCP-47 locale string.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.language.get(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def set(
        self,
        *,
        locale: str,
        restart: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Sets the device language/locale to the BCP-47 locale in the request body.

        An
        optional restart flag applies the change immediately by restarting the Android
        system framework (open apps are closed) instead of waiting for the next reboot;
        some devices ignore it.

        Args:
          locale: BCP-47 locale: a 2–3 letter language tag, optionally followed by a 4-letter
              script and/or a 2-letter region (e.g. en-US, de-DE, ja-JP, zh-Hans-CN).

          restart: Restart the Android system framework so the locale change takes full effect
              immediately; open apps are closed. Without it, the change may not fully apply
              until the next reboot. Some devices ignore this flag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.language.set(
            self._owner.id,
            locale=locale,
            restart=restart,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceDeepLink:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def execute_deep_link(
        self,
        *,
        deep_link: str,
        action: str | Omit = omit,
        bundle_id: str | Omit = omit,
        package_name: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Opens a deep link on the device.

        On Android the link is dispatched as an intent
        — packageName optionally pins it to a specific app and action overrides the
        default android.intent.action.VIEW. On iOS the URL is opened directly and the
        optional fields must be omitted. Protected packages are rejected.

        Args:
          deep_link: Deep link to open (e.g. myapp://path or https://example.com/path)

          action: Android only: intent action to dispatch. Defaults to android.intent.action.VIEW.

          bundle_id: Reserved for targeting a specific iOS app; currently rejected as unsupported.

          package_name: Android only: package to receive the intent (e.g. com.example.app). Omit to let
              the system pick the handler.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.deep_link.execute_deep_link(
            self._owner.id,
            deep_link=deep_link,
            action=action,
            bundle_id=bundle_id,
            package_name=package_name,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceBrowser:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def execute_script(
        self,
        *,
        script: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BrowserExecuteScriptResponse:
        """
        Evaluates a JavaScript expression exactly once in the device's single, confirmed
        foreground Chrome tab via the Chrome DevTools Protocol and returns its
        JSON-serialized result. A responsive browser state without exactly one visible
        page returns DEVICE_NO_BROWSER_TARGET (400). Transient discovery, page-dial, or
        visibility-probe transport failures return CDP_TRANSPORT_UNAVAILABLE (503) with
        Retry-After and an executionOutcome; the service may start Chrome once and retry
        selection before Runtime.evaluate, but dial or probe recovery is skipped for a
        backgrounded Chrome, and a user script is never retried after its write or read.
        Devices without browser support return an unsupported-feature error.

        Args:
          script: JavaScript expression to evaluate in the device's foreground Chrome tab (CDP
              Runtime.evaluate). It is an expression, not a function body — the expression's
              value is returned (no top-level 'return'). Must evaluate to a JSON-serializable
              value; wrap multi-statement logic in an IIFE, e.g. (() => { ... ; return x })().

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.devices.browser.execute_script(
            self._owner.id,
            script=script,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result


class _AsyncDeviceKiosk:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def disable(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Disables Android lock-task (kiosk) mode on the device, releasing it from the
        locked app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.kiosk.disable(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def enable(
        self,
        *,
        package_name: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Locks the device to the package named in the request body using Android
        lock-task (kiosk) mode, preventing the user from leaving the app.

        Args:
          package_name: Package to lock the device to (Android lock-task mode).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.kiosk.enable(
            self._owner.id,
            package_name=package_name,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None


class _AsyncDeviceNumber:
    def __init__(self, api: AsyncMobilerun, owner: AsyncDevice) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def retrieve(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DevicesNumberRetrieveResponse:
        """
        Returns the cloud number bound to the device and the SIM line the device
        presents (carrier, number).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.number.retrieve(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def bind(
        self,
        *,
        number_id: str,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NumberBindResponse:
        """Binds one of your cloud numbers to the device.

        The device's SIM shows the number
        and every SMS it receives is delivered into the device's messages app. Available
        on devices whose capabilities report telephony. A number can be bound to one
        device, and a device holds one number; unbind first to move it.

        Args:
          number_id: The cloud number's id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.devices.number.bind(
            self._owner.id,
            number_id=number_id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def unbind(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NumberUnbindResponse:
        """Releases the number bound to the device.

        The device returns to its own default
        line; SMS to the number stop reaching the device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.devices.number.unbind(
            self._owner.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result


AsyncDeviceInfo = Union[
    DeviceCreateResponse, DeviceRetrieveResponse, DeviceWaitReadyResponse, __types_device_list_response.Item
]


class AsyncDevice:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncDeviceInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncDeviceInfo] = info
        self._info_root = info_root
        self._owned = owned
        owner = self
        self.actions = _AsyncDeviceActions(api, owner)
        self.apps = _AsyncDeviceApps(api, owner)
        self.esim = _AsyncDeviceEsim(api, owner)
        self.files = _AsyncDeviceFiles(api, owner)
        self.keyboard = _AsyncDeviceKeyboard(api, owner)
        self.location = _AsyncDeviceLocation(api, owner)
        self.packages = _AsyncDevicePackages(api, owner)
        self.profile = _AsyncDeviceProfile(api, owner)
        self.proxy = _AsyncDeviceProxy(api, owner)
        self.screenshots = AsyncSavedScreenshotManager(api, owner.id)
        self.tasks = _AsyncDeviceTasks(api, owner)
        self.clipboard = _AsyncDeviceClipboard(api, owner)
        self.timezone = _AsyncDeviceTimezone(api, owner)
        self.language = _AsyncDeviceLanguage(api, owner)
        self.deep_link = _AsyncDeviceDeepLink(api, owner)
        self.browser = _AsyncDeviceBrowser(api, owner)
        self.kiosk = _AsyncDeviceKiosk(api, owner)
        self.recordings = AsyncRecordingManager(api, owner.id)
        self.traffic_sessions = AsyncTrafficSessionManager(api, owner.id)
        self.number = _AsyncDeviceNumber(api, owner)

    @override
    def __repr__(self) -> str:
        fields = f", name={self.name!r}, state={self.state!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceRetrieveResponse:
        result = await self.api.devices.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = ""
        return result

    async def wait_ready(
        self,
        *,
        timeout: float = 300,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> DeviceWaitReadyResponse:
        """Repeat the blocking server readiness call until success or timeout."""
        ready_api = self.api.with_options(max_retries=0)

        async def ready(remaining: float) -> DeviceWaitReadyResponse:
            result = await ready_api.devices.wait_ready(
                self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=remaining
            )
            self.info = result
            self._info_root = ""
            return result

        return await ready_async(ready, timeout=timeout)

    @property
    def name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "name"))

    @property
    def state(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "state"))

    async def fingerprint(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceFingerprintResponse:
        """
        Returns a live snapshot of the device's spoofed identity, including model,
        display, identifiers, and carrier. Devices without fingerprint support return an
        unsupported-feature error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.fingerprint(
            self.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def reboot(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Triggers a reboot of the device.

        The device transitions through its reboot
        lifecycle and becomes ready again once the restart completes. Only devices whose
        capabilities report `reboot=true` can be rebooted. Personal (BYOD) devices
        cannot be rebooted remotely: the request is refused with 400
        `DEVICE_TOOL_UNSUPPORTED` and nothing happens on the device.
        """
        await self.api.devices.reboot(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def reset(
        self,
        *,
        mode: Literal["full", "identity"] | Omit = omit,
        preserve: Optional[List[Literal["proxy", "location", "locale", "timezone"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Resets the device.

        `mode` selects what is erased: `full` (factory reset: apps,
        accounts, storage, new identity) or `identity` (new fingerprint, apps and data
        kept). Without `mode` the reset is `full`, or `identity` on devices with
        `factoryReset=false`. A mode or `preserve` value the device does not support is
        refused with 400 `DEVICE_TOOL_UNSUPPORTED`. `preserve` restores the latest
        proxy, location, locale or timezone set through the API after the reset; omitted
        or empty preserves nothing. The device becomes ready again after the reset.

        Args:
          mode: What to erase. full: factory reset — erases the user data (apps, accounts,
              storage) and gives the device a new identity. identity: new device fingerprint,
              apps and data are kept. When omitted: full, or identity on devices whose
              capabilities report factoryReset=false.

          preserve: Device configuration to restore after the reset: the latest value set through
              the API. Omitted, null or empty preserves nothing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.reset(
            self.id,
            mode=mode,
            preserve=preserve,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def retrieve_capabilities(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceRetrieveCapabilitiesResponse:
        """Returns the set of capabilities supported by this device.

        Used to determine
        which tools and features are available for the device.
        """
        result = await self.api.devices.retrieve_capabilities(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def set_name(
        self,
        *,
        name: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> DeviceSetNameResponse:
        """
        Sets the display name for a device from the name in the request body and returns
        the updated device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.devices.set_name(
            self.id,
            name=name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def terminate(
        self,
        *,
        previous_device_id: str | Omit = omit,
        terminate_at: Union[str, datetime] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Terminates the device and releases its resources.

        For a personal (BYOD) device
        the owner (API key or user) can instead remove the phone from the account so
        anyone can pair it again; the phone must be disconnected first, otherwise the
        request is rejected with 409 BYOD_DEVICE_CONNECTED. Other subscription-billed
        devices cannot be terminated with this request; it is rejected with 401. The
        `terminateAt` and `previousDeviceId` body fields are reserved for internal use;
        requests that set them are rejected with 401.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.terminate(
            self.id,
            previous_device_id=previous_device_id,
            terminate_at=terminate_at,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def resume(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
        wait_ready: bool = True,
        ready_timeout: float = 300,
    ) -> AsyncDevice:
        """
        Wakes a parked device: it first checks that the device can run again, then the
        same device starts and per-minute billing resumes. On a device that is not
        parked, the request does nothing.


        Waits until the object is ready again (default), returns the handle; opt out with `wait_ready=False` and set the timeout with `ready_timeout`.
        """
        check_wait(ready_timeout, SINGLE_CALL_INTERVAL)
        await self.api.devices.resume(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        if wait_ready:
            try:
                await self.wait_ready(timeout=ready_timeout)
            except BaseException as cause:
                if isinstance(cause, Exception):
                    raise ObjectReadyError(self, self.id, cause) from cause
                cast(Any, cause).object = self
                cast(Any, cause).id = self.id
                raise
        return self

    async def stop(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
        wait: bool = True,
        wait_timeout: float | None = None,
    ) -> AsyncDevice:
        """
        Parks the device: its data, apps and identity are kept, but nothing runs and
        nothing is billed until it is resumed. Only devices whose capabilities report
        stop=true support this; others return 404.


        Runs wait_stopped after success (default), returns the handle; opt out with `wait=False` and set the timeout with `wait_timeout`.
        """
        if wait_timeout is not None:
            check_wait(wait_timeout, SINGLE_CALL_INTERVAL)
        await self.api.devices.stop(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        if wait:
            await self.wait_stopped(timeout=300 if wait_timeout is None else wait_timeout)
        return self

    async def tap(
        self,
        x: int,
        y: int,
        *,
        humanize: bool | Omit = omit,
        stealth: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Taps the device screen at the given x/y coordinates.

        An optional humanize flag
        routes the tap through human-like input on devices that support it.

        Args:
          humanize: Request human-like input where supported by the device. Defaults to false.

          stealth: Deprecated: use humanize. Both names must agree when supplied together.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.actions.tap(
            self.id,
            x=x,
            y=y,
            humanize=humanize,
            stealth=stealth,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def type(
        self,
        text: str,
        *,
        clear: bool | Omit = omit,
        completion_mode: Literal["accepted", "committed"] | Omit = omit,
        error_rate: float | Omit = omit,
        humanize: bool | Omit = omit,
        stealth: bool | Omit = omit,
        wpm: int | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Types text into the focused input field.

        The optional completionMode defaults to
        accepted for backwards-compatible low latency; committed additionally waits for
        the complete text or a quiescent UI state.

        Args:
          completion_mode: Completion guarantee. accepted returns after the input provider accepts the
              operation; committed additionally waits for the focused UI state to contain the
              complete text or become quiescent.

          error_rate: Per-character mistake rate for humanized typing. -1 uses server default.

          humanize: Request human-like input where supported by the device. Defaults to false.

          stealth: Deprecated: use humanize. Both names must agree when supplied together.

          wpm: Words per minute for humanized typing. 0 uses the device default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.keyboard.write(
            self.id,
            text=text,
            clear=clear,
            completion_mode=completion_mode,
            error_rate=error_rate,
            humanize=humanize,
            stealth=stealth,
            wpm=wpm,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def screenshot(
        self,
        *,
        hide_overlay: bool | Omit = omit,
        save: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Screenshot:
        async with self.api.devices.screenshots.with_streaming_response.capture(
            self.id,
            hide_overlay=hide_overlay,
            save=save,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        ) as response:
            data = await response.read()
            return Screenshot(data, response.headers)

    @overload
    async def run(
        self,
        *,
        task: str,
        accessibility: bool | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        continue_on_failure: bool | Omit = omit,
        credentials: Iterable[task_run_params.Credential] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        humanize: bool | Omit = omit,
        internal: bool | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: builtins.type[_ModelT],
        reasoning: bool | Omit = omit,
        recording_enabled: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        system_prompt: Optional[str] | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncTask[_ModelT]: ...

    @overload
    async def run(
        self,
        *,
        task: str,
        accessibility: bool | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        continue_on_failure: bool | Omit = omit,
        credentials: Iterable[task_run_params.Credential] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        humanize: bool | Omit = omit,
        internal: bool | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reasoning: bool | Omit = omit,
        recording_enabled: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        system_prompt: Optional[str] | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncTask[None]: ...

    async def run(
        self,
        *,
        task: str,
        accessibility: bool | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        continue_on_failure: bool | Omit = omit,
        credentials: Iterable[task_run_params.Credential] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        humanize: bool | Omit = omit,
        internal: bool | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Union[Optional[Dict[str, object]], builtins.type[BaseModel]] | Omit = omit,
        reasoning: bool | Omit = omit,
        recording_enabled: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        system_prompt: Optional[str] | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncTask[Any]:
        """Create and dispatch a new agent task.

        Returns the task ID and device stream
        details.

        Args:
          display_id: The display ID of the device to run the task on.

          execution_timeout: Maximum agent execution time in seconds (1–2700).

          humanize: Request human-like input where supported by the device. Replaces the deprecated
              stealth field; both must agree when supplied together.

          internal: Mark a task started by an agent or worker on the user's behalf. It is listed as
              source='agent' (excluded from source='api' lists) and its events carry
              internal=true so user-facing notifications and webhooks skip it. It is still
              billed, controllable and retrievable by id.

          llm_model: The LLM model identifier to use for the task (e.g.
              'mobilerun/mobile-agent-fast'). When omitted with reasoning=false, the fast-mode
              default model is used.

          recording_enabled: Record device video for the whole task and persist a retrievable reference

          stealth: Deprecated: use humanize. Both names must agree when supplied together.

          subagent_model: LLM model used by sub-agent roles: executor, app_opener, structured_output

          system_prompt: Optional custom behavioral overlay applied on top of the agent's default system
              prompts. Never echoed back in responses or errors.

          temperature: Deprecated and ignored. Sampling behavior is controlled by the model provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.tasks.run(
            device_id=self.id,
            task=task,
            accessibility=accessibility,
            apps=apps,
            continue_on_failure=continue_on_failure,
            credentials=credentials,
            display_id=display_id,
            execution_timeout=execution_timeout,
            files=files,
            humanize=humanize,
            internal=internal,
            llm_model=llm_model,
            max_steps=max_steps,
            output_schema=model_output_schema(output_schema),
            reasoning=reasoning,
            recording_enabled=recording_enabled,
            stealth=stealth,
            subagent_model=subagent_model,
            system_prompt=system_prompt,
            temperature=temperature,
            vision=vision,
            vpn_country=vpn_country,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=bound_extra(extra_body, {"deviceId": self.id}, headers=False),
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return AsyncTask(self.api, result.id, result, output_parser=output_parser(output_schema), info_root="")

    async def swipe(
        self,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        duration: int,
        *,
        hold_ms: int | Omit = omit,
        humanize: bool | Omit = omit,
        stealth: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Swipes from a start coordinate to an end coordinate over the given duration in
        milliseconds. The optional humanize flag (best-effort, also with holdMs) adds a
        human-like path and timing. With holdMs > 0 the request returns 422 when
        duration + holdMs exceeds 9000 ms, or on devices that do not support it.

        Args:
          duration: Swipe duration in milliseconds

          hold_ms: Keep the finger at the end point for holdMs and suppress fling before lifting,
              so content moves by about the finger travel. Supported on Android cloud phones.

          humanize: Request human-like input where supported by the device. Defaults to false.

          stealth: Deprecated: use humanize. Both names must agree when supplied together.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.actions.swipe(
            self.id,
            duration=duration,
            end_x=end_x,
            end_y=end_y,
            start_x=start_x,
            start_y=start_y,
            hold_ms=hold_ms,
            humanize=humanize,
            stealth=stealth,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def key(
        self,
        key: int,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Presses a key using the platform key code.


        Sends a single Android key event to the device, identified by its key code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.keyboard.key(
            self.id,
            key=key,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def open_app(
        self,
        package_name: str,
        *,
        activity: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Launches the app identified by the path package name, optionally starting a
        specific activity given in the request body. Protected packages cannot be
        started.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.apps.start(
            package_name,
            device_id=self.id,
            activity=activity,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def stop_app(
        self,
        package_name: str,
        *,
        clear_data: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Force-stops the app identified by the path package name.

        When clearData is set
        in the request body, the app's data is also cleared. Protected packages cannot
        be stopped.

        Args:
          clear_data: If true, clears all app data (pm clear) in addition to stopping the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.apps.stop(
            package_name,
            device_id=self.id,
            clear_data=clear_data,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def home(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Presses the Home button.


        Performs a global system action on the device, such as navigating back or going
        to the home screen, identified by an action code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.actions.global_(
            self.id,
            action=2,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=bound_extra(extra_body, {"action": 2}, headers=False),
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def back(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Presses the Back button.


        Performs a global system action on the device, such as navigating back or going
        to the home screen, identified by an action code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        await self.api.devices.actions.global_(
            self.id,
            action=1,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=bound_extra(extra_body, {"action": 1}, headers=False),
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def ui(
        self,
        *,
        filter: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateUiResponse:
        """
        Returns the current accessibility UI state as a structured tree of on-screen elements.



        Returns the current accessibility UI state of the device as a structured tree of
        on-screen elements. An optional filter query reduces the result to interactive
        elements.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.state.ui(
            self.id,
            filter=filter,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def time(
        self,
        *,
        x_device_display_id: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Returns the device wall-clock time as an RFC 3339 timestamp.


        Returns the device's current wall-clock time as an RFC 3339 timestamp.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.devices.state.time(
            self.id,
            x_device_display_id=x_device_display_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def wait_stopped(
        self,
        *,
        timeout: float = 300,
        poll_interval: float = 1,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> DeviceRetrieveResponse:
        """Wait for the declared success condition; failure raises with the last response."""

        poll_api = self.api.with_options(max_retries=0)

        async def poll(remaining: float) -> DeviceRetrieveResponse:
            result = await poll_api.devices.retrieve(
                self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=remaining
            )
            self.info = result
            self._info_root = ""
            return result

        result = await wait_async(
            poll,
            lambda status: status.state,
            ["stopped"],
            ["terminate", "terminated"],
            pending=None,
            timeout=timeout,
            poll_interval=poll_interval,
            poll_request_timeout=30,
        )
        return result

    async def __aenter__(self) -> AsyncDevice:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if not self._owned:
            return
        self._owned = False
        try:
            with anyio.CancelScope(shield=True):
                with anyio.move_on_after(10) as scope:
                    await self.api.devices.terminate(
                        self.id,
                        extra_headers=None,
                        extra_query=None,
                        extra_body=None,
                        timeout=not_given,
                        idempotency_key=None,
                    )
                if scope.cancel_called:
                    raise TimeoutError("Object cleanup timed out")
        except BaseException as cleanup_error:
            if exc is None:
                raise
            attach_cleanup_error(exc, cleanup_error)


AsyncSavedScreenshotInfo = Union[__types_devices_screenshot_list_response.Item]


class AsyncSavedScreenshot:
    def __init__(
        self,
        api: AsyncMobilerun,
        device_id: str,
        id: str,
        info: Optional[AsyncSavedScreenshotInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self._device_id = device_id
        self.info: Optional[AsyncSavedScreenshotInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", captured_at={self.captured_at!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    @property
    def device_id(self) -> str:
        return self._device_id

    @property
    def captured_at(self) -> Union[datetime, None]:
        """Reads only the last create/list snapshot without making a request; fromId/from_id handles have no data."""
        return cast(Union[datetime, None], record_field(self.info, self._info_root, "capturedAt"))

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Delete a device screenshot"""
        await self.api.devices.screenshots.delete(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def image(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> bytes:
        async with self.api.devices.screenshots.with_streaming_response.image(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        ) as response:
            data = await response.read()
            return data

    async def __aenter__(self) -> AsyncSavedScreenshot:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncRecordingInfo = Union[
    RecordingStartResponse, RecordingStatusResponse, __types_devices_recording_list_response.RecordingListResponseItem
]


class AsyncRecording:
    def __init__(
        self,
        api: AsyncMobilerun,
        device_id: str,
        id: str,
        info: Optional[AsyncRecordingInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self._device_id = device_id
        self.info: Optional[AsyncRecordingInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", name={self.name!r}, status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    @property
    def device_id(self) -> str:
        return self._device_id

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingStatusResponse:
        result = await self.api.devices.recordings.status(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self.info = result
        self._info_root = ""
        return result

    @property
    def name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "name"))

    @property
    def status(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "status"))

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Delete a device recording"""
        await self.api.devices.recordings.delete(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def screenshots(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RecordingScreenshotsResponse]:
        """
        Screenshots saved into the recording with
        `GET /devices/{deviceId}/screenshot?save=true`, oldest first, each with a
        presigned download URL.
        """
        result = await self.api.devices.recordings.screenshots(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def stop(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RecordingStopResponse:
        """Stop a device recording"""
        result = await self.api.devices.recordings.stop(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def video(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> bytes:
        async with self.api.devices.recordings.with_streaming_response.video(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        ) as response:
            data = await response.read()
            return data

    async def trajectory(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> bytes:
        async with self.api.devices.recordings.with_streaming_response.trajectory(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        ) as response:
            data = await response.read()
            return data

    async def wait(
        self,
        *,
        timeout: float = 300,
        poll_interval: float = 1,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> RecordingStatusResponse:
        """Wait for the declared success condition; failure raises with the last response."""

        poll_api = self.api.with_options(max_retries=0)

        async def poll(remaining: float) -> RecordingStatusResponse:
            result = await poll_api.devices.recordings.status(
                self.id,
                device_id=self.device_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=remaining,
            )
            self.info = result
            self._info_root = ""
            return result

        result = await wait_async(
            poll,
            lambda status: status.status,
            ["completed"],
            ["failed", "expired"],
            pending=["recording", "uploading"],
            timeout=timeout,
            poll_interval=poll_interval,
            poll_request_timeout=30,
        )
        return result

    async def __aenter__(self) -> AsyncRecording:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if not self._owned:
            return
        self._owned = False
        try:
            with anyio.CancelScope(shield=True):
                with anyio.move_on_after(10) as scope:
                    await self.api.devices.recordings.stop(
                        self.id,
                        device_id=self.device_id,
                        extra_headers=None,
                        extra_query=None,
                        extra_body=None,
                        timeout=not_given,
                        idempotency_key=None,
                    )
                if scope.cancel_called:
                    raise TimeoutError("Object cleanup timed out")
        except BaseException as cleanup_error:
            if exc is None:
                raise
            attach_cleanup_error(exc, cleanup_error)


AsyncTrafficSessionInfo = Union[
    TrafficSessionCreateResponse, TrafficSessionRetrieveResponse, __types_devices_traffic_session_list_response.Item
]


class AsyncTrafficSession:
    def __init__(
        self,
        api: AsyncMobilerun,
        device_id: str,
        id: str,
        info: Optional[AsyncTrafficSessionInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self._device_id = device_id
        self.info: Optional[AsyncTrafficSessionInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", state={self.state!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    @property
    def device_id(self) -> str:
        return self._device_id

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficSessionRetrieveResponse:
        result = await self.api.devices.traffic_sessions.retrieve(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self.info = result
        self._info_root = ""
        return result

    @property
    def state(self) -> Union[Literal["starting", "active", "stopping", "stopped", "failed", "expired"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[Literal["starting", "active", "stopping", "stopped", "failed", "expired"], None],
            record_field(self.info, self._info_root, "state"),
        )

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TrafficSessionDeleteResponse:
        """Stop device traffic inspection"""
        result = await self.api.devices.traffic_sessions.delete(
            self.id,
            device_id=self.device_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def __aenter__(self) -> AsyncTrafficSession:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncProxyConfigurationInfo = Union[ProxyCreateResponse, TypesProxyRetrieveResponse, __types_proxy_list_response.Data]


class AsyncProxyConfiguration:
    "A stored proxy configuration."

    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncProxyConfigurationInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncProxyConfigurationInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", name={self.name!r}, protocol={self.protocol!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypesProxyRetrieveResponse:
        result = await self.api.proxies.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "name"))

    @property
    def protocol(self) -> Union[Literal["socks5", "wireguard"], None]:
        """Reads the last response without making a request."""
        return cast(Union[Literal["socks5", "wireguard"], None], record_field(self.info, self._info_root, "protocol"))

    @overload
    async def update(
        self,
        *,
        host: str,
        name: str,
        password: str,
        port: int,
        protocol: Literal["socks5"],
        user: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TypesProxyUpdateResponse: ...

    @overload
    async def update(
        self,
        *,
        config: str,
        name: str,
        protocol: Literal["wireguard"],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TypesProxyUpdateResponse: ...

    async def update(
        self,
        *,
        host: str | Omit = omit,
        name: str,
        password: str | Omit = omit,
        port: int | Omit = omit,
        protocol: Literal["socks5"] | Literal["wireguard"],
        user: str | Omit = omit,
        config: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TypesProxyUpdateResponse:
        """Replaces the proxy config identified by `proxyId` with the provided body.

        As
        with creation, the body is a `protocol`-discriminated union of socks5 or
        wireguard fields. Returns the updated config.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await cast(Callable[..., Awaitable[TypesProxyUpdateResponse]], self.api.proxies.update)(
            self.id,
            host=host,
            name=name,
            password=password,
            port=port,
            protocol=protocol,
            user=user,
            config=config,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProxyDeleteResponse:
        """
        Permanently deletes the proxy config identified by `proxyId` and returns the
        deleted config. Returns not found if no matching config exists.
        """
        result = await self.api.proxies.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def __aenter__(self) -> AsyncProxyConfiguration:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncConnectProxyInfo = Union[ConnectProxyRetrieveResponse, ProxyBuyResponse, __types_connect_proxy_list_response.Item]


class AsyncConnectProxy:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncConnectProxyInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncConnectProxyInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", name={self.name!r}, status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectProxyRetrieveResponse:
        result = await self.api.connect.proxies.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = ""
        return result

    @property
    def name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "name"))

    @property
    def status(
        self,
    ) -> Union[Literal["checking", "pending_payment", "provisioning", "active", "cancelling", "ended", "error"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[
                Literal["checking", "pending_payment", "provisioning", "active", "cancelling", "ended", "error"], None
            ],
            record_field(self.info, self._info_root, "status"),
        )

    async def update(
        self,
        *,
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ConnectProxyUpdateResponse:
        """
        Renames the proxy identified by the path ID.

        Args:
          name: New display name, up to 64 characters excluding surrounding whitespace, and
              containing no NUL. Send null (or an empty/whitespace-only string) to drop a
              custom name and go back to the generated label. Omit to leave the name
              unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.connect.proxies.update(
            self.id,
            name=name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def cancel(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes the proxy identified by the path ID and releases its provisioning.
        Returns 404 if no such proxy exists for the caller.
        """
        await self.api.connect.proxies.cancel(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def checkout(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProxyCheckoutResponse:
        """
        Refreshes a pending dedicated proxy's checkout on explicit payment intent.
        Already-paid proxies (provisioning, active, or cancelling) return their current
        status without a payment URL. An expired checkout requires a new purchase.
        """
        result = await self.api.connect.proxies.checkout(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def ensure_healthy(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProxyEnsureHealthyResponse:
        """
        Checks right now that the proxy's upstream accepts a connection through its
        current session. If the upstream refuses the session and the proxy is a rotating
        (sticky-session) proxy, the proxy is moved onto a fresh session that has been
        checked to work; its credentials and country stay the same, its exit IP changes.
        Intended for callers that are about to depend on the proxy (e.g. while
        provisioning a phone). After `rotated`, the gateway uses the new session within
        about 30 seconds. A `refused` or `unreachable` result is not an error: the
        response describes the proxy's state.
        """
        result = await self.api.connect.proxies.ensure_healthy(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def list_connections(
        self,
        *,
        close_reason: str | Omit = omit,
        country: str | Omit = omit,
        dst_host: str | Omit = omit,
        dst_port: int | Omit = omit,
        ended_after: Union[str, datetime] | Omit = omit,
        ended_before: Union[str, datetime] | Omit = omit,
        max_bytes_in: int | Omit = omit,
        max_bytes_out: int | Omit = omit,
        max_duration_ms: int | Omit = omit,
        max_total_bytes: int | Omit = omit,
        min_bytes_in: int | Omit = omit,
        min_bytes_out: int | Omit = omit,
        min_duration_ms: int | Omit = omit,
        min_total_bytes: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["startedAt", "endedAt", "bytesIn", "bytesOut", "totalBytes", "durationMs"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        protocol: Literal["tcp", "udp", "unknown"] | Omit = omit,
        provider: str | Omit = omit,
        session_id: str | Omit = omit,
        started_after: Union[str, datetime] | Omit = omit,
        started_before: Union[str, datetime] | Omit = omit,
        status: Literal["active", "closed"] | Omit = omit,
        user_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyListConnectionsResponse:
        """
        Returns the connection history recorded for this proxy, one item per connection
        (aggregated across the connection's lifetime). Supports filtering on every
        property plus ordering and pagination. Returns 503 when connection history is
        temporarily unavailable.

        Args:
          close_reason: Filter to connections that closed with this reason (closed connections only).

          country: Filter to connections served from this upstream country (ISO 3166-1 alpha-2).

          dst_host: Filter to connections to this destination host (exact match).

          dst_port: Filter to connections to this destination port.

          ended_after: Filter to connections whose last activity was at or after this time (inclusive).

          ended_before: Filter to connections whose last activity was at or before this time
              (inclusive).

          max_bytes_in: Filter to connections with at most this many bytes received from upstream.

          max_bytes_out: Filter to connections with at most this many bytes sent to upstream.

          max_duration_ms: Filter to connections lasting at most this many milliseconds.

          max_total_bytes: Filter to connections with at most this much total traffic (bytesIn + bytesOut).

          min_bytes_in: Filter to connections with at least this many bytes received from upstream.

          min_bytes_out: Filter to connections with at least this many bytes sent to upstream.

          min_duration_ms: Filter to connections lasting at least this many milliseconds.

          min_total_bytes: Filter to connections with at least this much total traffic (bytesIn +
              bytesOut).

          order: Sort direction.

          order_by: Property to order the results by.

          page: Page number (1-based).

          page_size: Number of items per page.

          protocol: Filter to connections of this transport protocol.

          provider: Filter to connections served by this upstream provider identifier.

          session_id: Filter to a single connection by its session id.

          started_after: Filter to connections that started at or after this time (inclusive).

          started_before: Filter to connections that started at or before this time (inclusive).

          status: Filter by connection status.

          user_id: Filter to connections made by this user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.connect.proxies.list_connections(
            self.id,
            close_reason=close_reason,
            country=country,
            dst_host=dst_host,
            dst_port=dst_port,
            ended_after=ended_after,
            ended_before=ended_before,
            max_bytes_in=max_bytes_in,
            max_bytes_out=max_bytes_out,
            max_duration_ms=max_duration_ms,
            max_total_bytes=max_total_bytes,
            min_bytes_in=min_bytes_in,
            min_bytes_out=min_bytes_out,
            min_duration_ms=min_duration_ms,
            min_total_bytes=min_total_bytes,
            order=order,
            order_by=order_by,
            page=page,
            page_size=page_size,
            protocol=protocol,
            provider=provider,
            session_id=session_id,
            started_after=started_after,
            started_before=started_before,
            status=status,
            user_id=user_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def ping(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyPingResponse:
        """
        Returns the most recent cached network-latency measurement for the proxy,
        sampled periodically by connecting through the proxy to a fixed target.
        `latency` is null when no measurement is available yet (e.g. the proxy is not
        active, or it has not been sampled since coming online).
        """
        result = await self.api.connect.proxies.ping(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def __aenter__(self) -> AsyncConnectProxy:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncConnectUserInfo = Union[UserCreateResponse, UserRetrieveResponse, __types_connect_user_list_response.Item]


class AsyncConnectUser:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncConnectUserInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncConnectUserInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", username={self.username!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        result = await self.api.connect.users.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = ""
        return result

    @property
    def username(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "username"))

    async def update(
        self,
        *,
        proxy_id: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> UserUpdateResponse:
        """
        Rebind the user to a different proxy (or detach it by passing null).

        Args:
          proxy_id: Proxy to rebind to, or null to detach. Omit to leave the user's current binding
              unchanged — only an explicit null detaches.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.connect.users.update(
            self.id,
            proxy_id=proxy_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes the SOCKS5 user identified by the path ID, revoking its credentials and
        any proxy binding. Returns 404 if no such user exists for the caller.
        """
        await self.api.connect.users.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def list_connections(
        self,
        *,
        close_reason: str | Omit = omit,
        country: str | Omit = omit,
        dst_host: str | Omit = omit,
        dst_port: int | Omit = omit,
        ended_after: Union[str, datetime] | Omit = omit,
        ended_before: Union[str, datetime] | Omit = omit,
        max_bytes_in: int | Omit = omit,
        max_bytes_out: int | Omit = omit,
        max_duration_ms: int | Omit = omit,
        max_total_bytes: int | Omit = omit,
        min_bytes_in: int | Omit = omit,
        min_bytes_out: int | Omit = omit,
        min_duration_ms: int | Omit = omit,
        min_total_bytes: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["startedAt", "endedAt", "bytesIn", "bytesOut", "totalBytes", "durationMs"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        protocol: Literal["tcp", "udp", "unknown"] | Omit = omit,
        provider: str | Omit = omit,
        proxy_id: str | Omit = omit,
        session_id: str | Omit = omit,
        started_after: Union[str, datetime] | Omit = omit,
        started_before: Union[str, datetime] | Omit = omit,
        status: Literal["active", "closed"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListConnectionsResponse:
        """
        Returns the connection history recorded for this user, one item per connection
        (aggregated across the connection's lifetime). Supports filtering on every
        property plus ordering and pagination. Returns 503 when connection history is
        temporarily unavailable.

        Args:
          close_reason: Filter to connections that closed with this reason (closed connections only).

          country: Filter to connections served from this upstream country (ISO 3166-1 alpha-2).

          dst_host: Filter to connections to this destination host (exact match).

          dst_port: Filter to connections to this destination port.

          ended_after: Filter to connections whose last activity was at or after this time (inclusive).

          ended_before: Filter to connections whose last activity was at or before this time
              (inclusive).

          max_bytes_in: Filter to connections with at most this many bytes received from upstream.

          max_bytes_out: Filter to connections with at most this many bytes sent to upstream.

          max_duration_ms: Filter to connections lasting at most this many milliseconds.

          max_total_bytes: Filter to connections with at most this much total traffic (bytesIn + bytesOut).

          min_bytes_in: Filter to connections with at least this many bytes received from upstream.

          min_bytes_out: Filter to connections with at least this many bytes sent to upstream.

          min_duration_ms: Filter to connections lasting at least this many milliseconds.

          min_total_bytes: Filter to connections with at least this much total traffic (bytesIn +
              bytesOut).

          order: Sort direction.

          order_by: Property to order the results by.

          page: Page number (1-based).

          page_size: Number of items per page.

          protocol: Filter to connections of this transport protocol.

          provider: Filter to connections served by this upstream provider identifier.

          proxy_id: Filter to connections routed through this proxy.

          session_id: Filter to a single connection by its session id.

          started_after: Filter to connections that started at or after this time (inclusive).

          started_before: Filter to connections that started at or before this time (inclusive).

          status: Filter by connection status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.connect.users.list_connections(
            self.id,
            close_reason=close_reason,
            country=country,
            dst_host=dst_host,
            dst_port=dst_port,
            ended_after=ended_after,
            ended_before=ended_before,
            max_bytes_in=max_bytes_in,
            max_bytes_out=max_bytes_out,
            max_duration_ms=max_duration_ms,
            max_total_bytes=max_total_bytes,
            min_bytes_in=min_bytes_in,
            min_bytes_out=min_bytes_out,
            min_duration_ms=min_duration_ms,
            min_total_bytes=min_total_bytes,
            order=order,
            order_by=order_by,
            page=page,
            page_size=page_size,
            protocol=protocol,
            provider=provider,
            proxy_id=proxy_id,
            session_id=session_id,
            started_after=started_after,
            started_before=started_before,
            status=status,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def __aenter__(self) -> AsyncConnectUser:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


class _AsyncTaskScreenshots:
    def __init__(self, api: AsyncMobilerun, owner: AsyncTask[Any]) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def retrieve(
        self,
        index: int,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenshotRetrieveResponse:
        """
        Get a specific screenshot by index.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.tasks.screenshots.retrieve(
            index,
            task_id=self._owner.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TasksScreenshotListResponse:
        """List all screenshot URLs for a task."""
        result = await self.api.tasks.screenshots.list(
            self._owner.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result


class _AsyncTaskUiStates:
    def __init__(self, api: AsyncMobilerun, owner: AsyncTask[Any]) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def retrieve(
        self,
        index: int,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UiStateRetrieveResponse:
        """
        Get a specific UI state by index.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.tasks.ui_states.retrieve(
            index,
            task_id=self._owner.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UiStateListResponse:
        """List all UI state URLs for a task."""
        result = await self.api.tasks.ui_states.list(
            self._owner.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result


AsyncTaskInfo = Union[
    TaskRetrieveResponse,
    TaskGetStatusResponse,
    TaskRunResponse,
    __types_devices_task_list_response.Item,
    __types_task_list_response.Item,
]


class AsyncTask(Generic[_OutputT]):
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncTaskInfo] = None,
        *,
        owned: bool = False,
        output_parser: Optional[Callable[[object], _OutputT]] = None,
        info_root: str = "task",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncTaskInfo] = info
        self._info_root = info_root
        self._owned = owned
        self._output_parser = output_parser
        owner = self
        self.screenshots = _AsyncTaskScreenshots(api, owner)
        self.ui_states = _AsyncTaskUiStates(api, owner)

    @override
    def __repr__(self) -> str:
        fields = f", status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRetrieveResponse:
        result = await self.api.tasks.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "task"
        return result

    @property
    def status(
        self,
    ) -> Union[
        Literal["prepared", "queued", "created", "running", "cancelling", "completed", "failed", "cancelled"], None
    ]:
        """Not available on handles from `device.tasks.list()` until `refresh()`."""
        return cast(
            Union[
                Literal["prepared", "queued", "created", "running", "cancelling", "completed", "failed", "cancelled"],
                None,
            ],
            record_field(self.info, self._info_root, "status"),
        )

    async def attach(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Attach to a running task and receive its events as an SSE stream."""
        await self.api.tasks.attach(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return None

    async def get_status(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGetStatusResponse:
        """Get the status of a task."""
        result = await self.api.tasks.get_status(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def get_trajectory(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGetTrajectoryResponse:
        """Get the trajectory of a task."""
        result = await self.api.tasks.get_trajectory(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def send_message(
        self,
        *,
        message: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TaskSendMessageResponse:
        """Send a message to a running agent task.

        The message ID is delivered via SSE
        (UserMessageEvent with action=queued).

        Args:
          message: Message to send to the running agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.tasks.send_message(
            self.id,
            message=message,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def stop(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TaskStopResponse:
        """Cancel a running task.

        Returns an error if the task is already in a terminal
        state.
        """
        result = await self.api.tasks.stop(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def wait(
        self,
        *,
        timeout: float = 600,
        poll_interval: float = 1,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> TaskGetStatusResponse:
        """Wait for the declared success condition; failure raises with the last response."""

        poll_api = self.api.with_options(max_retries=0)

        async def poll(remaining: float) -> TaskGetStatusResponse:
            result = await poll_api.tasks.get_status(
                self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=remaining
            )
            self.info = result
            self._info_root = ""
            return result

        result = await wait_async(
            poll,
            lambda status: status.status,
            ["completed"],
            ["failed", "cancelled"],
            pending=["prepared", "queued", "created", "running", "cancelling"],
            timeout=timeout,
            poll_interval=poll_interval,
            poll_request_timeout=30,
        )
        return result

    async def wait_output(
        self,
        *,
        timeout: float = 600,
        poll_interval: float = 1,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> WaitOutput[_OutputT, TaskGetStatusResponse]:
        if self._output_parser is None:
            raise TypeError("Typed output requires an output schema parser")
        result = await self.wait(
            timeout=timeout,
            poll_interval=poll_interval,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        return parse_output(
            self._output_parser, read_path(result, ["output"]), result, self.id, self.__class__.__name__
        )

    async def __aenter__(self) -> AsyncTask[_OutputT]:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncTriggerInfo = Union[TriggerCreateResponse, TriggerRetrieveResponse, __types_workflows_trigger_list_response.Item]


class AsyncTrigger:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncTriggerInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncTriggerInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", name={self.name!r}, activation={self.activation!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        result = await self.api.workflows.triggers.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "name"))

    @property
    def activation(self) -> Union[Literal["event", "schedule", "custom"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[Literal["event", "schedule", "custom"], None], record_field(self.info, self._info_root, "activation")
        )

    async def update(
        self,
        *,
        activation: Literal["event", "schedule", "custom"] | Omit = omit,
        conditions: Optional[trigger_update_params.Conditions] | Omit = omit,
        custom_payload_schema: Optional[Dict[str, object]] | Omit = omit,
        description: str | Omit = omit,
        event_type: str | Omit = omit,
        name: str | Omit = omit,
        payload: Optional[Dict[str, object]] | Omit = omit,
        schedule_rule: Optional[trigger_update_params.ScheduleRule] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TriggerUpdateResponse:
        """Partially update a trigger; all fields are optional.

        When `activation` is
        changed, the type-specific field rules are re-validated. Schedule triggers
        accept stored `payload` values (at most 1 MiB); null clears them. The resulting
        payload must match customPayloadSchema (422 on mismatch, including schema
        changes that invalidate stored values). Absent or null values are validated as
        an empty object when a schema is configured. Changes apply from the next run.
        Returns 404 if the trigger does not exist.

        Args:
          custom_payload_schema: Optional JSON Schema for validating payloads for custom or schedule triggers

          payload: Stored schedule input values (maximum 1 MiB of JSON); null clears them. Requires
              customPayloadSchema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.triggers.update(
            self.id,
            activation=activation,
            conditions=conditions,
            custom_payload_schema=custom_payload_schema,
            description=description,
            event_type=event_type,
            name=name,
            payload=payload,
            schedule_rule=schedule_rule,
            timezone=timezone,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TriggerDeleteResponse:
        """Delete a trigger by its ID. Returns 404 if no trigger matches."""
        result = await self.api.workflows.triggers.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def fire(
        self,
        *,
        payload: Dict[str, object],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> TriggerFireResponse:
        """
        Invoke a custom trigger directly with an arbitrary JSON payload.

        Fan-out: a trigger may be referenced by multiple flows (workflows). Firing it
        enqueues one execution per enabled, non-deleted flow attached to this trigger,
        each receiving the same payload. The `enqueuedCount` in the response reports how
        many were enqueued (0 if no flows are attached, or if all matching flows are
        gated by a cooldown).

        Payload validation:

        - If the trigger has a `customPayloadSchema`, the payload is validated against
          it (JSON Schema).
        - If no schema is configured, the payload only needs to be a JSON object — any
          keys and values are accepted.

        Only triggers with `activation = "custom"` can be fired through this endpoint;
        event and schedule triggers return 409.

        Supports an optional `Idempotency-Key` header (1-255 printable ASCII
        characters), which maps to the derived `invocationId` used for fan-out
        deduplication. The payload is bound to the key on the first accepted fire,
        before fan-out. A repeat with the same key and an identical payload returns 202
        with `Idempotent-Replayed: true` (`deduplicated: true` when flows were skipped;
        `enqueuedCount` counts only executions enqueued by that call); a changed payload
        under the same key returns 422 `idempotency_key_reused`.

        Args:
          payload: Arbitrary JSON object forwarded to every flow attached to this trigger.
              Validated against the trigger's customPayloadSchema when one is configured;
              otherwise only "must be a JSON object" is enforced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.triggers.fire(
            self.id,
            payload=payload,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def __aenter__(self) -> AsyncTrigger:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncCatalogEntryInfo = Union[ActionCatalogRetrieveResponse, __types_workflows_action_catalog_list_response.Item]


class AsyncCatalogEntry:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncCatalogEntryInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncCatalogEntryInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", name={self.name!r}, service={self.service!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        profile: Literal["agent_routine"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCatalogRetrieveResponse:
        result = await self.api.workflows.action_catalog.retrieve(
            self.id,
            profile=profile,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "name"))

    @property
    def service(
        self,
    ) -> Union[Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[
                Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api"], None
            ],
            record_field(self.info, self._info_root, "service"),
        )

    async def __aenter__(self) -> AsyncCatalogEntry:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncWorkflowActionInfo = Union[
    ActionCreateResponse, ActionRetrieveResponse, __types_workflows_action_list_response.Item
]


class AsyncWorkflowAction:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncWorkflowActionInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncWorkflowActionInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", name={self.name!r}, service={self.service!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        profile: Literal["agent_routine"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        result = await self.api.workflows.actions.retrieve(
            self.id,
            profile=profile,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "name"))

    @property
    def service(
        self,
    ) -> Union[Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[
                Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api"], None
            ],
            record_field(self.info, self._info_root, "service"),
        )

    async def update(
        self,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        params: Dict[str, object] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ActionUpdateResponse:
        """
        Partially update an action's name, description, or params; all fields are
        optional. Returns 404 if the action does not exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.actions.update(
            self.id,
            description=description,
            name=name,
            params=params,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ActionDeleteResponse:
        """Delete an action by its ID. Returns 404 if no action matches."""
        result = await self.api.workflows.actions.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def __aenter__(self) -> AsyncWorkflowAction:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


class _AsyncFlowActions:
    def __init__(self, api: AsyncMobilerun, owner: AsyncFlow) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowsActionListResponse:
        """
        Return the ordered list of actions attached to a flow, including any nested
        child actions. Returns 404 if the flow does not exist.
        """
        result = await self.api.workflows.flows.actions.list(
            self._owner.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def add(
        self,
        *,
        action_id: str,
        position: int,
        children: Iterable[action_add_params.Child] | Omit = omit,
        continue_on_error: bool | Omit = omit,
        key: str | Omit = omit,
        name_override: str | Omit = omit,
        overrides: Optional[action_add_params.Overrides] | Omit = omit,
        parent_flow_action_id: Optional[str] | Omit = omit,
        recording_enabled: bool | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ActionAddResponse:
        """
        Append a single action to a flow at the given `position`, optionally nesting it
        under a `parentFlowActionId` or supplying its own `children`. Supports a
        `nameOverride`, param `overrides`, and `continueOnError`. Returns 404 if the
        flow does not exist.

        Supports an optional `Idempotency-Key` header (1-255 printable ASCII
        characters). Replays with the same key and an identical body return the original
        201; a changed body under the same key returns 422 `idempotency_key_reused`.

        Args:
          key: Stable identifier used by template resolution v2+ to address this step as
              {{key.field}}. Omitted keys are derived from the step name whenever a flow is
              created. For template resolution v3, replacing an existing flow's full action
              tree requires every step to carry an explicit key — a missing key is rejected
              there, not derived, so a name change can never silently move a step's key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.actions.add(
            self._owner.id,
            action_id=action_id,
            position=position,
            children=children,
            continue_on_error=continue_on_error,
            key=key,
            name_override=name_override,
            overrides=overrides,
            parent_flow_action_id=parent_flow_action_id,
            recording_enabled=recording_enabled,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def remove(
        self,
        flow_action_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ActionRemoveResponse:
        """Remove a single action from a flow by its `flowActionId`.

        Returns 404 if the
        flow or flow action does not exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.actions.remove(
            flow_action_id,
            flow_id=self._owner.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def replace(
        self,
        *,
        actions: Iterable[action_replace_params.Action],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ActionReplaceResponse:
        """
        Replace a flow's entire action list with the supplied set (at least one
        required). Each action references an `actionId` and a unique `position`, and may
        include nested `children`, a `nameOverride`, param `overrides`, and a
        `continueOnError` flag. Returns 404 if the flow does not exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.actions.replace(
            self._owner.id,
            actions=actions,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result


class _AsyncFlowState:
    def __init__(self, api: AsyncMobilerun, owner: AsyncFlow) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateListResponse:
        """
        List the keys a routine has saved with `state.save`, with the metadata of each
        key's newest version.
        """
        result = await self.api.workflows.flows.state.list(
            self._owner.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def delete(
        self,
        key: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> StateDeleteResponse:
        """Delete every version of one state key.

        The next `state.load` of the key reports
        `found: false`. Deleting an unknown key succeeds.

        Args:
          key: State key: 1–128 characters of letters, digits, ".", "\\__" or "-".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.state.delete(
            key,
            flow_id=self._owner.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def list_versions(
        self,
        key: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateListVersionsResponse:
        """
        Return the retained versions of one state key, newest first, including each
        saved value. An unknown key returns an empty list.

        Args:
          key: State key: 1–128 characters of letters, digits, ".", "\\__" or "-".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.workflows.flows.state.list_versions(
            key,
            flow_id=self._owner.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result


AsyncFlowInfo = Union[
    FlowCreateResponse, FlowRetrieveResponse, FlowCloneResponse, __types_workflows_flow_list_response.Item
]


class AsyncFlow:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncFlowInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncFlowInfo] = info
        self._info_root = info_root
        self._owned = owned
        owner = self
        self.actions = _AsyncFlowActions(api, owner)
        self.state = _AsyncFlowState(api, owner)

    @override
    def __repr__(self) -> str:
        fields = f", name={self.name!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowRetrieveResponse:
        result = await self.api.workflows.flows.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def name(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "name"))

    async def update(
        self,
        *,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        delivery: Optional[flow_update_params.Delivery] | Omit = omit,
        description: str | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        health_monitoring_enabled: bool | Omit = omit,
        lifecycle_status: Literal["enabled", "disabled"] | Omit = omit,
        name: str | Omit = omit,
        notify_on_failure: bool | Omit = omit,
        notify_on_success: bool | Omit = omit,
        notify_webhook_id: Optional[str] | Omit = omit,
        owner_wake: Literal["final", "off"] | Omit = omit,
        recording_enabled: bool | Omit = omit,
        recording_policy: flow_update_params.RecordingPolicy | Omit = omit,
        self_healing_enabled: bool | Omit = omit,
        self_healing_max_attempts: int | Omit = omit,
        trigger_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowUpdateResponse:
        """
        Partially update a flow's settings — name, trigger binding, enabled state,
        target devices, cooldown, or notifications; all fields are optional. Actions are
        managed through the flow-actions endpoints, not here. Returns 404 if the flow
        does not exist.

        Args:
          lifecycle_status: Set the visible agent lifecycle. Archive remains available only through DELETE.

          recording_enabled: Deprecated compatibility field. true maps to recordingPolicy.mode="flow"; false
              maps to "off".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.update(
            self.id,
            cooldown_scope=cooldown_scope,
            cooldown_seconds=cooldown_seconds,
            delivery=delivery,
            description=description,
            device_ids=device_ids,
            enabled=enabled,
            health_monitoring_enabled=health_monitoring_enabled,
            lifecycle_status=lifecycle_status,
            name=name,
            notify_on_failure=notify_on_failure,
            notify_on_success=notify_on_success,
            notify_webhook_id=notify_webhook_id,
            owner_wake=owner_wake,
            recording_enabled=recording_enabled,
            recording_policy=recording_policy,
            self_healing_enabled=self_healing_enabled,
            self_healing_max_attempts=self_healing_max_attempts,
            trigger_id=trigger_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowDeleteResponse:
        """Terminally archive a flow by its ID.

        Archived flows cannot be restored and are
        hidden from customer reads. Repeating the request is idempotent for the owner.
        """
        result = await self.api.workflows.flows.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def activate(
        self,
        *,
        verification_execution_id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowActivateResponse:
        """
        Activate a disabled flow only when the supplied verification execution succeeded
        and the flow graph has not changed since verification. Repeating activation is
        idempotent for an already-enabled flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.activate(
            self.id,
            verification_execution_id=verification_execution_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delivery_options(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowDeliveryOptionsResponse:
        """
        Return the recording/delivery readiness for a flow (recording mode, whether
        delivery can include the recording, whether a files.upload action exists, the
        first direct OneDrive/Google Drive upload step if any) plus, per destination,
        whether the flow owner has an active connection. Returns 404 if the flow does
        not exist.
        """
        result = await self.api.workflows.flows.delivery_options(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def dry_run(
        self,
        *,
        payload: Dict[str, object] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowDryRunResponse:
        """
        Simulate this flow firing without storing events, enqueuing jobs, or consuming
        cooldown/rate-limit slots.

        Works for every trigger activation type:

        - `event`: validates the payload against the event catalog schema and evaluates
          the trigger conditions.
        - `custom`: validates the payload against the custom payload schema (conditions
          do not apply).
        - `schedule`: validates the stored trigger payload and its step references, and
          reports the next fire time; request payload overrides are ignored.

        The response reports `wouldFire` — whether the flow would actually run right now
        — alongside the gates that decide it (enabled, device attached, blocked,
        cooldown). `rateLimited` is informational and is not folded into `wouldFire`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.dry_run(
            self.id,
            payload=payload,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def list_repairs(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowListRepairsResponse:
        """List self-healing repair episodes"""
        result = await self.api.workflows.flows.list_repairs(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        return result

    async def retrieve_repair(
        self,
        episode_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowRetrieveRepairResponse:
        """
        Get a self-healing repair episode

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.workflows.flows.retrieve_repair(
            episode_id,
            flow_id=self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def run(
        self,
        *,
        capture_screenshots: bool | Omit = omit,
        payload: Dict[str, object] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowRunResponse:
        """
        Immediately enqueue one live execution on every device bound to the flow,
        regardless of whether its trigger is event-based, custom, or scheduled.

        Supports an optional `Idempotency-Key` header (1-255 printable ASCII
        characters). The run identity is derived from the key, so a retry never starts a
        second run. Replays with the same key and an identical body return the original
        status and the original `executionIds`; a changed body under the same key
        returns 422 `idempotency_key_reused`.

        Args:
          capture_screenshots: Record and keep this run's scripts.run screenshots
              (device.screenshot(save=True)) even without flow delivery. Used for a one-off
              proof run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.run(
            self.id,
            capture_screenshots=capture_screenshots,
            payload=payload,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def unblock(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FlowUnblockResponse:
        """Clear a flow's blocked status after fixing the underlying issue.

        Idempotent —
        safe to call on already-healthy flows.
        """
        result = await self.api.workflows.flows.unblock(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def clone(
        self,
        *,
        device_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncFlow:
        """Create a copy of an existing flow, including its actions and settings.

        The
        optional body can override the new flow's `name` and target `deviceIds`. Returns
        404 if the source flow does not exist.

        Supports an optional `Idempotency-Key` header (1-255 printable ASCII
        characters). Replays with the same key and an identical body return the original
        201; a changed body under the same key returns 422 `idempotency_key_reused`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.clone(
            self.id,
            device_ids=device_ids,
            name=name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return AsyncFlow(self.api, result.data.id, result, info_root="data")

    async def verify(
        self,
        *,
        invocation_id: str,
        device_id: str | Omit = omit,
        payload: Dict[str, object] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncExecution:
        """Performs a real verification run on a device.


        Run a bound, deduplicated **verification** of this flow on exactly one device as
        a real run.

        Unlike a normal trigger firing, verification:

        - runs a flow that is `enabled` OR `disabled` (an archived flow returns 404);
        - targets one device (`deviceId`, or the single bound device);
        - is idempotent per `invocationId`: a repeat returns the existing run
          (`deduplicated: true`, HTTP 200) instead of enqueuing another (HTTP 202);
        - never mutates flow health, `lastTriggeredAt`, or the repair loop.

        Per-activation payload gate:

        - `custom`: validates the payload against the custom payload schema (422 on
          failure).
        - `event`: validates the payload against the event catalog schema and evaluates
          the trigger conditions; a failing gate returns 409 `conditions_not_met` with
          the dry-run report.
        - `schedule`: uses the stored trigger payload as event.payload; request payload
          overrides are ignored.

        Args:
          invocation_id: Client-supplied idempotency key. A repeat request for the same (flow,
              invocationId) returns the existing verification run (`deduplicated: true`,
              HTTP 200) instead of enqueuing another.

          device_id: Device to run the verification on. Must be one the flow is bound to. Optional
              only when the flow is bound to exactly one device (that device is used);
              otherwise required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.workflows.flows.verify(
            self.id,
            invocation_id=invocation_id,
            device_id=device_id,
            payload=payload,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return AsyncExecution(self.api, result.data.execution_id, result, info_root="data")

    async def __aenter__(self) -> AsyncFlow:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


class _AsyncExecutionScreenshots:
    def __init__(self, api: AsyncMobilerun, owner: AsyncExecution) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def retrieve(
        self,
        screenshot_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Redirects (302) to a freshly signed, time-limited image URL for a screenshot
        captured during this execution. Owner-gated: 404 if the execution or the
        screenshot does not belong to the caller.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self.api.workflows.executions.screenshots.retrieve(
            screenshot_id,
            execution_id=self._owner.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return None


AsyncExecutionInfo = Union[
    ExecutionRetrieveResponse, FlowVerifyResponse, __types_workflows_execution_list_response.Item
]


class AsyncExecution:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncExecutionInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncExecutionInfo] = info
        self._info_root = info_root
        self._owned = owned
        owner = self
        self.screenshots = _AsyncExecutionScreenshots(api, owner)

    @override
    def __repr__(self) -> str:
        fields = f", status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionRetrieveResponse:
        result = await self.api.workflows.executions.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def status(
        self,
    ) -> Union[Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"], None],
            record_field(self.info, self._info_root, "status"),
        )

    async def abort(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExecutionAbortResponse:
        """Stops the execution between steps and marks it cancelled.

        Idempotent-ish:
        already-terminal executions return 409.
        """
        result = await self.api.workflows.executions.abort(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def __aenter__(self) -> AsyncExecution:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncWebhookInfo = Union[WebhookCreateResponse, WebhookRetrieveResponse, __types_webhook_list_response.Item]


class AsyncWebhook:
    "info is the last create/get snapshot and may contain the create-time secret. Rotation revokes it and returns the new secret without updating info."

    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncWebhookInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncWebhookInfo] = info
        self._info_root = info_root
        self._owned = owned
        owner = self
        self.deliveries = AsyncWebhookDeliveryManager(api, owner.id)

    @override
    def __repr__(self) -> str:
        fields = f", url={self.url!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveResponse:
        result = await self.api.webhooks.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def url(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "url"))

    async def update(
        self,
        *,
        description: Optional[str] | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        state: Literal["ACTIVE", "DISABLED"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookUpdateResponse:
        """Updates a webhook subscription.

        Any combination of the subscribed event types,
        state (ACTIVE or DISABLED), and description may be changed, and at least one
        field must be supplied. Setting state to ACTIVE re-enables a subscription that
        was auto-blocked after sustained delivery failures. The URL or integration
        target cannot be changed; delete and recreate the webhook instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.webhooks.update(
            self.id,
            description=description,
            event_types=event_types,
            state=state,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Deletes a webhook subscription so it stops receiving deliveries.

        Returns 204 No
        Content on success.
        """
        await self.api.webhooks.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return None

    async def rotate_secret(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookRotateSecretResponse:
        """Rotates and revokes the old secret.

        The last create/get snapshot in info is preserved; any create-time secret in it is now revoked. Returns the new secret.



        Generates a new signing secret for the webhook subscription and returns it once
        in the response. The previous secret is replaced immediately, so any signature
        verification on your endpoint must be updated to use the new value. Only `http`
        webhooks have a signing secret; for `integration` webhooks this returns 400.
        """
        result = await self.api.webhooks.rotate_secret(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def test(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookTestDeliveryResponse:
        """
        Sends a single test payload to the webhook subscription URL (or a test message
        to its integration target) to verify connectivity. The response reports whether
        the attempt succeeded along with the returned HTTP status code or error, if any.
        """
        result = await self.api.webhooks.test_delivery(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def __aenter__(self) -> AsyncWebhook:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncWebhookDeliveryInfo = Union[
    DeliveryRetrieveAttemptsResponse, __types_webhooks_delivery_list_for_webhook_response.Item
]


class AsyncWebhookDelivery:
    def __init__(
        self,
        api: AsyncMobilerun,
        webhook_id: str,
        id: str,
        info: Optional[AsyncWebhookDeliveryInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self._webhook_id = webhook_id
        self.info: Optional[AsyncWebhookDeliveryInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    @property
    def webhook_id(self) -> str:
        return self._webhook_id

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRetrieveAttemptsResponse:
        result = await self.api.webhooks.deliveries.retrieve_attempts(
            self.id,
            id=self.webhook_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def status(self) -> Union[Literal["pending", "success", "skipped", "dead"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[Literal["pending", "success", "skipped", "dead"], None],
            record_field(self.info, self._info_root, "status"),
        )

    async def __aenter__(self) -> AsyncWebhookDelivery:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncMailboxInfo = Union[MailboxCreateResponse, MailboxRetrieveResponse, __types_mailbox_list_response.Item]


class AsyncMailbox:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncMailboxInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncMailboxInfo] = info
        self._info_root = info_root
        self._owned = owned
        owner = self
        self.messages = AsyncMailboxMessageManager(api, owner.id)

    @override
    def __repr__(self) -> str:
        fields = f", address={self.address!r}, status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxRetrieveResponse:
        result = await self.api.mailboxes.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def address(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "address"))

    @property
    def status(
        self,
    ) -> Union[
        Literal[
            "provisioning",
            "awaiting_payment",
            "active",
            "cancel_scheduled",
            "archived",
            "billing_error",
            "pending_connection",
            "connection_expired",
            "connection_removed",
        ],
        None,
    ]:
        """Reads the last response without making a request."""
        return cast(
            Union[
                Literal[
                    "provisioning",
                    "awaiting_payment",
                    "active",
                    "cancel_scheduled",
                    "archived",
                    "billing_error",
                    "pending_connection",
                    "connection_expired",
                    "connection_removed",
                ],
                None,
            ],
            record_field(self.info, self._info_root, "status"),
        )

    async def update(
        self,
        *,
        label: Optional[str],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MailboxUpdateResponse:
        """
        Updates the label of a mailbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.mailboxes.update(
            self.id,
            label=label,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MailboxDeleteResponse:
        """Cancels the mailbox rental or schedules cancellation for an active paid mailbox.

        Existing addresses and messages are retained.



        Cancels a pending mailbox or schedules an active paid mailbox for cancellation.
        Existing addresses and messages are retained. Repeating the request is safe. An
        external inbox (Gmail) cannot be cancelled here; disconnect the link instead.
        """
        result = await self.api.mailboxes.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def disconnect(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MailboxDisconnectResponse:
        """Removes only this mailbox link.

        The Gmail connection used by your agents stays
        in place.
        """
        result = await self.api.mailboxes.disconnect(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def otp(
        self,
        *,
        after: Union[str, datetime] | Omit = omit,
        max_length: int | Omit = omit,
        min_length: int | Omit = omit,
        sender: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxOtpResponse:
        """Returns the most likely recent OTP for the mailbox.

        Returns 204 when no matching
        code is available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.mailboxes.otp(
            self.id,
            after=after,
            max_length=max_length,
            min_length=min_length,
            sender=sender,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result

    async def restart(
        self,
        *,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MailboxRestartResponse:
        """Restarts a paid mailbox rental.

        Uses included capacity when available unless paid service is requested.


        Restarts an archived mailbox with the same address.

        Uses included capacity when
        available unless paid service is requested.

        Args:
          billing_preference: included uses package capacity when available and otherwise starts paid
              checkout; included_only fails without creating a paid reservation when no
              included slot remains; rent always starts paid checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.mailboxes.restart(
            self.id,
            billing_preference=billing_preference,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def uncancel(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MailboxUncancelResponse:
        """Withdraws a scheduled cancellation.

        Only available while cancellation is
        pending.
        """
        result = await self.api.mailboxes.uncancel(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def wait_for_otp(
        self,
        *,
        after: Union[str, datetime] | Omit = omit,
        max_length: int | Omit = omit,
        min_length: int | Omit = omit,
        sender: str | Omit = omit,
        timeout: float = 120,
        poll_interval: float = 1,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Data:
        """Only codes received after this wait started are considered unless after is passed. The comparison uses the client clock. Returns the OTP data including code, received time, sender, message ID and confidence; leaves info unchanged."""
        wait_start = datetime.now(timezone.utc)
        if isinstance(after, Omit):
            after = wait_start
        poll_api = self.api.with_options(max_retries=0)

        async def poll(remaining: float) -> Optional[MailboxOtpResponse]:
            async with poll_api.mailboxes.with_streaming_response.otp(
                self.id,
                after=after,
                max_length=max_length,
                min_length=min_length,
                sender=sender,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=remaining,
            ) as response:
                data = await response.read()
                if response.status_code == 204 or not data:
                    return None
                result = await response.parse()
            return result

        result = await wait_async(
            poll,
            lambda status: "ready" if condition_met(read_path(status, ["data", "code"]), "non_empty") else "pending",
            ["ready"],
            [],
            pending=["pending"],
            timeout=timeout,
            poll_interval=poll_interval,
            poll_request_timeout=30,
        )
        return cast(Data, read_path(result, ["data"]))

    async def __aenter__(self) -> AsyncMailbox:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncMailboxConnectionInfo = Union[ConnectionCreateResponse, ConnectionRetrieveResponse]


class AsyncMailboxConnection:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncMailboxConnectionInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncMailboxConnectionInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", address={self.address!r}, status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveResponse:
        result = await self.api.mailboxes.connections.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = ""
        return result

    @property
    def address(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "address"))

    @property
    def status(self) -> Union[Literal["pending", "active", "expired", "removed"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[Literal["pending", "active", "expired", "removed"], None],
            record_field(self.info, self._info_root, "status"),
        )

    async def __aenter__(self) -> AsyncMailboxConnection:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncMailboxMessageInfo = Union[MailboxesMessageRetrieveResponse, __types_mailboxes_message_list_response.Item]


class AsyncMailboxMessage:
    def __init__(
        self,
        api: AsyncMobilerun,
        mailbox_id: str,
        id: str,
        info: Optional[AsyncMailboxMessageInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self._mailbox_id = mailbox_id
        self.info: Optional[AsyncMailboxMessageInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", subject={self.subject!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    @property
    def mailbox_id(self) -> str:
        return self._mailbox_id

    async def refresh(
        self,
        *,
        include_html: Literal["true", "false"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxesMessageRetrieveResponse:
        result = await self.api.mailboxes.messages.retrieve(
            self.id,
            mailbox_id=self.mailbox_id,
            include_html=include_html,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def subject(self) -> Union[str, None]:
        """Reads the last response without making a request."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "subject"))

    async def __aenter__(self) -> AsyncMailboxMessage:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncAgentFileInfo = Union[FileConfirmResponse, __types_file_list_response.File, __types_agents_file_list_response.File]


class AsyncAgentFile:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncAgentFileInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncAgentFileInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", filename={self.filename!r}, display_name={self.display_name!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    @property
    def filename(self) -> Union[str, None]:
        """Reads only the last create/list snapshot without making a request; fromId/from_id handles have no data."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "filename"))

    @property
    def display_name(self) -> Union[str, None]:
        """Reads only the last create/list snapshot without making a request; fromId/from_id handles have no data."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "displayName"))

    async def update(
        self,
        *,
        display_name: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FileUpdateResponse:
        """Partial update of `displayName` and/or `enabled`.

        Only files with `zone=skills`
        are mutable; other zones return 422 `unsupported_zone`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.files.update(
            self.id,
            display_name=display_name,
            enabled=enabled,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FileDeleteResponse:
        """Hard-delete a file."""
        result = await self.api.files.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def cancel_pending(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FileCancelPendingResponse:
        """
        Soft-cancels an in-flight upload before confirm, transitioning it to expired and
        deleting the underlying object. Only acts on `pending` uploads — refuses to
        touch `ready` files, so confirmed files are never removed. Idempotent:
        `{ cancelled: false }` if the file exists but is no longer pending.
        """
        result = await self.api.files.cancel_pending(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def confirm(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FileConfirmResponse:
        """
        Confirm a file upload after validating the stored object with a server-side HEAD
        request.
        """
        result = await self.api.files.confirm(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def download(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> bytes:
        async with self.api.files.with_streaming_response.download(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        ) as response:
            data = await response.read()
            return data

    async def __aenter__(self) -> AsyncAgentFile:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


class _AsyncAgentFiles:
    def __init__(self, api: AsyncMobilerun, owner: AsyncAgent) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def list(
        self,
        *,
        zone: Literal["user", "agent", "workflow", "skills"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncAgentFile, AgentsFileListResponse]:
        async def load() -> AsyncObjectPage[AsyncAgentFile, AgentsFileListResponse]:
            __page = await self.api.agents.files.list(
                self._owner.id,
                zone=zone,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncAgentFile(self.api, item.file_id, item, info_root="") for item in (__page.files or [])], __page
            )

        return AsyncObjectPager(load)


class _AsyncAgentConversations:
    def __init__(self, api: AsyncMobilerun, owner: AsyncAgent) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def create(
        self,
        *,
        title: str,
        agent: str | Omit = omit,
        description: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ConversationCreateResponse:
        """Create a named chat session bound to one agent.

        Idempotent via the
        `Idempotency-Key` header, like the unscoped create.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.agents.conversations.create(
            self._owner.id,
            title=title,
            agent=agent,
            description=description,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def list(
        self,
        *,
        kind: Literal["chat", "agent_workflow"] | Omit = omit,
        mine: Literal["true", "false"] | Omit = omit,
        workflow_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentsConversationListResponse:
        """List the user's named chat sessions for one agent.

        Supports the same `kind`,
        `workflowId` and `mine` filters as the unscoped list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        result = await self.api.agents.conversations.list(
            self._owner.id,
            kind=kind,
            mine=mine,
            workflow_id=workflow_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return result


class _AsyncAgentRequests:
    def __init__(self, api: AsyncMobilerun, owner: AsyncAgent) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def list_for_agent(
        self,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncAgentRequest, RequestListForAgentResponse]:
        async def load() -> AsyncObjectPage[AsyncAgentRequest, RequestListForAgentResponse]:
            __page = await self.api.agents.requests.list_for_agent(
                self._owner.id,
                before=before,
                limit=limit,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncAgentRequest(self.api, item.id, item, info_root="") for item in (__page.requests or [])], __page
            )

        return AsyncObjectPager(load)


class _AsyncAgentRoutines:
    def __init__(self, api: AsyncMobilerun, owner: AsyncAgent) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def create(
        self,
        *,
        actions: Iterable[routine_create_params.Action],
        name: str,
        trigger_id: str,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        delivery: routine_create_params.Delivery | Omit = omit,
        description: str | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        health_monitoring_enabled: bool | Omit = omit,
        notify_on_failure: bool | Omit = omit,
        notify_on_success: bool | Omit = omit,
        notify_webhook_id: Optional[str] | Omit = omit,
        recording_enabled: bool | Omit = omit,
        recording_policy: routine_create_params.RecordingPolicy | Omit = omit,
        self_healing_enabled: bool | Omit = omit,
        self_healing_max_attempts: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RoutineCreateResponse:
        """
        Forwards the scheduler CreateFlowBody unchanged and assigns the Agent selected
        in the path. Requires Idempotency-Key; reuse it after a transient failure.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.agents.routines.create(
            self._owner.id,
            actions=actions,
            name=name,
            trigger_id=trigger_id,
            cooldown_scope=cooldown_scope,
            cooldown_seconds=cooldown_seconds,
            delivery=delivery,
            description=description,
            device_ids=device_ids,
            enabled=enabled,
            health_monitoring_enabled=health_monitoring_enabled,
            notify_on_failure=notify_on_failure,
            notify_on_success=notify_on_success,
            notify_webhook_id=notify_webhook_id,
            recording_enabled=recording_enabled,
            recording_policy=recording_policy,
            self_healing_enabled=self_healing_enabled,
            self_healing_max_attempts=self_healing_max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def clone(
        self,
        routine_id: str,
        *,
        device_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RoutineCloneResponse:
        """
        The source must belong to the authenticated owner and be assigned to the same
        Agent or unassigned. The target is the Agent in the path. Requires
        Idempotency-Key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.agents.routines.clone(
            routine_id,
            agent_id=self._owner.id,
            device_ids=device_ids,
            name=name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result


class _AsyncAgentProfile:
    def __init__(self, api: AsyncMobilerun, owner: AsyncAgent) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    async def update(
        self,
        *,
        avatar_config: Optional[profile_update_params.AvatarConfig] | Omit = omit,
        avatar_kind: Optional[Literal["blob"]] | Omit = omit,
        color: Optional[
            Literal[
                "slate", "red", "orange", "amber", "lime", "green", "teal", "cyan", "blue", "indigo", "violet", "pink"
            ]
        ]
        | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        model_profile: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncAgent:
        """
        Owner-scoped partial update of `displayName`, `instructions`, `modelProfile` and
        the avatar. A null modelProfile uses the environment default; an unknown id
        returns unknown_model_profile with details.validProfiles. Returns the updated
        Agent; an Agent of another owner or an unknown id is a 404.

        Args:
          color: Set the avatar palette color without changing its seed; null removes only the
              color. Omitted color stays unchanged, including during a seed update.

          display_name: Single-line name shown for the Agent; surrounding whitespace is trimmed and it
              needs at least one letter or number.

          instructions: The Agent's individual instructions passage; an empty or whitespace-only text
              clears it. Line breaks count three characters toward the rendered size limit.

          model_profile: Model profile id from GET /agents/model-profiles; null uses the environment
              default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.agents.profile.update(
            self._owner.id,
            avatar_config=avatar_config,
            avatar_kind=avatar_kind,
            color=color,
            display_name=display_name,
            instructions=instructions,
            model_profile=model_profile,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return AsyncAgent(self.api, result.id, result, info_root="")


AsyncAgentInfo = Union[AgentCreateResponse, ProfileUpdateResponse, __types_agent_list_response.Agent]


class AsyncAgent:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncAgentInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "agent",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncAgentInfo] = info
        self._info_root = info_root
        self._owned = owned
        owner = self
        self.files = _AsyncAgentFiles(api, owner)
        self.conversations = _AsyncAgentConversations(api, owner)
        self.requests = _AsyncAgentRequests(api, owner)
        self.routines = _AsyncAgentRoutines(api, owner)
        self.profile = _AsyncAgentProfile(api, owner)

    @override
    def __repr__(self) -> str:
        fields = f", display_name={self.display_name!r}, status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    @property
    def display_name(self) -> Union[str, None]:
        """Reads only the last create/list snapshot without making a request; fromId/from_id handles have no data."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "profile.displayName"))

    @property
    def status(self) -> Union[Literal["active", "pending", "failed", "archived", "disabled"], None]:
        """Reads only the last create/list snapshot without making a request; fromId/from_id handles have no data."""
        return cast(
            Union[Literal["active", "pending", "failed", "archived", "disabled"], None],
            record_field(self.info, self._info_root, "status"),
        )

    async def __aenter__(self) -> AsyncAgent:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncAgentRequestInfo = Union[
    RequestRetrieveResponse,
    RequestRetrieveBySessionResponse,
    __types_agents_request_list_for_agent_response.Request,
    __types_agents_request_list_response.Request,
]


class AsyncAgentRequest:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncAgentRequestInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncAgentRequestInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", status={self.status!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestRetrieveResponse:
        result = await self.api.agents.requests.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = ""
        return result

    @property
    def status(
        self,
    ) -> Union[
        Literal["queued", "running", "answered", "failed", "timed_out", "cancelled", "late_answer", "needs_user_input"],
        None,
    ]:
        """Reads the last response without making a request."""
        return cast(
            Union[
                Literal[
                    "queued",
                    "running",
                    "answered",
                    "failed",
                    "timed_out",
                    "cancelled",
                    "late_answer",
                    "needs_user_input",
                ],
                None,
            ],
            record_field(self.info, self._info_root, "status"),
        )

    async def __aenter__(self) -> AsyncAgentRequest:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncNumberMessageInfo = Union[
    TypesMessageRetrieveResponse,
    MessageSendResponse,
    __types_message_list_response.Item,
    __types_numbers_message_list_response.Item,
]


class AsyncNumberMessage:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncNumberMessageInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncNumberMessageInfo] = info
        self._info_root = info_root
        self._owned = owned

    @override
    def __repr__(self) -> str:
        fields = f", status={self.status!r}, direction={self.direction!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypesMessageRetrieveResponse:
        result = await self.api.messages.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def status(
        self,
    ) -> Union[
        Literal["received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"], None
    ]:
        """Reads the last response without making a request."""
        return cast(
            Union[
                Literal["received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"],
                None,
            ],
            record_field(self.info, self._info_root, "status"),
        )

    @property
    def direction(self) -> Union[Literal["inbound", "outbound"], None]:
        """Reads the last response without making a request."""
        return cast(Union[Literal["inbound", "outbound"], None], record_field(self.info, self._info_root, "direction"))

    async def __aenter__(self) -> AsyncNumberMessage:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


class _AsyncPhoneNumberMessages:
    def __init__(self, api: AsyncMobilerun, owner: AsyncPhoneNumber) -> None:
        self.api = api
        self._owner = owner

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def list(
        self,
        *,
        direction: Literal["all", "inbound", "outbound"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncObjectPager[AsyncNumberMessage, NumbersMessageListResponse]:
        async def load(__number: int) -> AsyncObjectPage[AsyncNumberMessage, NumbersMessageListResponse]:
            __page = await self.api.numbers.messages.list(
                self._owner.id,
                direction=direction,
                page=page,
                page_size=page_size,
                since=since,
                extra_headers=extra_headers,
                extra_query=bound_extra(extra_query, {"page": __number}),
                extra_body=extra_body,
                timeout=timeout,
            )
            return AsyncObjectPage(
                [AsyncNumberMessage(self.api, item.id, item, info_root="") for item in (__page.items or [])],
                __page,
                lambda: next_object_page(
                    __page.pagination.page, __page.pagination.has_next, __page.pagination.pages, __number
                ),
                load,
            )

        return AsyncObjectPager(lambda: load(int(page) if isinstance(page, (int, float)) else 1))


AsyncPhoneNumberInfo = Union[NumberCreateResponse, TypesNumberRetrieveResponse, __types_number_list_response.Item]


class AsyncPhoneNumber:
    def __init__(
        self,
        api: AsyncMobilerun,
        id: str,
        info: Optional[AsyncPhoneNumberInfo] = None,
        *,
        owned: bool = False,
        info_root: str = "data",
    ) -> None:
        self.api = api
        self.id = id
        self.info: Optional[AsyncPhoneNumberInfo] = info
        self._info_root = info_root
        self._owned = owned
        owner = self
        self.messages = _AsyncPhoneNumberMessages(api, owner)

    @override
    def __repr__(self) -> str:
        fields = f", phone_number={self.phone_number!r}, state={self.state!r}" if self.info is not None else ""
        return f"{self.__class__.__name__}(id={self.id!r}{fields})"

    async def refresh(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypesNumberRetrieveResponse:
        result = await self.api.numbers.retrieve(
            self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        self.info = result
        self._info_root = "data"
        return result

    @property
    def phone_number(self) -> Union[str, None]:
        """Not available on handles from `numbers.create()` until `refresh()`."""
        return cast(Union[str, None], record_field(self.info, self._info_root, "phoneNumber"))

    @property
    def state(
        self,
    ) -> Union[Literal["awaiting_payment", "provisioning", "active", "cancel_scheduled", "expired", "failed"], None]:
        """Reads the last response without making a request."""
        return cast(
            Union[Literal["awaiting_payment", "provisioning", "active", "cancel_scheduled", "expired", "failed"], None],
            record_field(self.info, self._info_root, "state"),
        )

    async def update(
        self,
        *,
        label: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NumberUpdateResponse:
        """Updates the display label.

        Omitting `label` leaves it unchanged; null or an
        empty string clears it.

        Args:
          label: User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
              code units; an emoji/flag may span several). Display-only, never used for
              routing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.numbers.update(
            self.id,
            label=label,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def delete(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NumberDeleteResponse:
        """Cancels the phone number rental.


        Cancels a pending purchase or schedules cancellation of an active paid phone
        number. Repeating a scheduled cancellation is safe. Returns 409 when
        cancellation is not available.
        """
        result = await self.api.numbers.delete(
            self.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return result

    async def send(
        self,
        *,
        body: str,
        to: str,
        delivery_report: bool | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AsyncNumberMessage:
        """Queues an SMS from one of the caller's numbers that can send.

        Replaying an
        Idempotency-Key with the same payload returns the original message, reusing it
        with a different payload returns 422. 409 capability_unavailable: this number
        cannot send right now. 422 invalid_recipient / unsupported_destination /
        body_too_long: the recipient or text does not fit the number. 429
        daily_limit_reached: the rolling 24 h limit for the account is used up; 429
        rate_limited: too many sends by the owner in a short window; 429
        number_rate_limited: too many outbound sends from this number in the configured
        window (all sends from this number count, including those made on your behalf).
        403 send_disabled: self-service SMS send is switched off;
        outbound_sms_not_granted: outbound SMS requires an admin grant.

        Args:
          body: SMS body text, up to 1600 characters (longer bodies are rejected with 400). A
              number's own limit may be lower and is answered 422 body_too_long.

          to: Recipient phone number, as E.164 or a US 10/11-digit number. Destinations the
              number cannot send to are rejected with 422 unsupported_destination, non-numbers
              with 422 invalid_recipient.

          delivery_report: Deprecated: best effort and ignored on most lines. Hosted SIM numbers return no
              carrier delivery report, so their messages end at `sent` and no
              `sms.send.delivered` event follows. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        result = await self.api.numbers.messages.send(
            self.id,
            body=body,
            to=to,
            delivery_report=delivery_report,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
            idempotency_key=idempotency_key,
        )
        return AsyncNumberMessage(self.api, result.data.id, result, info_root="data")

    async def wait_until_active(
        self,
        *,
        timeout: float = 300,
        poll_interval: float = 1,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> TypesNumberRetrieveResponse:
        """Wait for the number to become active. awaiting_payment means checkout is not completed; the last response carried by WaitFailureError includes the checkout URL in data.checkoutUrl (data.checkout_url in Python)."""

        poll_api = self.api.with_options(max_retries=0)

        async def poll(remaining: float) -> TypesNumberRetrieveResponse:
            result = await poll_api.numbers.retrieve(
                self.id, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=remaining
            )
            self.info = result
            self._info_root = "data"
            return result

        result = await wait_async(
            poll,
            lambda status: status.data.state,
            ["active", "cancel_scheduled"],
            ["expired", "failed", "awaiting_payment"],
            pending=["provisioning"],
            timeout=timeout,
            poll_interval=poll_interval,
            poll_request_timeout=30,
        )
        return result

    async def __aenter__(self) -> AsyncPhoneNumber:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[builtins.type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None


AsyncAppListPage = AsyncObjectPage[AsyncApp, TypesAppListResponse]
AsyncCredentialPackageListPage = ObjectPage[AsyncCredentialPackage, PackageListAllResponse]
AsyncCredentialListPage = ObjectPage[AsyncCredential, CredentialsPackageListResponse]
AsyncDeviceListPage = AsyncObjectPage[AsyncDevice, DeviceListResponse]
AsyncSavedScreenshotListPage = AsyncObjectPage[AsyncSavedScreenshot, DevicesScreenshotListResponse]
AsyncRecordingListPage = ObjectPage[AsyncRecording, Optional[RecordingListResponse]]
AsyncTrafficSessionListPage = AsyncObjectPage[AsyncTrafficSession, TrafficSessionListResponse]
AsyncProxyConfigurationListPage = ObjectPage[AsyncProxyConfiguration, TypesProxyListResponse]
AsyncConnectProxyListPage = AsyncObjectPage[AsyncConnectProxy, ConnectProxyListResponse]
AsyncConnectUserListPage = AsyncObjectPage[AsyncConnectUser, UserListResponse]
AsyncTaskListPage = AsyncObjectPage[AsyncTask, TypesTaskListResponse]
AsyncTriggerListPage = AsyncObjectPage[AsyncTrigger, TriggerListResponse]
AsyncCatalogEntryListPage = AsyncObjectPage[AsyncCatalogEntry, ActionCatalogListResponse]
AsyncWorkflowActionListPage = AsyncObjectPage[AsyncWorkflowAction, WorkflowsActionListResponse]
AsyncFlowListPage = AsyncObjectPage[AsyncFlow, FlowListResponse]
AsyncExecutionListPage = AsyncObjectPage[AsyncExecution, ExecutionListResponse]
AsyncWebhookListPage = AsyncObjectPage[AsyncWebhook, WebhookListResponse]
AsyncWebhookDeliveryListPage = AsyncObjectPage[AsyncWebhookDelivery, DeliveryListForWebhookResponse]
AsyncMailboxListPage = AsyncObjectPage[AsyncMailbox, MailboxListResponse]
AsyncMailboxMessageListPage = AsyncObjectPage[AsyncMailboxMessage, MailboxesMessageListResponse]
AsyncAgentFileListPage = ObjectPage[AsyncAgentFile, TypesFileListResponse]
AsyncAgentListPage = ObjectPage[AsyncAgent, AgentListResponse]
AsyncAgentRequestListPage = ObjectPage[AsyncAgentRequest, RequestListResponse]
AsyncNumberMessageListPage = AsyncObjectPage[AsyncNumberMessage, TypesMessageListResponse]
AsyncPhoneNumberListPage = AsyncObjectPage[AsyncPhoneNumber, NumberListResponse]
