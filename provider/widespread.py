from typing import Any

from dify_plugin import ToolProvider


class WidespreadProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        # No credentials required — the read/discovery surface is public.
        # Signed write operations stay behind the non-custodial MCP server.
        return None
