---
keywords: "MCP server, Model Context Protocol, Claude Code, Claude Desktop, OpenCode, Codex, Cursor, VS Code, Copilot, Windsurf, Gemini CLI, Zed, Cline, AI pentest assistant, API key"
description: "Connect AI clients such as Claude Code, Codex, OpenCode, Cursor and VS Code to Faction's built-in MCP server with a personal API key, so an assistant can read and draft findings as you."
---

# MCP Server

!!! note "Enterprise feature"
    The MCP server is part of the commercial edition of Faction. It is not included in OWASP Faction, the open source edition. In OWASP Faction the **MCP Server** card does not appear on the **AI Configuration** page and `/api/mcp` does not exist.

Faction has a built-in [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server. MCP is the standard AI clients use to call tools, so once Faction is connected, an assistant like Claude Code, Codex or Cursor can list your assessments, read findings, draft new ones, record retest results and fill in checklists, all through Faction's API.

There is nothing to install or run next to Faction. The server is part of the Faction backend and answers at:

```text
https://<your-faction-host>/api/mcp
```

## How it works

- **Each person connects as themselves.** A client authenticates with a personal API key (`sk_fac_…`) and acts as the key's owner. It can see and change exactly what that person can in the Faction web UI: the same permissions and the same assessment scope. A tester assigned to three assessments sees those three and nothing else.
- **Read-only keys stay read-only.** A key created with the **Read only** scope can browse, but every tool that writes returns an error.
- **Nothing can be deleted.** There are no delete tools. Deleting is done in the web UI.
- **Every call that reaches a tool is logged.** Each tool call is recorded with the user, the API key, the tool and its arguments under **Logs → MCP**, and kept for 90 days. A call rejected before it reaches a tool — an unknown tool name, or arguments that fail the tool's input schema — is not recorded.
- **It is off until an administrator turns it on.**

The transport is stateless Streamable HTTP. Clients send JSON-RPC over `POST`; `GET` returns `405`, which tells a client there is no event stream to open. Authentication is a static `Authorization: Bearer` header. The server does not offer OAuth sign-in, which matters for a few clients (see [Claude Desktop](#claude-desktop)).

## Turn it on

Anyone with the `ai:config:write` permission (super admins included) enables the server once for the whole install, from the **MCP Server** card at the bottom of the **AI Configuration** page:

1. Open **Administration → AI Configuration**.
2. In the **MCP Server** card, switch the toggle to **Enabled** and confirm with **Turn On**.

The same card shows the server URL and ready-to-paste snippets for Claude Code, Cursor and VS Code. Viewing the card only needs the `ai:config:read` permission. While the server is off, clients get `403` with a message saying so.

## Create an API key

Each person uses their own key.

1. Open the user menu and choose **API Keys**.
2. Click **Create API Key**, give it a name you will recognize (for example "Claude Code laptop"), and pick a scope:
    - **Read & write**: everything you can currently do.
    - **Read only**: the assistant can look things up but not change anything. A good default while you are getting started.
3. Copy the key. It is shown once.

Once the MCP server is enabled, the **API Keys** page also shows a **Connect an AI client** card with the URL and snippets.

!!! warning "Treat the key like a password"
    Anyone holding the key can do what you can do in Faction. Keep it out of files you commit: every example below reads it from an environment variable or a secret prompt. Revoke a key on the **API Keys** page if it leaks.

The examples on this page read the key from an environment variable named `FACTION_API_KEY` and use `https://faction.example.com` as the host. Replace the host with your own.

```bash
export FACTION_API_KEY="sk_fac_…"
```

## Connect your client

### Claude Code

Add the server with the CLI. `--scope user` makes it available in every project; leave it off to add it to the current project only.

```bash
claude mcp add --transport http --scope user faction \
  https://faction.example.com/api/mcp \
  --header "Authorization: Bearer ${FACTION_API_KEY}"
```

Your shell substitutes the key when you run the command, so the key is stored in Claude Code's user settings. To keep it out of every file, add the server to a project's `.mcp.json` instead. Claude Code expands `${VAR}` when it connects:

```json
{
  "mcpServers": {
    "faction": {
      "type": "http",
      "url": "https://faction.example.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ${FACTION_API_KEY}"
      }
    }
  }
}
```

Check it with `claude mcp list`, or run `/mcp` inside a session to see the server's status and tools.

### Claude Desktop

Claude Desktop adds remote servers through **Settings → Connectors**, and on most plans that dialog only offers OAuth sign-in, which Faction's MCP server does not use. Connect through the [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) bridge instead. It needs Node.js installed.

Edit `claude_desktop_config.json`:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "faction": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "https://faction.example.com/api/mcp",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer sk_fac_…"
      }
    }
  }
}
```

There is no space after `Authorization:` in the header argument; `mcp-remote` needs it written that way. Quit Claude Desktop completely and reopen it. If it cannot find `npx`, use the full path (`which npx` on macOS).

!!! info
    On Team and Enterprise plans where Anthropic has enabled request-header authentication for custom connectors, you can instead add a custom connector with the Faction URL, choose **No sign-in**, and set an `authorization` request header to `Bearer sk_fac_…`.

### OpenAI Codex CLI

Add the server to `~/.codex/config.toml`. Codex reads the key from the environment variable you name and sends it as a bearer token, so the key never appears in the file:

```toml
[mcp_servers.faction]
url = "https://faction.example.com/api/mcp"
bearer_token_env_var = "FACTION_API_KEY"
```

Or from the command line:

```bash
codex mcp add faction --url https://faction.example.com/api/mcp \
  --bearer-token-env-var FACTION_API_KEY
