"""Github Resolver."""

import json
import re
from typing import Pattern

import aiohttp
from aries_cloudagent.core.profile import Profile
from aries_cloudagent.resolver.base import (
    BaseDIDResolver,
    DIDNotFound,
    ResolverError,
    ResolverType,
)
from pydid import DID


class GithubResolver(BaseDIDResolver):
    """Github Resolver."""

    def __init__(self):
        super().__init__(ResolverType.NATIVE)
        self._supported_did_regex = re.compile("^did:github:.*$")

    @property
    def supported_did_regex(self) -> Pattern:
        """Return list of supported methods."""
        return self._supported_did_regex

    async def setup(self, context):
        """Setup the github resolver (none required)."""

    async def _resolve(self, profile: Profile, did: str) -> dict:
        """Resolve github DIDs."""
        as_did = DID(did)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://raw.githubusercontent.com/{as_did.method_specific_id}"
                "/ghdid/master/index.jsonld"
            ) as response:
                if response.status == 200:
                    try:
                        return json.loads(await response.text())
                    except Exception as err:
                        raise ResolverError(
                            "Response was incorrectly formatted"
                        ) from err
                if response.status == 404:
                    raise DIDNotFound(f"No document found for {did}")
                raise ResolverError(
                    "Could not find doc for {}: {}".format(did, await response.text())
                )
