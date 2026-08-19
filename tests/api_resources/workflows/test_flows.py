# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from mobilerun_sdk.types.workflows import FlowCreateResponse, FlowRetrieveResponse, FlowUpdateResponse, FlowListResponse, FlowDeleteResponse, FlowCloneResponse, FlowDryRunResponse, FlowListRepairsResponse, FlowUnblockResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.workflows import flow_create_params
from mobilerun_sdk.types.workflows import flow_update_params
from mobilerun_sdk.types.workflows import flow_list_params
from mobilerun_sdk.types.workflows import flow_clone_params
from mobilerun_sdk.types.workflows import flow_dry_run_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestFlows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.create(
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowCreateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.create(
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
                "children": [{
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                    "continue_on_error": True,
                    "name_override": "x",
                    "overrides": {
                        "params": {
                            "foo": "bar"
                        }
                    },
                }],
                "continue_on_error": True,
                "name_override": "x",
                "overrides": {
                    "params": {
                        "foo": "bar"
                    }
                },
            }],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cooldown_scope="flow",
            cooldown_seconds=0,
            description="description",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enabled=True,
            health_monitoring_enabled=True,
            notify_on_failure=True,
            notify_on_success=True,
            notify_webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            self_healing_enabled=True,
            self_healing_max_attempts=1,
        )
        assert_matches_type(FlowCreateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.create(
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowCreateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.create(
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowCreateResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowRetrieveResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowRetrieveResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowRetrieveResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.with_raw_response.retrieve(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cooldown_scope="flow",
            cooldown_seconds=0,
            description="description",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enabled=True,
            health_monitoring_enabled=True,
            name="x",
            notify_on_failure=True,
            notify_on_success=True,
            notify_webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            self_healing_enabled=True,
            self_healing_max_attempts=1,
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowUpdateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowUpdateResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.with_raw_response.update(
              flow_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.list()
        assert_matches_type(FlowListResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.list(
            created_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            enabled="true",
            mine="true",
            order_by="name",
            order_by_direction="asc",
            page=1,
            page_size=1,
            search="x",
            status=["healthy"],
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowListResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowListResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowListResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowDeleteResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowDeleteResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowDeleteResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.with_raw_response.delete(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.clone(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowCloneResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.clone(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="x",
        )
        assert_matches_type(FlowCloneResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.clone(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowCloneResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.clone(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowCloneResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_clone(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.with_raw_response.clone(
              flow_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_dry_run(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.dry_run(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowDryRunResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_dry_run_with_all_params(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.dry_run(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={
                "foo": "bar"
            },
        )
        assert_matches_type(FlowDryRunResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_dry_run(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.dry_run(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowDryRunResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_dry_run(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.dry_run(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowDryRunResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_dry_run(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.with_raw_response.dry_run(
              flow_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_repairs(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.list_repairs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowListRepairsResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_repairs(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.list_repairs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowListRepairsResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_repairs(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.list_repairs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowListRepairsResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_repairs(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.with_raw_response.list_repairs(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unblock(self, client: Mobilerun) -> None:
        flow = client.workflows.flows.unblock(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowUnblockResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unblock(self, client: Mobilerun) -> None:

        response = client.workflows.flows.with_raw_response.unblock(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = response.parse()
        assert_matches_type(FlowUnblockResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unblock(self, client: Mobilerun) -> None:
        with client.workflows.flows.with_streaming_response.unblock(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = response.parse()
            assert_matches_type(FlowUnblockResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unblock(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.with_raw_response.unblock(
              "",
          )
class TestAsyncFlows:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.create(
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowCreateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.create(
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
                "children": [{
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                    "continue_on_error": True,
                    "name_override": "x",
                    "overrides": {
                        "params": {
                            "foo": "bar"
                        }
                    },
                }],
                "continue_on_error": True,
                "name_override": "x",
                "overrides": {
                    "params": {
                        "foo": "bar"
                    }
                },
            }],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cooldown_scope="flow",
            cooldown_seconds=0,
            description="description",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enabled=True,
            health_monitoring_enabled=True,
            notify_on_failure=True,
            notify_on_success=True,
            notify_webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            self_healing_enabled=True,
            self_healing_max_attempts=1,
        )
        assert_matches_type(FlowCreateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.create(
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowCreateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.create(
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowCreateResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowRetrieveResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowRetrieveResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowRetrieveResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.with_raw_response.retrieve(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cooldown_scope="flow",
            cooldown_seconds=0,
            description="description",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enabled=True,
            health_monitoring_enabled=True,
            name="x",
            notify_on_failure=True,
            notify_on_success=True,
            notify_webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            self_healing_enabled=True,
            self_healing_max_attempts=1,
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowUpdateResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.update(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowUpdateResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.with_raw_response.update(
              flow_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.list()
        assert_matches_type(FlowListResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.list(
            created_by="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            enabled="true",
            mine="true",
            order_by="name",
            order_by_direction="asc",
            page=1,
            page_size=1,
            search="x",
            status=["healthy"],
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowListResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowListResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowListResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowDeleteResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowDeleteResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowDeleteResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.with_raw_response.delete(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.clone(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowCloneResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.clone(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="x",
        )
        assert_matches_type(FlowCloneResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.clone(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowCloneResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.clone(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowCloneResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_clone(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.with_raw_response.clone(
              flow_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_dry_run(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.dry_run(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowDryRunResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_dry_run_with_all_params(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.dry_run(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={
                "foo": "bar"
            },
        )
        assert_matches_type(FlowDryRunResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_dry_run(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.dry_run(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowDryRunResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_dry_run(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.dry_run(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowDryRunResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_dry_run(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.with_raw_response.dry_run(
              flow_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_repairs(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.list_repairs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowListRepairsResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_repairs(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.list_repairs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowListRepairsResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_repairs(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.list_repairs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowListRepairsResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_repairs(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.with_raw_response.list_repairs(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unblock(self, async_client: AsyncMobilerun) -> None:
        flow = await async_client.workflows.flows.unblock(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FlowUnblockResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unblock(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.with_raw_response.unblock(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        flow = await response.parse()
        assert_matches_type(FlowUnblockResponse, flow, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unblock(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.with_streaming_response.unblock(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            flow = await response.parse()
            assert_matches_type(FlowUnblockResponse, flow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unblock(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.with_raw_response.unblock(
              "",
          )