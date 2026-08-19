# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

import os

from ._streaming import AsyncStream as AsyncStream, Stream as Stream

from ._types import NotGiven, not_given

from typing import Mapping, Any

from ._utils import is_mapping_t, get_async_library

from ._compat import cached_property

from typing_extensions import override, Self

from ._exceptions import APIStatusError

from . import _exceptions

import os
import asyncio
from typing_extensions import Literal

import httpx

from ._version import __version__
from ._qs import Querystring
from ._utils import maybe_coerce_integer, maybe_coerce_float, maybe_coerce_boolean, is_given
from ._types import Omit, Timeout, Transport, ProxiesTypes, RequestOptions, Headers, NoneType, Query, Body
from ._base_client import (
    DEFAULT_CONNECTION_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    ResponseT,
    SyncHttpxClientWrapper,
    AsyncHttpxClientWrapper,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .resources import apps
  from .resources import carriers
  from .resources import credentials
  from .resources import devices
  from .resources import models
  from .resources import profiles
  from .resources import proxies
  from .resources import connect
  from .resources import tasks
  from .resources import workflows
  from .resources import webhooks
  from .resources import agents
  from .resources import app_events
  from .resources import notifications
  from .resources import esims
  from .resources import messages
  from .resources import numbers
  from .resources import store
  from .resources import apps
  from .resources import carriers
  from .resources import credentials
  from .resources import devices
  from .resources import models
  from .resources import profiles
  from .resources import proxies
  from .resources import connect
  from .resources import tasks
  from .resources import workflows
  from .resources import webhooks
  from .resources import agents
  from .resources import app_events
  from .resources import notifications
  from .resources import esims
  from .resources import messages
  from .resources import numbers
  from .resources import store
  from .resources import apps
  from .resources import carriers
  from .resources import credentials
  from .resources import devices
  from .resources import models
  from .resources import profiles
  from .resources import proxies
  from .resources import connect
  from .resources import tasks
  from .resources import workflows
  from .resources import webhooks
  from .resources import agents
  from .resources import app_events
  from .resources import notifications
  from .resources import esims
  from .resources import messages
  from .resources import numbers
  from .resources import store
  from .resources import apps
  from .resources import carriers
  from .resources import credentials
  from .resources import devices
  from .resources import models
  from .resources import profiles
  from .resources import proxies
  from .resources import connect
  from .resources import tasks
  from .resources import workflows
  from .resources import webhooks
  from .resources import agents
  from .resources import app_events
  from .resources import notifications
  from .resources import esims
  from .resources import messages
  from .resources import numbers
  from .resources import store
  from .resources.apps import AppsResource, AsyncAppsResource
  from .resources.carriers import CarriersResource, AsyncCarriersResource
  from .resources.credentials.credentials import CredentialsResource, AsyncCredentialsResource
  from .resources.devices.devices import DevicesResource, AsyncDevicesResource
  from .resources.models import ModelsResource, AsyncModelsResource
  from .resources.profiles import ProfilesResource, AsyncProfilesResource
  from .resources.proxies import ProxiesResource, AsyncProxiesResource
  from .resources.connect.connect import ConnectResource, AsyncConnectResource
  from .resources.tasks.tasks import TasksResource, AsyncTasksResource
  from .resources.workflows.workflows import WorkflowsResource, AsyncWorkflowsResource
  from .resources.webhooks.webhooks import WebhooksResource, AsyncWebhooksResource
  from .resources.agents import AgentsResource, AsyncAgentsResource
  from .resources.app_events.app_events import AppEventsResource, AsyncAppEventsResource
  from .resources.notifications import NotificationsResource, AsyncNotificationsResource
  from .resources.esims.esims import EsimsResource, AsyncEsimsResource
  from .resources.messages.messages import MessagesResource, AsyncMessagesResource
  from .resources.numbers.numbers import NumbersResource, AsyncNumbersResource
  from .resources.store.store import StoreResource, AsyncStoreResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Mobilerun", "AsyncMobilerun", "Client", "AsyncClient"]

class Mobilerun(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(self, *, api_key: str | None = None, base_url: str | httpx.URL | None = None, timeout: float | Timeout | None | NotGiven = not_given, max_retries: int = DEFAULT_MAX_RETRIES, default_headers: Mapping[str, str] | None = None, default_query: Mapping[str, object] | None = None,
    # Configure a custom httpx client.
    # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
    # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
    http_client: httpx.Client | None = None,
    # Enable or disable schema validation for data returned by the API.
    # When enabled an error APIResponseValidationError is raised
    # if the API responds with invalid data for the expected schema.
    #
    # This parameter may be removed or changed in the future.
    # If you rely on this feature, please open a GitHub issue
    # outlining your use-case to help us decide if it should be
    # part of our public interface in the future.
    _strict_response_validation: bool = False) -> None:
        """Construct a new synchronous Mobilerun client instance.

        This automatically infers the `api_key` argument from the `MOBILERUN_CLOUD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
          api_key = os.environ.get("MOBILERUN_CLOUD_API_KEY")
        self.api_key = api_key

        if base_url is None:
          base_url = os.environ.get("MOBILERUN_BASE_URL")
        if base_url is None:
          base_url = f"https://api.mobilerun.ai/v1"

        custom_headers_env = os.environ.get("MOBILERUN_CUSTOM_HEADERS")
        if custom_headers_env is not None:
          parsed: dict[str, str] = {}
          for line in custom_headers_env.split('\n'):
            colon = line.find(':')
            if colon >= 0:
              parsed[line[:colon].strip()] = line[colon + 1:].strip()
          default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(version=__version__, base_url=base_url, max_retries=max_retries, timeout=timeout, http_client=http_client, custom_headers=default_headers, custom_query=default_query, _strict_response_validation=_strict_response_validation)

    @cached_property
    def apps(self) -> AppsResource:
        from .resources.apps import AppsResource
        return AppsResource(self)

    @cached_property
    def carriers(self) -> CarriersResource:
        from .resources.carriers import CarriersResource
        return CarriersResource(self)

    @cached_property
    def credentials(self) -> CredentialsResource:
        from .resources.credentials import CredentialsResource
        return CredentialsResource(self)

    @cached_property
    def devices(self) -> DevicesResource:
        from .resources.devices import DevicesResource
        return DevicesResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        """LLM Models"""
        from .resources.models import ModelsResource
        return ModelsResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        from .resources.profiles import ProfilesResource
        return ProfilesResource(self)

    @cached_property
    def proxies(self) -> ProxiesResource:
        from .resources.proxies import ProxiesResource
        return ProxiesResource(self)

    @cached_property
    def connect(self) -> ConnectResource:
        from .resources.connect import ConnectResource
        return ConnectResource(self)

    @cached_property
    def tasks(self) -> TasksResource:
        """Tasks API"""
        from .resources.tasks import TasksResource
        return TasksResource(self)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        from .resources.workflows import WorkflowsResource
        return WorkflowsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource
        return WebhooksResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource
        return AgentsResource(self)

    @cached_property
    def app_events(self) -> AppEventsResource:
        from .resources.app_events import AppEventsResource
        return AppEventsResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        from .resources.notifications import NotificationsResource
        return NotificationsResource(self)

    @cached_property
    def esims(self) -> EsimsResource:
        from .resources.esims import EsimsResource
        return EsimsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource
        return MessagesResource(self)

    @cached_property
    def numbers(self) -> NumbersResource:
        from .resources.numbers import NumbersResource
        return NumbersResource(self)

    @cached_property
    def store(self) -> StoreResource:
        from .resources.store import StoreResource
        return StoreResource(self)

    @cached_property
    def with_raw_response(self) -> MobilerunWithRawResponse:
        return MobilerunWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MobilerunWithStreamedResponse:
        return MobilerunWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {
            "Authorization": f"Bearer {api_key}"
        }

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
          **super().default_headers,
          "X-Stainless-Async": "false",
          **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
          return

        raise TypeError("\"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted\"")

    def copy(self, *, api_key: str | None = None, base_url: str | httpx.URL | None = None, timeout: float | Timeout | None | NotGiven = not_given, http_client: httpx.Client | None = None, max_retries: int | NotGiven = not_given, default_headers: Mapping[str, str] | None = None, set_default_headers: Mapping[str, str] | None = None, default_query: Mapping[str, object] | None = None, set_default_query: Mapping[str, object] | None = None, _extra_kwargs: Mapping[str, Any] = {}) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
          raise ValueError(
            'The `default_headers` and `set_default_headers` arguments are mutually exclusive'
          )

        if default_query is not None and set_default_query is not None:
          raise ValueError(
            'The `default_query` and `set_default_query` arguments are mutually exclusive'
          )

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(api_key = api_key or self.api_key, base_url=base_url or self.base_url, timeout=self.timeout if isinstance(timeout, NotGiven) else timeout, http_client=http_client, max_retries=max_retries if is_given(max_retries) else self.max_retries, default_headers=headers, default_query=params, **_extra_kwargs)

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response,) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)

class AsyncMobilerun(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(self, *, api_key: str | None = None, base_url: str | httpx.URL | None = None, timeout: float | Timeout | None | NotGiven = not_given, max_retries: int = DEFAULT_MAX_RETRIES, default_headers: Mapping[str, str] | None = None, default_query: Mapping[str, object] | None = None,
    # Configure a custom httpx client.
    # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
    # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
    http_client: httpx.AsyncClient | None = None,
    # Enable or disable schema validation for data returned by the API.
    # When enabled an error APIResponseValidationError is raised
    # if the API responds with invalid data for the expected schema.
    #
    # This parameter may be removed or changed in the future.
    # If you rely on this feature, please open a GitHub issue
    # outlining your use-case to help us decide if it should be
    # part of our public interface in the future.
    _strict_response_validation: bool = False) -> None:
        """Construct a new async AsyncMobilerun client instance.

        This automatically infers the `api_key` argument from the `MOBILERUN_CLOUD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
          api_key = os.environ.get("MOBILERUN_CLOUD_API_KEY")
        self.api_key = api_key

        if base_url is None:
          base_url = os.environ.get("MOBILERUN_BASE_URL")
        if base_url is None:
          base_url = f"https://api.mobilerun.ai/v1"

        custom_headers_env = os.environ.get("MOBILERUN_CUSTOM_HEADERS")
        if custom_headers_env is not None:
          parsed: dict[str, str] = {}
          for line in custom_headers_env.split('\n'):
            colon = line.find(':')
            if colon >= 0:
              parsed[line[:colon].strip()] = line[colon + 1:].strip()
          default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(version=__version__, base_url=base_url, max_retries=max_retries, timeout=timeout, http_client=http_client, custom_headers=default_headers, custom_query=default_query, _strict_response_validation=_strict_response_validation)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        from .resources.apps import AsyncAppsResource
        return AsyncAppsResource(self)

    @cached_property
    def carriers(self) -> AsyncCarriersResource:
        from .resources.carriers import AsyncCarriersResource
        return AsyncCarriersResource(self)

    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        from .resources.credentials import AsyncCredentialsResource
        return AsyncCredentialsResource(self)

    @cached_property
    def devices(self) -> AsyncDevicesResource:
        from .resources.devices import AsyncDevicesResource
        return AsyncDevicesResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        """LLM Models"""
        from .resources.models import AsyncModelsResource
        return AsyncModelsResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        from .resources.profiles import AsyncProfilesResource
        return AsyncProfilesResource(self)

    @cached_property
    def proxies(self) -> AsyncProxiesResource:
        from .resources.proxies import AsyncProxiesResource
        return AsyncProxiesResource(self)

    @cached_property
    def connect(self) -> AsyncConnectResource:
        from .resources.connect import AsyncConnectResource
        return AsyncConnectResource(self)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        """Tasks API"""
        from .resources.tasks import AsyncTasksResource
        return AsyncTasksResource(self)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        from .resources.workflows import AsyncWorkflowsResource
        return AsyncWorkflowsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource
        return AsyncWebhooksResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource
        return AsyncAgentsResource(self)

    @cached_property
    def app_events(self) -> AsyncAppEventsResource:
        from .resources.app_events import AsyncAppEventsResource
        return AsyncAppEventsResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        from .resources.notifications import AsyncNotificationsResource
        return AsyncNotificationsResource(self)

    @cached_property
    def esims(self) -> AsyncEsimsResource:
        from .resources.esims import AsyncEsimsResource
        return AsyncEsimsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource
        return AsyncMessagesResource(self)

    @cached_property
    def numbers(self) -> AsyncNumbersResource:
        from .resources.numbers import AsyncNumbersResource
        return AsyncNumbersResource(self)

    @cached_property
    def store(self) -> AsyncStoreResource:
        from .resources.store import AsyncStoreResource
        return AsyncStoreResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMobilerunWithRawResponse:
        return AsyncMobilerunWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMobilerunWithStreamedResponse:
        return AsyncMobilerunWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {
            "Authorization": f"Bearer {api_key}"
        }

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
          **super().default_headers,
          "X-Stainless-Async": f'async:{get_async_library()}',
          **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
          return

        raise TypeError("\"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted\"")

    def copy(self, *, api_key: str | None = None, base_url: str | httpx.URL | None = None, timeout: float | Timeout | None | NotGiven = not_given, http_client: httpx.AsyncClient | None = None, max_retries: int | NotGiven = not_given, default_headers: Mapping[str, str] | None = None, set_default_headers: Mapping[str, str] | None = None, default_query: Mapping[str, object] | None = None, set_default_query: Mapping[str, object] | None = None, _extra_kwargs: Mapping[str, Any] = {}) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
          raise ValueError(
            'The `default_headers` and `set_default_headers` arguments are mutually exclusive'
          )

        if default_query is not None and set_default_query is not None:
          raise ValueError(
            'The `default_query` and `set_default_query` arguments are mutually exclusive'
          )

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(api_key = api_key or self.api_key, base_url=base_url or self.base_url, timeout=self.timeout if isinstance(timeout, NotGiven) else timeout, http_client=http_client, max_retries=max_retries if is_given(max_retries) else self.max_retries, default_headers=headers, default_query=params, **_extra_kwargs)

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response,) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)

class MobilerunWithRawResponse:
    _client: Mobilerun

    def __init__(self, client: Mobilerun) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AppsResourceWithRawResponse:
        from .resources.apps import AppsResourceWithRawResponse
        return AppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def carriers(self) -> carriers.CarriersResourceWithRawResponse:
        from .resources.carriers import CarriersResourceWithRawResponse
        return CarriersResourceWithRawResponse(self._client.carriers)

    @cached_property
    def credentials(self) -> credentials.CredentialsResourceWithRawResponse:
        from .resources.credentials import CredentialsResourceWithRawResponse
        return CredentialsResourceWithRawResponse(self._client.credentials)

    @cached_property
    def devices(self) -> devices.DevicesResourceWithRawResponse:
        from .resources.devices import DevicesResourceWithRawResponse
        return DevicesResourceWithRawResponse(self._client.devices)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        """LLM Models"""
        from .resources.models import ModelsResourceWithRawResponse
        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        from .resources.profiles import ProfilesResourceWithRawResponse
        return ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def proxies(self) -> proxies.ProxiesResourceWithRawResponse:
        from .resources.proxies import ProxiesResourceWithRawResponse
        return ProxiesResourceWithRawResponse(self._client.proxies)

    @cached_property
    def connect(self) -> connect.ConnectResourceWithRawResponse:
        from .resources.connect import ConnectResourceWithRawResponse
        return ConnectResourceWithRawResponse(self._client.connect)

    @cached_property
    def tasks(self) -> tasks.TasksResourceWithRawResponse:
        """Tasks API"""
        from .resources.tasks import TasksResourceWithRawResponse
        return TasksResourceWithRawResponse(self._client.tasks)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithRawResponse:
        from .resources.workflows import WorkflowsResourceWithRawResponse
        return WorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse
        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse
        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def app_events(self) -> app_events.AppEventsResourceWithRawResponse:
        from .resources.app_events import AppEventsResourceWithRawResponse
        return AppEventsResourceWithRawResponse(self._client.app_events)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        from .resources.notifications import NotificationsResourceWithRawResponse
        return NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def esims(self) -> esims.EsimsResourceWithRawResponse:
        from .resources.esims import EsimsResourceWithRawResponse
        return EsimsResourceWithRawResponse(self._client.esims)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse
        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def numbers(self) -> numbers.NumbersResourceWithRawResponse:
        from .resources.numbers import NumbersResourceWithRawResponse
        return NumbersResourceWithRawResponse(self._client.numbers)

    @cached_property
    def store(self) -> store.StoreResourceWithRawResponse:
        from .resources.store import StoreResourceWithRawResponse
        return StoreResourceWithRawResponse(self._client.store)

class AsyncMobilerunWithRawResponse:
    _client: AsyncMobilerun

    def __init__(self, client: AsyncMobilerun) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithRawResponse:
        from .resources.apps import AsyncAppsResourceWithRawResponse
        return AsyncAppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def carriers(self) -> carriers.AsyncCarriersResourceWithRawResponse:
        from .resources.carriers import AsyncCarriersResourceWithRawResponse
        return AsyncCarriersResourceWithRawResponse(self._client.carriers)

    @cached_property
    def credentials(self) -> credentials.AsyncCredentialsResourceWithRawResponse:
        from .resources.credentials import AsyncCredentialsResourceWithRawResponse
        return AsyncCredentialsResourceWithRawResponse(self._client.credentials)

    @cached_property
    def devices(self) -> devices.AsyncDevicesResourceWithRawResponse:
        from .resources.devices import AsyncDevicesResourceWithRawResponse
        return AsyncDevicesResourceWithRawResponse(self._client.devices)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        """LLM Models"""
        from .resources.models import AsyncModelsResourceWithRawResponse
        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        from .resources.profiles import AsyncProfilesResourceWithRawResponse
        return AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def proxies(self) -> proxies.AsyncProxiesResourceWithRawResponse:
        from .resources.proxies import AsyncProxiesResourceWithRawResponse
        return AsyncProxiesResourceWithRawResponse(self._client.proxies)

    @cached_property
    def connect(self) -> connect.AsyncConnectResourceWithRawResponse:
        from .resources.connect import AsyncConnectResourceWithRawResponse
        return AsyncConnectResourceWithRawResponse(self._client.connect)

    @cached_property
    def tasks(self) -> tasks.AsyncTasksResourceWithRawResponse:
        """Tasks API"""
        from .resources.tasks import AsyncTasksResourceWithRawResponse
        return AsyncTasksResourceWithRawResponse(self._client.tasks)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithRawResponse:
        from .resources.workflows import AsyncWorkflowsResourceWithRawResponse
        return AsyncWorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse
        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse
        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def app_events(self) -> app_events.AsyncAppEventsResourceWithRawResponse:
        from .resources.app_events import AsyncAppEventsResourceWithRawResponse
        return AsyncAppEventsResourceWithRawResponse(self._client.app_events)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse
        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def esims(self) -> esims.AsyncEsimsResourceWithRawResponse:
        from .resources.esims import AsyncEsimsResourceWithRawResponse
        return AsyncEsimsResourceWithRawResponse(self._client.esims)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse
        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def numbers(self) -> numbers.AsyncNumbersResourceWithRawResponse:
        from .resources.numbers import AsyncNumbersResourceWithRawResponse
        return AsyncNumbersResourceWithRawResponse(self._client.numbers)

    @cached_property
    def store(self) -> store.AsyncStoreResourceWithRawResponse:
        from .resources.store import AsyncStoreResourceWithRawResponse
        return AsyncStoreResourceWithRawResponse(self._client.store)

class MobilerunWithStreamedResponse:
    _client: Mobilerun

    def __init__(self, client: Mobilerun) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AppsResourceWithStreamingResponse:
        from .resources.apps import AppsResourceWithStreamingResponse
        return AppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def carriers(self) -> carriers.CarriersResourceWithStreamingResponse:
        from .resources.carriers import CarriersResourceWithStreamingResponse
        return CarriersResourceWithStreamingResponse(self._client.carriers)

    @cached_property
    def credentials(self) -> credentials.CredentialsResourceWithStreamingResponse:
        from .resources.credentials import CredentialsResourceWithStreamingResponse
        return CredentialsResourceWithStreamingResponse(self._client.credentials)

    @cached_property
    def devices(self) -> devices.DevicesResourceWithStreamingResponse:
        from .resources.devices import DevicesResourceWithStreamingResponse
        return DevicesResourceWithStreamingResponse(self._client.devices)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        """LLM Models"""
        from .resources.models import ModelsResourceWithStreamingResponse
        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        from .resources.profiles import ProfilesResourceWithStreamingResponse
        return ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def proxies(self) -> proxies.ProxiesResourceWithStreamingResponse:
        from .resources.proxies import ProxiesResourceWithStreamingResponse
        return ProxiesResourceWithStreamingResponse(self._client.proxies)

    @cached_property
    def connect(self) -> connect.ConnectResourceWithStreamingResponse:
        from .resources.connect import ConnectResourceWithStreamingResponse
        return ConnectResourceWithStreamingResponse(self._client.connect)

    @cached_property
    def tasks(self) -> tasks.TasksResourceWithStreamingResponse:
        """Tasks API"""
        from .resources.tasks import TasksResourceWithStreamingResponse
        return TasksResourceWithStreamingResponse(self._client.tasks)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithStreamingResponse:
        from .resources.workflows import WorkflowsResourceWithStreamingResponse
        return WorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse
        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse
        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def app_events(self) -> app_events.AppEventsResourceWithStreamingResponse:
        from .resources.app_events import AppEventsResourceWithStreamingResponse
        return AppEventsResourceWithStreamingResponse(self._client.app_events)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        from .resources.notifications import NotificationsResourceWithStreamingResponse
        return NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def esims(self) -> esims.EsimsResourceWithStreamingResponse:
        from .resources.esims import EsimsResourceWithStreamingResponse
        return EsimsResourceWithStreamingResponse(self._client.esims)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse
        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def numbers(self) -> numbers.NumbersResourceWithStreamingResponse:
        from .resources.numbers import NumbersResourceWithStreamingResponse
        return NumbersResourceWithStreamingResponse(self._client.numbers)

    @cached_property
    def store(self) -> store.StoreResourceWithStreamingResponse:
        from .resources.store import StoreResourceWithStreamingResponse
        return StoreResourceWithStreamingResponse(self._client.store)

class AsyncMobilerunWithStreamedResponse:
    _client: AsyncMobilerun

    def __init__(self, client: AsyncMobilerun) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithStreamingResponse:
        from .resources.apps import AsyncAppsResourceWithStreamingResponse
        return AsyncAppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def carriers(self) -> carriers.AsyncCarriersResourceWithStreamingResponse:
        from .resources.carriers import AsyncCarriersResourceWithStreamingResponse
        return AsyncCarriersResourceWithStreamingResponse(self._client.carriers)

    @cached_property
    def credentials(self) -> credentials.AsyncCredentialsResourceWithStreamingResponse:
        from .resources.credentials import AsyncCredentialsResourceWithStreamingResponse
        return AsyncCredentialsResourceWithStreamingResponse(self._client.credentials)

    @cached_property
    def devices(self) -> devices.AsyncDevicesResourceWithStreamingResponse:
        from .resources.devices import AsyncDevicesResourceWithStreamingResponse
        return AsyncDevicesResourceWithStreamingResponse(self._client.devices)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        """LLM Models"""
        from .resources.models import AsyncModelsResourceWithStreamingResponse
        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        from .resources.profiles import AsyncProfilesResourceWithStreamingResponse
        return AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def proxies(self) -> proxies.AsyncProxiesResourceWithStreamingResponse:
        from .resources.proxies import AsyncProxiesResourceWithStreamingResponse
        return AsyncProxiesResourceWithStreamingResponse(self._client.proxies)

    @cached_property
    def connect(self) -> connect.AsyncConnectResourceWithStreamingResponse:
        from .resources.connect import AsyncConnectResourceWithStreamingResponse
        return AsyncConnectResourceWithStreamingResponse(self._client.connect)

    @cached_property
    def tasks(self) -> tasks.AsyncTasksResourceWithStreamingResponse:
        """Tasks API"""
        from .resources.tasks import AsyncTasksResourceWithStreamingResponse
        return AsyncTasksResourceWithStreamingResponse(self._client.tasks)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithStreamingResponse:
        from .resources.workflows import AsyncWorkflowsResourceWithStreamingResponse
        return AsyncWorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse
        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse
        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def app_events(self) -> app_events.AsyncAppEventsResourceWithStreamingResponse:
        from .resources.app_events import AsyncAppEventsResourceWithStreamingResponse
        return AsyncAppEventsResourceWithStreamingResponse(self._client.app_events)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse
        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def esims(self) -> esims.AsyncEsimsResourceWithStreamingResponse:
        from .resources.esims import AsyncEsimsResourceWithStreamingResponse
        return AsyncEsimsResourceWithStreamingResponse(self._client.esims)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse
        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def numbers(self) -> numbers.AsyncNumbersResourceWithStreamingResponse:
        from .resources.numbers import AsyncNumbersResourceWithStreamingResponse
        return AsyncNumbersResourceWithStreamingResponse(self._client.numbers)

    @cached_property
    def store(self) -> store.AsyncStoreResourceWithStreamingResponse:
        from .resources.store import AsyncStoreResourceWithStreamingResponse
        return AsyncStoreResourceWithStreamingResponse(self._client.store)

Client = Mobilerun

AsyncClient = AsyncMobilerun