```

Check it with `codex mcp list`. The variable must be set in the shell that starts Codex.

### OpenCode

Add the server to `opencode.json`, either in the project root or globally at `~/.config/opencode/opencode.json`. OpenCode's variable syntax is `{env:NAME}`. Setting `"oauth": false` stops it from attempting an OAuth sign-in:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "faction": {
      "type": "remote",
      "url": "https://faction.example.com/api/mcp",
      "headers": {
        "Authorization": "Bearer {env:FACTION_API_KEY}"
      },
      "oauth": false
    }
  }
}
```

### Cursor

Add the server to `~/.cursor/mcp.json` (all projects) or `.cursor/mcp.json` in a project:

```json
{
  "mcpServers": {
    "faction": {
      "url": "https://faction.example.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ${env:FACTION_API_KEY}"
      }
    }
  }
}
```

The server and its tools appear under **Settings → MCP**. If it fails to connect with a `401`, open **Output → MCP Logs**: some Cursor versions send `${env:…}` in headers literally instead of substituting it. In that case, put the key in the file directly and keep the file out of version control.

### VS Code (GitHub Copilot)

Add the server to `.vscode/mcp.json` in a workspace, or run **MCP: Open User Configuration** for all workspaces. The `inputs` block makes VS Code prompt for the key once and store it securely rather than in the file:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "faction-api-key",
      "description": "Faction API key",
      "password": true
    }
  ],
  "servers": {
    "faction": {
      "type": "http",
      "url": "https://faction.example.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ${input:faction-api-key}"
      }
    }
  }
}
```

Use **MCP: List Servers** to start the server and check its status, then pick Faction's tools in Copilot's agent mode.

### Windsurf

Add the server to `~/.codeium/windsurf/mcp_config.json` (`%USERPROFILE%\.codeium\windsurf\mcp_config.json` on Windows). Windsurf uses `serverUrl` rather than `url`:

```json
{
  "mcpServers": {
    "faction": {
      "serverUrl": "https://faction.example.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ${env:FACTION_API_KEY}"
      }
    }
  }
}
```

The server appears in Cascade's MCP panel.

### Gemini CLI

Add the server with the CLI. `-s user` adds it for every project instead of the current one:

```bash
gemini mcp add -s user --transport http faction \
  https://faction.example.com/api/mcp \
  --header "Authorization: Bearer ${FACTION_API_KEY}"
