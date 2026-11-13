import json
from urllib.parse import quote
from urllib.request import Request, urlopen

BASE = "https://widespread-bridge.widespread.workers.dev"


def get(path: str, base: str = BASE, timeout: int = 30):
    req = Request(f"{base.rstrip('/')}{path}", headers={"accept": "application/json"})
    with urlopen(req, timeout=timeout) as resp:  # noqa: S310
        return json.loads(resp.read().decode())


def q(v) -> str:
    return quote(str(v), safe="")
