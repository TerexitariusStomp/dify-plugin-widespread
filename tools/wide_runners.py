from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools._client import get


class WideRunnersTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        data = get("/api/runners")
        runners = (data.get("runners", data) if isinstance(data, dict) else data) or []
        yield self.create_json_message({"runners": runners})
        yield self.create_text_message(f"{len(runners)} runner(s).")
