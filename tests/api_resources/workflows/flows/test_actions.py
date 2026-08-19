# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from mobilerun_sdk.types.workflows.flows import ActionListResponse, ActionAddResponse, ActionRemoveResponse, ActionReplaceResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.workflows.flows import action_add_params
from mobilerun_sdk.types.workflows.flows import action_replace_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        action = client.workflows.flows.actions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionListResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:

        response = client.workflows.flows.actions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action = response.parse()
        assert_matches_type(ActionListResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.workflows.flows.actions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action = response.parse()
            assert_matches_type(ActionListResponse, action, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.actions.with_raw_response.list(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Mobilerun) -> None:
        action = client.workflows.flows.actions.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            position=0,
        )
        assert_matches_type(ActionAddResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Mobilerun) -> None:
        action = client.workflows.flows.actions.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            position=0,
            children=[{
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
            continue_on_error=True,
            name_override="x",
            overrides={
                "params": {
                    "foo": "bar"
                }
            },
            parent_flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionAddResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Mobilerun) -> None:

        response = client.workflows.flows.actions.with_raw_response.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            position=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action = response.parse()
        assert_matches_type(ActionAddResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Mobilerun) -> None:
        with client.workflows.flows.actions.with_streaming_response.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            position=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action = response.parse()
            assert_matches_type(ActionAddResponse, action, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.actions.with_raw_response.add(
              flow_id="",
              action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              position=0,
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Mobilerun) -> None:
        action = client.workflows.flows.actions.remove(
            flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionRemoveResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Mobilerun) -> None:

        response = client.workflows.flows.actions.with_raw_response.remove(
            flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action = response.parse()
        assert_matches_type(ActionRemoveResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Mobilerun) -> None:
        with client.workflows.flows.actions.with_streaming_response.remove(
            flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action = response.parse()
            assert_matches_type(ActionRemoveResponse, action, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.actions.with_raw_response.remove(
              flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              flow_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_action_id` but received ''"):
          client.workflows.flows.actions.with_raw_response.remove(
              flow_action_id="",
              flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Mobilerun) -> None:
        action = client.workflows.flows.actions.replace(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
        )
        assert_matches_type(ActionReplaceResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Mobilerun) -> None:

        response = client.workflows.flows.actions.with_raw_response.replace(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action = response.parse()
        assert_matches_type(ActionReplaceResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Mobilerun) -> None:
        with client.workflows.flows.actions.with_streaming_response.replace(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action = response.parse()
            assert_matches_type(ActionReplaceResponse, action, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          client.workflows.flows.actions.with_raw_response.replace(
              flow_id="",
              actions=[{
                  "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                  "position": 0,
              }],
          )
class TestAsyncActions:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        action = await async_client.workflows.flows.actions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionListResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.actions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action = await response.parse()
        assert_matches_type(ActionListResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.actions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action = await response.parse()
            assert_matches_type(ActionListResponse, action, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.actions.with_raw_response.list(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncMobilerun) -> None:
        action = await async_client.workflows.flows.actions.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            position=0,
        )
        assert_matches_type(ActionAddResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncMobilerun) -> None:
        action = await async_client.workflows.flows.actions.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            position=0,
            children=[{
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
            continue_on_error=True,
            name_override="x",
            overrides={
                "params": {
                    "foo": "bar"
                }
            },
            parent_flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionAddResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.actions.with_raw_response.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            position=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action = await response.parse()
        assert_matches_type(ActionAddResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.actions.with_streaming_response.add(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            position=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action = await response.parse()
            assert_matches_type(ActionAddResponse, action, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.actions.with_raw_response.add(
              flow_id="",
              action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              position=0,
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncMobilerun) -> None:
        action = await async_client.workflows.flows.actions.remove(
            flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionRemoveResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.actions.with_raw_response.remove(
            flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action = await response.parse()
        assert_matches_type(ActionRemoveResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.actions.with_streaming_response.remove(
            flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action = await response.parse()
            assert_matches_type(ActionRemoveResponse, action, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.actions.with_raw_response.remove(
              flow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              flow_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_action_id` but received ''"):
          await async_client.workflows.flows.actions.with_raw_response.remove(
              flow_action_id="",
              flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncMobilerun) -> None:
        action = await async_client.workflows.flows.actions.replace(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
        )
        assert_matches_type(ActionReplaceResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.flows.actions.with_raw_response.replace(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action = await response.parse()
        assert_matches_type(ActionReplaceResponse, action, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.actions.with_streaming_response.replace(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[{
                "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "position": 0,
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action = await response.parse()
            assert_matches_type(ActionReplaceResponse, action, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
          await async_client.workflows.flows.actions.with_raw_response.replace(
              flow_id="",
              actions=[{
                  "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                  "position": 0,
              }],
          )