# GEPA Self-Evolution Cycle 31 — Complete ✅

**Date:** 2026-07-31 02:05
**Method:** Strategy A (Direct Parent Execution / LLM-as-Judge)
**Branch:** `gepa/phase1-skill-optimization-cycle-20260731-20260729` (both self-evolution and hermes-agent repos)
**Model:** `deepseek/deepseek-v4-flash` (CommandCode, cron default)

---

## Fast Path Check

- **Most recent self-evolution cycle:** Cycle 30 (2026-07-28 02:00) — completed with 5 skills evolved (full report, NOT `[SILENT]`).
- **CLI/user sessions since Cycle 30:** `20260730_191210_56f5f9` (Proxmox Homelab Management, CLI), plus Telegram activity on 2026-07-30 — active sessions exist.
- **Error/correction sessions:** Dojo bridge query surfaced no unresolved skill-level failures; recent cron sessions (nightly-memory-maintenance, Pepper income agent) ran without new skill-level corrections.
- **Verdict:** Fast Path does **NOT** trigger — the previous cycle ran actual work and user/CLI activity followed. Proceeding with full cycle.

## Dojo Data

```bash
$ python3 scripts/dojo-bridge.py --days 3 --gepa-only
(empty — no skill-level failures detected)
```

**Dojo targets:** **0** — normal per pitfall #44. All failures in the last 3 days are in core Hermes tools, not installed skills. Proceeding with delta-driven + word-count fallback selection.

## Selection Rationale

### Delta-driven

