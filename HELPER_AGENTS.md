# Helper Agents — for Fable

Three OpenClaw agents are configured to help work the physics problem in this
directory. Each is a distinct large model reached through the local OpenClaw
gateway. This file is your guide to talking to them.

## Roster

| Agent id    | Model (via Together.ai)              | Context | Thinking | Good for |
|-------------|--------------------------------------|--------:|----------|----------|
| `deepseek`  | `deepseek-ai/DeepSeek-V4-Pro`        |   512k  | high     | Long derivations, careful multi-step reasoning, holding a lot of context at once |
| `glm`       | `zai-org/GLM-5.2`                    |   203k  | high     | Independent second opinion, general analysis, cross-checking a result |
| `kimi-code` | `moonshotai/Kimi-K2.7-Code`         |   262k  | high     | Turning math into code, numerics/simulation, symbolic algebra, checking a calculation by running it |

All three:
- run with **thinking effort set to `high`**,
- share **this directory (`entropicGravity`) as their workspace** — they can read
  the files here (`ETRG-0_referee_packet.md`, the PDF, `files/`) directly, so you
  can refer to a filename instead of pasting its whole contents,
- keep **separate memory/state** from each other and from you.

## How to talk to them

The `openclaw` CLI is on the PATH and works from any directory. One turn, one reply:

```bash
openclaw agent --agent deepseek --message "Derive the entropic-gravity force law from the packet in ETRG-0_referee_packet.md; show each step."
```

The command blocks until the agent replies and prints the reply to stdout
(default timeout 600s — these are slow, thinking-hard models, so expect tens of
seconds to a few minutes per call).

### Multi-turn consultation (keep a thread)

By default each call is a **fresh session** (no memory of prior calls). To hold an
ongoing back-and-forth with one agent, reuse a `--session-key`:

```bash
openclaw agent --agent glm --session-key agent:glm:etrg --message "Here is my derivation so far: ..."
openclaw agent --agent glm --session-key agent:glm:etrg --message "Given that, does the low-energy limit recover Newtonian gravity?"
```

Same key → same conversation, so the agent remembers what it already told you.
Use a different key (e.g. `agent:glm:review-2`) to start a clean thread.

### Machine-readable replies

Add `--json` if you want to parse the reply programmatically instead of reading prose:

```bash
openclaw agent --agent kimi-code --message "Write a numpy script that checks eq. (14)" --json
```

### If you (Fable) are yourself an OpenClaw agent

Instead of the CLI you can use the **`sessions_send`** tool directly:
`sessions_send({ agentId: "deepseek", message: "..." })` — it targets the agent by
id and returns its reply. Use `sessions_spawn` to run one as a background sub-agent.

## Working notes

- **State is per-call unless you pass `--session-key`.** For a one-shot question,
  include everything the agent needs in the message (or point it at a file in this
  directory). Don't assume it remembers an earlier call.
- **They are independent models, not a hive.** They don't see each other's replies.
  If you want them to cross-check, pass one agent's output to another explicitly.
- **Costs run on the Together.ai account** (paid per token). `high` thinking + big
  contexts means each call is non-trivial; prefer targeted questions over dumping
  the whole problem repeatedly.
- **Overriding thinking per call:** append `--thinking medium` (or `off`, `max`,
  etc.) to a single call if `high` is overkill for a quick question.

## Suggested collaboration patterns

- **Independent derivation + cross-check:** ask `deepseek` and `glm` the *same*
  derivation separately, then compare. Divergence flags where the physics is subtle.
- **Derive then verify numerically:** get the closed-form result from `deepseek`,
  hand it to `kimi-code` to implement and check against limits/known values.
- **Adversarial review:** give one agent your current result and ask it to *try to
  break it* — find the step that fails, the missing assumption, the wrong sign.
- **Divide the problem:** parcel independent sub-lemmas to different agents in
  parallel (separate terminals / separate session keys), then assemble.

---
*Configured 2026-07-09. Agents live in `~/.openclaw/openclaw.json`; run
`openclaw agents list` to see them. If a model id ever stops resolving, Together's
catalog may have moved — check with the person who set this up.*
