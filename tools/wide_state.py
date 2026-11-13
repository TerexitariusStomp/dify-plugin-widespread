from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools._client import get


class WideStateTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        state = get("/api/state")
        yield self.create_json_message(state)
        yield self.create_text_message(
            f"{len(state.get('claims') or [])} claim(s), {len(state.get('bounties') or [])} bounty(ies)."
        )
