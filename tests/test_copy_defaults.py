from typing import Any

import httpx
import pytest

from supermemory import AsyncSupermemory, Supermemory

CASES = [
    ({"set_default_headers": {}}, {}, {"trace": "original"}),
    ({"set_default_query": {}}, {"x-context": "original"}, {}),
    ({"set_default_headers": {}, "set_default_query": {}}, {}, {}),
    ({"set_default_headers": None, "set_default_query": None}, {"x-context": "original"}, {"trace": "original"}),
    (
        {"set_default_headers": {"X-New": "replacement"}, "set_default_query": {"new": "replacement"}},
        {"x-new": "replacement"},
        {"new": "replacement"},
    ),
    (
        {"default_headers": {"X-New": "additional"}, "default_query": {"new": "additional"}},
        {"x-context": "original", "x-new": "additional"},
        {"trace": "original", "new": "additional"},
    ),
]


@pytest.fixture(autouse=True)
def clear_custom_headers(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SUPERMEMORY_CUSTOM_HEADERS", raising=False)


def verify(request: httpx.Request, headers: dict[str, str], query: dict[str, str]) -> None:
    assert {k: v for k, v in request.headers.items() if k in ("x-context", "x-new")} == headers
    assert dict(request.url.params) == query
    assert request.headers["authorization"] == "Bearer sm_test"


@pytest.mark.parametrize("method", ["copy", "with_options"])
@pytest.mark.parametrize("options,headers,query", CASES)
def test_sync_copy_replaces_or_merges_defaults(
    method: str, options: dict[str, Any], headers: dict[str, str], query: dict[str, str]
) -> None:
    seen = []

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(
            200,
            json={"namespaces": [], "pagination": {"currentPage": 1, "limit": 10, "totalItems": 0, "totalPages": 0}},
        )

    with httpx.Client(transport=httpx.MockTransport(handle)) as transport:
        client = Supermemory(
            api_key="sm_test",
            http_client=transport,
            default_headers={"X-Context": "original"},
            default_query={"trace": "original"},
        )
        derived = getattr(client, method)(**options)
        derived.namespaces.list()
        client.namespaces.list()

    assert len(seen) == 2
    verify(seen[0], headers, query)
    verify(seen[1], {"x-context": "original"}, {"trace": "original"})


@pytest.mark.parametrize("method", ["copy", "with_options"])
@pytest.mark.parametrize("options,headers,query", CASES)
async def test_async_copy_replaces_or_merges_defaults(
    method: str, options: dict[str, Any], headers: dict[str, str], query: dict[str, str]
) -> None:
    seen = []

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(
            200,
            json={"namespaces": [], "pagination": {"currentPage": 1, "limit": 10, "totalItems": 0, "totalPages": 0}},
        )

    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as transport:
        client = AsyncSupermemory(
            api_key="sm_test",
            http_client=transport,
            default_headers={"X-Context": "original"},
            default_query={"trace": "original"},
        )
        derived = getattr(client, method)(**options)
        await derived.namespaces.list()
        await client.namespaces.list()

    assert len(seen) == 2
    verify(seen[0], headers, query)
    verify(seen[1], {"x-context": "original"}, {"trace": "original"})
