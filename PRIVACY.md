# Privacy

This plugin makes read-only HTTPS GET requests to the Widespread bridge
(widespread-bridge.widespread.workers.dev). No credentials, API keys, or
personal data are collected, stored, or transmitted. Tool parameters
(`query`, `source`, `limit`) are sent to the bridge only as URL query strings
for feed/market lookups. Write/earn operations that require signatures are
deliberately excluded — they run through the non-custodial MCP server with
client-held keys.

No user data is collected by this plugin.