```

Or edit `~/.gemini/settings.json` (or `.gemini/settings.json` in a project). Gemini CLI uses `httpUrl` for Streamable HTTP; `url` means the older SSE transport, which Faction does not serve:

```json
{
  "mcpServers": {
    "faction": {
      "httpUrl": "https://faction.example.com/api/mcp",
      "headers": {
        "Authorization": "Bearer sk_fac_…"
      }
    }
  }
}
```

Check it with `gemini mcp list`, or `/mcp` inside a session.

### Zed

Add the server under `context_servers` in Zed's `settings.json` (**zed: open settings file**):

```json
{
  "context_servers": {
    "faction": {
      "url": "https://faction.example.com/api/mcp",
      "headers": {
        "Authorization": "Bearer sk_fac_…"
      }
    }
  }
}
```

### Cline

Open the Cline sidebar, then **MCP Servers → Configure**, and add the server to `cline_mcp_settings.json`. The `type` must be exactly `streamableHttp`. Any other value, or none, makes Cline fall back to the older SSE transport, which fails against Faction with `405`:

```json
{
  "mcpServers": {
    "faction": {
      "type": "streamableHttp",
      "url": "https://faction.example.com/api/mcp",
      "headers": {
        "Authorization": "Bearer sk_fac_…"
      },
      "disabled": false
    }
  }
}
```

### Other clients

Any MCP client that supports **Streamable HTTP** with a **custom request header** can connect. Give it the URL and the header `Authorization: Bearer sk_fac_…`. A client that only supports the older HTTP+SSE transport, or only OAuth sign-in for remote servers, needs the `mcp-remote` bridge shown under [Claude Desktop](#claude-desktop).

## First steps

Ask the assistant to call `whoami` first. It returns who the connection acts as and the permissions the key grants, which confirms the key works and explains what the assistant can and cannot do. Then try something like:

- "List my assessments that are in Testing."
- "Show the high and critical findings on the ACME web app assessment."
- "Draft a finding for a reflected XSS in the search parameter, based on the default vulnerability template."
- "Mark checklist item 'Check login' as passed with a note that MFA is enforced."

## Available tools

| Group | Tools |
|---|---|
| Identity | `whoami` |
| Assessments | `list_assessments`, `get_assessment` |
| Vulnerabilities | `list_vulnerabilities`, `get_vulnerability`, `search_vulnerabilities`, `create_vulnerability`, `update_vulnerability`, `set_vulnerability_status` |
| Reference data | `list_vulnerability_categories`, `list_vulnerability_templates`, `get_vulnerability_template` |
| Remediation and retests | `get_remediation_queue`, `list_retests`, `get_assessment_retests`, `get_retest`, `schedule_retest`, `complete_retest` |
| Checklists | `list_assessment_checklists`, `update_checklist_responses` |
| Notebooks | `get_notebook_tree`, `search_notebook`, `get_notebook_node`, `create_notebook_node`, `update_notebook_node` |

Things worth knowing when you prompt:

- IDs are UUIDs. Vulnerabilities belong to an assessment, so vulnerability tools take an `assessment_id`.
- Notebooks belong to an application, not an assessment. `get_assessment` returns the assessment's `applicationId`.
- Severity is one of `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` or `INFORMATIONAL`.
- Descriptions, recommendations, details and notebook pages are HTML.
- `update_vulnerability` changes only the fields it is given. Findings on a finalized assessment cannot be edited, but their status can still change.
- `update_checklist_responses` records only the answers it is given and keeps the rest.
- List tools return a page at a time (up to 100 items), so the assistant pages through larger lists.

Every tool is listed to every client. If a key lacks the permission a tool needs, the call returns an error naming the permissions it requires.

Report generation and deleting records are not available through MCP.

## Audit log

**Logs → MCP** lists every tool call: time, user, tool, assessment, result and duration. Open a row to see the API key, the arguments and any error message. Tool results are not stored. Rows are kept for 90 days. Anyone with the `audit:logs:read` permission can view the log.

A call rejected before it reaches a tool — an unknown tool name, or arguments that fail the tool's input schema — never creates a row here, since no tool ran.

## Troubleshooting

| Response | Meaning |
|---|---|
| `401 Unauthorized` | The key is missing, mistyped, expired or revoked, or the client did not send the `Authorization` header. Check the header is exactly `Authorization: Bearer sk_fac_…`. |
| `403` "The MCP server is turned off" | An administrator has not enabled it in the **MCP Server** card on **Administration → AI Configuration**. |
| `403` with no message | The request came from a web page on another site. Browser requests are only accepted from Faction's own address. Desktop and CLI clients are not affected. |
| `404` | This install runs OWASP Faction, which does not include the MCP server. |
| `402` | Only seen on the commercial build when the community edition is forced (for example a self-check or test environment). A normal OWASP Faction install returns `404` instead — see above. |
| `405 Method Not Allowed` | The client opened a `GET` event stream. Faction uses stateless Streamable HTTP; switch the client to Streamable HTTP (for example `type: "streamableHttp"` in Cline, `httpUrl` in Gemini CLI). |
| A tool returns "Access denied" or "not found" | The key's owner does not have the permission, or the record is outside their assessment scope. Faction generally reports an out-of-scope record as not found rather than naming it. `whoami` shows what the key grants. |