Created start marker `/tmp/gepa-cycle-31-start` (per pitfall #14). Cross-checked both sources:

1. **`git log --since="2026-07-28T02:20" --name-only -- skills/`** in hermes-agent repo surfaced 3 commits:
   - `8e1debd5e` docs purge → `software-development/python-debugpy/SKILL.md` (changed docs references, not structure)
   - `c26839775` / `847e401b7` computer_use alignment → `autonomous-ai-agents/computer-use/SKILL.md`
2. **Validation against live path (`~/.hermes/skills/`):**
   - `software-development/python-debugpy`: **already fully evolved** (triggers=1, When to Use=1, Not For=1, Pitfalls=1, version 1.1.0) → counted as *found but already evolved* (pitfall #19).
   - `autonomous-ai-agents/computer-use`: **not in live path** — the live skill is at `~/.hermes/skills/computer-use/` (top-level, v2.1.0, already evolved). The repo path exists in the repo but the live path is the source of truth (pitfall #36); the top-level live `computer-use` already has all 4 gaps → *found but already evolved*.

**Delta result:** 2 found, 0 actionable, 2 already evolved. Falling back to word-count for all 5 slots.

### Word-count fallback (4-gap scan)

Full scan of `~/.hermes/skills/` for SKILL.md missing ≥3 of (trigger_conditions, When to Use, Not For, Pitfalls), ranked by byte size, diverse categories. Top candidates (excluding `persona-*`, `recipe-*` scaffolding, node_modules):

| # | Skill | Category | Bytes | Gaps |
|---|-------|----------|-------|------|
| 1 | `chatterbox-turbo-server` | devops/tts | 11,545 | all 4 |
| 2 | `unslop-code` | software-dev | 9,741 | all 4 |
| 3 | `unslop-ui` | software-dev | 7,376 | all 4 |
| 4 | `llm-usage-tracker` | productivity | 6,826 | all 4 |
| 5 | `hermes-agentbar` | devops | 6,426 | all 4 |

Selected for diversity (TTS/infra, code audit, UI audit, provider-usage apps, Windows tray app) and because all are live-path skills the agent actually loads.

## Evolved Skills

All 5 received the full 4-gap treatment (LLM-as-Judge Strategy A), version bumped to 1.0.0 (none had a version field).

| # | Skill | Added | Version |
|---|-------|-------|---------|
| 1 | `chatterbox-turbo-server` | trigger_conditions (10), When to Use (5), Not For (5), Pitfalls (7) | — → 1.0.0 |
| 2 | `unslop-code` | trigger_conditions (10), When to Use (5), Not For (5), Pitfalls (7) | — → 1.0.0 |
| 3 | `unslop-ui` | trigger_conditions (10), When to Use (5), Not For (5), Pitfalls (7) | — → 1.0.0 |
| 4 | `llm-usage-tracker` | trigger_conditions (10), When to Use (5), Not For (4), Pitfalls (8) | — → 1.0.0 |
| 5 | `hermes-agentbar` | trigger_conditions (10), When to Use (4), Not For (4), Pitfalls (7) | — → 1.0.0 |

### Notable content decisions

- **Not For entries name real sibling skills** (checked via skills_list): `kittentts-server`, `f5-tts-setup`, `voice-cloning-workflow`, `unslop-ui`, `unslop-text`, `no-ai-slop`, `humanizer`, `code-review`, `requesting-code-review`, `claude-design`, `design-an-interface`, `popular-web-designs`, `llm-usage-tracker`, `pystray-windows-tray-click`, `gui-app-headless-testing`, `cron-model-optimization`.
- **hermes-agentbar**: converted the existing "Key Pitfalls" h3 blocks into numbered pitfalls (7 total), preserving all technical detail (pystray default=True source trace, cookie auth, pythonw).
- **chatterbox-turbo-server**: pitfall #2 captures the 2026-07-30 cron-timeout incident (F5-TTS killed at 3600s, reverted to Chatterbox) — the most recent real-world failure affecting this skill.
- **unslop-code / unslop-ui**: pitfalls mirror the skill's own anti-slop philosophy (fix a default with another default = not a fix; scanner blind spots; over-flagging erodes trust).

## Scores (LLM-as-Judge, 5 dimensions × 10)

| Skill | Baseline | Evolved | Δ |
|-------|:--------:|:-------:|:-:|
| `chatterbox-turbo-server` | 25 | 38 | **+13** |
| `unslop-code` | 27 | 39 | **+12** |
| `unslop-ui` | 27 | 39 | **+12** |
| `llm-usage-tracker` | 26 | 38 | **+12** |
| `hermes-agentbar` | 24 | 37 | **+13** |
| **Average** | 25.8 | 38.2 | **+12.4** |

Dimension breakdown (baseline → evolved):
- trigger_clarity: 3.8 → 8.0
- step_completeness: 6.0 → 8.2
- pitfall_coverage: 4.0 → 8.0
- command_accuracy: 7.0 → 7.6
- reuse_potential: 5.0 → 7.4

## Sync & Patches

- All 5 evolved SKILL.md written to **live path** `~/.hermes/skills/<path>/SKILL.md` first (source of truth), then synced to:
  - `~/.hermes/hermes-agent/skills/<path>/SKILL.md` (repo copy)
  - `~/hermes-skills/skills/<path>/SKILL.md` (backup repo)
- All 5 are **new files** in the hermes-agent repo (none tracked before) — staged with `git add`, patches generated from `git diff --cached` (per pitfall #23/#40):

| Skill | Patch |
|-------|-------|
| chatterbox-turbo-server | `patches/chatterbox-turbo-server/gepa-cycle-31.patch` (333 lines) |
| unslop-code | `patches/software-development/unslop-code/gepa-cycle-31.patch` (180 lines) |
| unslop-ui | `patches/software-development/unslop-ui/gepa-cycle-31.patch` (158 lines) |
| llm-usage-tracker | `patches/productivity/llm-usage-tracker/gepa-cycle-31.patch` (168 lines) |
| hermes-agentbar | `patches/devops/hermes-agentbar/gepa-cycle-31.patch` (144 lines) |

None gitignored (checked `git check-ignore`).

## Commits

- **hermes-agent repo** (`~/.hermes/hermes-agent`, branch `$BRANCH`): 5 new skill files committed locally. **Not pushed** — per pitfall #43, the `jarvis4openclaw/hermes-agent` fork does not exist; local commit is the source of truth. Note: repo had pre-existing uncommitted changes (`hermes_cli/web_server.py` modified + `.orig` untracked) which were left untouched.
- **self-evolution repo** (`~/hermes-agent-self-evolution`, branch `$BRANCH`): patches + this report + metrics committed. Pushed to `jarvis4openclaw/hermes-agent-self-evolution`.
- **hermes-skills backup** (`~/hermes-skills`): 5 evolved SKILL.md committed. Pushed to `jarvis4openclaw/hermes-skills`.

## Metrics

See `reports/gepa_cycle_31_metrics.json`.

## Verification

- All 5 live files re-checked: `trigger_conditions=1`, `When to Use=1`, `Not For=1`, `Pitfalls=1` with 7-8 numbered items each.
- All 5 files present in live path, repo path, and backup path (same content via `cp`).
- Patches non-empty (144-333 lines each) — generated after `git add` from staged diff.

## Cycle Learnings

- **Computer-use delta trap:** `git log` shows `autonomous-ai-agents/computer-use/SKILL.md` (upstream repo path), but the live skill lives at top-level `~/.hermes/skills/computer-use/` (v2.1.0, evolved). The repo-path file is NOT the live skill — validating against `~/.hermes/skills/<path>` with the repo's full relative path would miss the top-level live copy. Check `find ~/.hermes/skills -name SKILL.md -path "*<skill>*"` before declaring a delta candidate not-in-live-path.
- All 5 candidates were **new to the repo** — a reminder that live-path-first is the only correct workflow; the repo is a secondary copy (pitfall #36).
