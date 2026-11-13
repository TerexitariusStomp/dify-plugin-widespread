from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools._client import get


class WideBountiesTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        state = get("/api/state")
        bounties = (state.get("bounties") or [])[: int(tool_parameters.get("limit") or 25)]
        yield self.create_json_message({"bounties": bounties})
        yield self.create_text_message(
            "\n".join(f"- {b.get('title', b.get('id', '?'))} — {b.get('reward', b.get('amount', ''))}" for b in bounties) or "No open bounties."
        )
