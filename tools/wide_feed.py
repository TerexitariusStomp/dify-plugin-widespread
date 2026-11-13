from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools._client import get, q


class WideFeedTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        query = q(tool_parameters.get("query") or "")
        source = q(tool_parameters.get("source") or "")
        limit = int(tool_parameters.get("limit") or 25)
        doc = get(f"/api/feed?q={query}&source={source}&limit={limit}")
        items = (doc.get("items", doc) if isinstance(doc, dict) else doc) or []
        yield self.create_json_message({"items": items[:limit]})
        yield self.create_text_message(f"{len(items[:limit])} feed item(s).")
