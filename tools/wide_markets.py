from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools._client import get


class WideMarketsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        data = get("/api/markets")
        markets = (data.get("markets", data) if isinstance(data, dict) else data) or []
        markets = markets[: int(tool_parameters.get("limit") or 25)]
        yield self.create_json_message({"markets": markets})
        yield self.create_text_message(f"{len(markets)} open market(s).")
