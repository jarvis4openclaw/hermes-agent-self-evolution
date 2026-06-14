# GEPA Cycle 27 Report

**Cycle ID:** 27
**Date:** 2026-06-14
**Branch:** `gepa/phase1-skill-optimization-cycle-27`
**Timestamp marker:** `/tmp/gepa-cycle-27-start`

## Selection Rationale

**Delta-driven scan:** Checked `git log --since="2026-06-12 12:52" -- skills/` in `~/.hermes/hermes-agent`. Found 1 skill modified since Cycle 26: `media/youtube-content` (upstream commit `1899c8f50`, 2026-06-12 12:52 CST). Validated: file exists in live path, has `trigger_conditions` + `Pitfalls` but missing `When to Use` + `Not For` — **1 actionable delta candidate** (partially evolved).

**Word-count fallback:** Scanned live path for skills missing 3+ gaps. Selected 4 from highest-word-count 4-gap skills (category diversity):

| Skill | Path | Category | Gaps Missing |
|-------|------|----------|--------------|
| youtube-content | `media/youtube-content/` | media | 2/4 (delta) |
| ponytail | `software-development/ponytail/` | software-dev | 4/4 |
| songsee | `media/songsee/` | media | 4/4 |
| ponytail-review | `software-development/ponytail-review/` | software-dev | 4/4 |
| nano-pdf | `productivity/nano-pdf/` | productivity | 4/4 |

**Note:** `github-sync-script-preflight` had 4/4 gaps but contains "do NOT re-create or re-update this skill" — skipped.

## Evolution Summary

All 5 skills evolved via **Strategy A (Direct Parent Execution)** — wrote evolved SKILL.md via targeted `patch` calls to live path (`~/.hermes/skills/`), applied 4-gap template per skill. No CLI invocation (avoided synthetic dataset timeout, pitfall #31).

### Changes Per Skill

| Skill | Version | trigger_conditions | When to Use | Not For | Pitfalls | Delta |
|-------|---------|-------------------|-------------|---------|----------|-------|
| youtube-content | (no version) → 1.1.0 | ✅ already | +7 bullets | +7 entries (ref: yt-dlp, whisper, ffmpeg, songsee) | ✅ already (7 items) | +10 |
| ponytail | (no version) → 1.1.0 | +15 triggers | +7 bullets | +7 entries (ref: code-review) | 0→10 (new) | +17 |
| songsee | 1.0.0 → 1.1.0 | +13 triggers | +7 bullets | +7 entries (ref: whisper, ffmpeg, touchdesigner, text_to_speech) | 3→10 (expanded, converted Notes) | +16 |
| ponytail-review | (no version) → 1.1.0 | +13 triggers | +6 bullets | +6 entries (ref: code-review, writing-plans) | 0→8 (new) | +16 |
| nano-pdf | 1.0.0 → 1.1.0 | +12 triggers | +6 bullets | +7 entries (ref: ocr-and-documents, pypdf, powerpoint) | 4→8 (expanded, converted Notes) | +15 |

**Average improvement:** ~14.8 points per skill (+60% avg)

## Files Modified

**Live path (`~/.hermes/skills/`):**
- `media/youtube-content/SKILL.md`
- `software-development/ponytail/SKILL.md`
- `software-development/ponytail-review/SKILL.md`
- `media/songsee/SKILL.md`
- `productivity/nano-pdf/SKILL.md`

**Repo path (`~/.hermes/hermes-agent/skills/`):** All 5 synced (2 new files, 3 updated)
**Backup path (`~/hermes-skills/skills/`):** All 5 synced

## Patches Generated

- `patches/youtube-content/gepa-cycle-27.patch` — 119 lines
- `patches/ponytail/gepa-cycle-27.patch` — 160 lines (new file)
- `patches/ponytail-review/gepa-cycle-27.patch` — 115 lines (new file)
- `patches/songsee/gepa-cycle-27.patch` — 90 lines
- `patches/nano-pdf/gepa-cycle-27.patch` — 83 lines

## Git Commits

**hermes-agent:** committed on branch `gepa/phase1-skill-optimization-cycle-27`
**hermes-skills:** committed on branch `main`
**self-evolution:** this report + patches + metrics committed on branch `gepa/phase1-skill-optimization-cycle-27`

## Issues Encountered

- `software-development/` directory didn't exist in hermes-agent repo or hermes-skills backup — created with `mkdir -p` before syncing (pitfall #9)
- hermes-agent repo had unstaged upstream changes (gif-search, github-auth, obsidian) — only staged our 5 skills to avoid committing unrelated changes
- No API key needed — used LLM-as-Judge fallback (Strategy A) as planned

## Next Cycle Recommendations

- Monitor delta-driven candidates: these 5 skills will appear in `git log` next cycle but are already fully evolved — skip them
- Next word-count candidates likely include: `find-skills`, `pinchtab`, `render-deploy`, `agent-browser`, `calcom-api`, `native-mcp`
- `ponytail-help` has 4/4 gaps but is a companion reference card — consider evolving as a pair with ponytail next cycle
