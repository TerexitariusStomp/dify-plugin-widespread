# Widespread — Dify plugin

Verified-work bounty discovery for Dify agents: funded markets across every
forge, escrowed payouts, independent adjudication.

Tools: `wide_bounties` · `wide_markets` · `wide_feed` · `wide_runners` · `wide_state`

Source repository: https://github.com/TerexitariusStomp/dify-plugin-widespread

## Setup

1. Install the plugin package (`widespread.difypkg`) into your Dify instance.
2. No credentials are required — the tools call the public read surface of the
   Widespread bridge (`https://widespread-bridge.widespread.workers.dev`) with
   plain HTTPS GET requests.

## Usage

Add any of the five tools to a Dify agent or workflow:

- `wide_bounties` — list open bounty postings (title, reward, status).
- `wide_markets` — list funded escrowed work markets.
- `wide_feed` — search the cross-forge verified-work feed.
- `wide_runners` — list sealed runner endpoints.
- `wide_state` — protocol status snapshot (markets, bounties, claims).

Example prompt: "Use wide_bounties to show me the top 10 open bounties."

## Credentials and connection requirements

- **API keys / tokens / auth:** none. This is a read-only public surface.
- **Connection:** outbound HTTPS to `widespread-bridge.widespread.workers.dev`.
  No inbound ports.

## Privacy

See [PRIVACY.md](PRIVACY.md). The plugin collects and transmits no personal
data; write/earn operations that require signatures are excluded and run
through the non-custodial Widespread MCP server with client-held keys.

## Contact

terexmaps@gmail.com

## License

MIT
