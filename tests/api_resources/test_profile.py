# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from supermemory import Supermemory, AsyncSupermemory
from tests.utils import assert_matches_type
from supermemory.types import ProfilePropertyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_property(self, client: Supermemory) -> None:
        profile = client.profile.property(
            container_tag="containerTag",
        )
        assert_matches_type(ProfilePropertyResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_property_with_all_params(self, client: Supermemory) -> None:
        profile = client.profile.property(
            container_tag="containerTag",
            q="q",
        )
        assert_matches_type(ProfilePropertyResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_property(self, client: Supermemory) -> None:
        response = client.profile.with_raw_response.property(
            container_tag="containerTag",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfilePropertyResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_property(self, client: Supermemory) -> None:
        with client.profile.with_streaming_response.property(
            container_tag="containerTag",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfilePropertyResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_property(self, async_client: AsyncSupermemory) -> None:
        profile = await async_client.profile.property(
            container_tag="containerTag",
        )
        assert_matches_type(ProfilePropertyResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_property_with_all_params(self, async_client: AsyncSupermemory) -> None:
        profile = await async_client.profile.property(
            container_tag="containerTag",
            q="q",
        )
        assert_matches_type(ProfilePropertyResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_property(self, async_client: AsyncSupermemory) -> None:
        response = await async_client.profile.with_raw_response.property(
            container_tag="containerTag",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfilePropertyResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_property(self, async_client: AsyncSupermemory) -> None:
        async with async_client.profile.with_streaming_response.property(
            container_tag="containerTag",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfilePropertyResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
