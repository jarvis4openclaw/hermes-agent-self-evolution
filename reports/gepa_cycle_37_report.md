# GEPA Self-Evolution Cycle 37 — Complete ✅

**Date:** 2026-08-07 02:20 — **Branch:** `gepa/phase1-skill-optimization-cycle-20260807-20260807`
**Method:** Strategy A (Direct Parent Execution / LLM-as-Judge) — model `deepseek/deepseek-v4-flash`

---

## Fast Path Check

Previous cycle (36, 2026-08-06 02:25) did real work (4 skills evolved). Since then, real user/agent activity followed:
- **chatterbox-turbo-server** modified 2026-08-06 10:03 (already fully evolved v1.1.0 — checked, no gaps)
- **self-hosted-app-deployment** modified 2026-08-06 10:30 (genuine gap: v1.0.0, no When to Use / Not For, only 4 pitfalls)
- **hermes-config-management** still carries its malformed trigger_conditions block (top-level, not under `metadata.hermes`) — deferred from cycle 36, structural work still needed

Fast Path does **not** trigger — full cycle run.

## Dojo Data

`dojo-bridge.py --days 3 --gepa-only` → **0 targets** (normal per pitfall #44; all failures in core tools). Skills are healthy.

## Selection

| Source | Found | Actionable | Already evolved |
|--------|:-----:|:----------:|:---------------:|
| Dojo | 0 | 0 | — |
| Delta-driven | 7 | 2 | 5 (Cycle-36 skills all v1.1.0+ with 4 gaps; chatterbox-turbo-server v1.1.0 already evolved; hermes-skills-optimization v1.2.0 already evolved) |
| Word-count fallback | — | 3 slots | — |

**Delta-driven actionable (2):**
- `devops/self-hosted-app-deployment` (1.0.0 → 1.1.0) — genuine user modification Aug 6 10:30 (LCC deploy work); had trigger_conditions but missing When to Use / Not For; only 4 pitfalls
- `devops/hermes-config-management` (1.2.0 → 1.3.0) — **structural fix**: the trigger_conditions block sat at top-level of frontmatter (malformed — cycle 36 deferred it). Moved under `metadata.hermes`, added When to Use / Not For, converted the loose "Pitfalls" bullets into a first-class 10-item numbered Pitfalls section.

**Word-count fallback (3):** picked from the 4-gap scan (3 of 4 gaps each, high word count, different categories):
- `creative/claude-design` (25,117 bytes, 1.1.0 → 1.2.0) — missing trigger_conditions + Not For; converted bullet Pitfalls to numbered
- `mlops/training/grpo-rl-training` (17,225 bytes, 1.0.0 → 1.1.0) — missing trigger_conditions + Not For + Pitfalls; already had a decision table and troubleshooting guide
- `mlops/inference/outlines` (15,976 bytes, 1.0.0 → 1.1.0) — missing trigger_conditions + Not For + Pitfalls

Skipped: `openhue`/`sonoscli` — clawdbot-format third-party skills (pitfall #46). `cron-model-optimization` — already has 25 numbered pitfalls, partial-gap fill deferred (same reasoning as cycle 36).

## Optimization (Strategy A)

Applied the 4-gap template to 5 skills:

| Skill | Version | Changes |
|-------|---------|---------|
| `creative/claude-design` | 1.1.0 → 1.2.0 | +trigger_conditions (12), +When to Use (4), +Not For (5, disambiguates vs popular-web-designs/design-md/excalidraw/architecture-diagram/sketch), converted 7 bullet pitfalls → 10 numbered (fake tool calls, external prompt drift, doctrine stripping, over/under-asking, generic SaaS slop, browser-verification claims, source fidelity, copyright, contrast/responsive). |
| `mlops/training/grpo-rl-training` | 1.0.0 → 1.1.0 | +trigger_conditions (12), +Not For (5, vs fine-tuning-with-trl/simpo-training/peft-fine-tuning/pytorch-fsdp/unsloth), +Pitfalls (10: loss-vs-reward, reward signature mismatch, mode collapse, KL explosion, flat rewards, group size, vLLM integration, OOM, incremental shaping, holdout eval). |
| `mlops/inference/outlines` | 1.0.0 → 1.1.0 | +trigger_conditions (10), +When to Use (5), +Pitfalls (8: API models unsupported, transformers version skew, schema compile failures, Optional/defaults, enum context, latency tradeoff, backend differences, valid-but-wrong JSON). |
| `devops/self-hosted-app-deployment` | 1.0.0 → 1.1.0 | +When to Use (4), +Not For (4, vs proxmox-ssh-lifecycle/server-health/startos), expanded 4 → 10 pitfalls (demo API drift, hidden hardcoded domains, conditional deps, network_mode+ports, nesting=1, single-200 victory). |
| `devops/hermes-config-management` | 1.2.0 → 1.3.0 | **Structural fix**: moved trigger_conditions from malformed top-level frontmatter into `metadata.hermes` (27 triggers preserved), +When to Use (5), +Not For (5, vs hermes-provider-config/cron-model-optimization/hermes-config-backup/hermes-config-post-audit-recovery/hermes-profile-setup), converted the embedded "### Pitfalls" bullets → first-class 10-item numbered section. |

**Scores (0–10):**

| Skill | trig | steps | pitf | cmds | reuse | Δ |
|-------|------|-------|------|------|-------|---|
| claude-design | 3→8 | 7→8 | 4→9 | 8→8 | 7→8 | **+11** |
| grpo-rl-training | 3→8 | 6→7 | 1→8 | 7→7 | 6→8 | **+13** |
| outlines | 3→8 | 6→7 | 1→8 | 7→7 | 5→7 | **+12** |
| self-hosted-app-deployment | 5→8 | 6→8 | 4→9 | 8→8 | 6→8 | **+12** |
| hermes-config-management | 4→8 | 7→8 | 4→9 | 7→8 | 7→8 | **+12** |

**Average Δ: +12.0**

## Sync

- Live path (source of truth): `~/.hermes/skills/` — 5 SKILL.md updated
- Repo path: `~/.hermes/hermes-agent/skills/` — synced; **4 are new to the repo** (self-hosted-app-deployment, hermes-config-management, grpo-rl-training, outlines — previously live-path-only, pitfall #33), claude-design tracked
- Backup: `~/hermes-skills/skills/` — all 5 synced

## Patches

Generated from the cycle-37 commit diff (`dec261e54c`):
- `patches/claude-design/gepa-cycle-37.patch` (77 lines)
- `patches/grpo-rl-training/gepa-cycle-37.patch` (609 lines)
- `patches/outlines/gepa-cycle-37.patch` (681 lines)
- `patches/self-hosted-app-deployment/gepa-cycle-37.patch` (119 lines)
- `patches/hermes-config-management/gepa-cycle-37.patch` (567 lines)

## Commits

- **hermes-agent repo** (local only, per pitfall #43 — do NOT push): `dec261e54c` on branch `gepa/phase1-skill-optimization-cycle-20260807-20260807`
- **self-evolution repo**: patches + report + metrics on same branch (committed below)
- **hermes-skills backup**: synced + committed below (push to jarvis4openclaw/hermes-skills)

## Notes / Pitfalls Hit

- Pitfall #40 (tracked files need `git add` before `git diff --cached`): all 5 files staged before patch generation — clean patches, no 0-line diffs.
- Pitfall #33 (live-path-only skills): 4 of 5 targets had no repo copy; `mkdir -p` + `cp` handled it, and they now exist as new files in the repo commit.
- Pitfall #19/#34 (delta candidates already evolved): reported accurately — 5 of 7 delta candidates were already evolved, 2 actionable.
- Cycle-36 deferred item resolved: `hermes-config-management`'s malformed trigger_conditions block is now under `metadata.hermes`.
- Pre-existing dirty state in hermes-agent repo (`hermes_cli/web_server.py` M) left untouched — pre-dates this cycle and is not a skill file.
