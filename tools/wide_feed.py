from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools._client import get, q

_CHAIN_FORGES = {"near", "solana", "ethereum", "base", "arbitrum", "bitcoin"}
_WEB3_SOURCES = {"near-chain", "olas", "agentledger", "wurk", "termix", "claudelance"}
_CHAIN_CURRENCIES = {"NEAR", "SOL", "ETH", "BTC", "USDC", "USDT", "DAI", "WURK"}


def _excluded(record: dict) -> bool:
    forge = str(record.get("forge") or "").lower()
    source = str(record.get("source") or "").lower()
    currency = str(record.get("currency") or "").upper()
    proof = str((record.get("escrow") or {}).get("proof") or "")
    return (
        forge in _CHAIN_FORGES
        or source in _WEB3_SOURCES
        or source.endswith("-chain")
        or currency in _CHAIN_CURRENCIES
        or currency.startswith("TOK:")
        or proof.split(":", 1)[0].lower() in _CHAIN_FORGES
        or record.get("kind") == "service"
    )


class WideFeedTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        query = q(tool_parameters.get("query") or "")
        source = q(tool_parameters.get("source") or "")
        limit = int(tool_parameters.get("limit") or 25)
        doc = get(f"/api/feed?q={query}&source={source}&limit={limit}")
        records = (doc.get("records") or doc.get("items") or []) if isinstance(doc, dict) else (doc or [])
        items = [r for r in records if isinstance(r, dict) and not _excluded(r)]
        page = items[:limit]
        yield self.create_json_message({"items": page})
        yield self.create_text_message(f"{len(page)} feed item(s).")
