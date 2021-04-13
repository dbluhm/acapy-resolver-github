"""Test Github Resolver."""

import pytest
from acapy_resolver_github.resolver import GithubResolver


@pytest.fixture
def resolver():
    yield GithubResolver()


@pytest.fixture
def profile():
    yield None


@pytest.mark.asyncio
async def test_resolve_dbluhm(resolver, profile):
    doc = await resolver.resolve(profile, "did:github:dbluhm")
    assert doc.id == "did:github:dbluhm"
