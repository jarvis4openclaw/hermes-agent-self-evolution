# GEPA Phase 1 Cycle 3 — Skill Optimization Report

**Date:** 2026-04-12  
**Branch:** gepa/phase1-skill-optimization-cycle-3  
**Skills optimized:** 5  

---

## Summary

Cycle 3 focused on improving skill discoverability and runtime reliability across 5 skills. The primary changes were:

1. **trigger_conditions** added to YAML frontmatter — enables the skill router to match user intent to skills more reliably
2. **Pitfalls sections** added — 7 concrete failure modes per skill with actionable fixes
3. **When to Use / Not For** sections** added to codex — reduces mis-invocations on simple tasks

---

## Skills Modified

### 1. `codex` (autonomous-ai-agents)
- **Version:** 1.0.0 → 1.1.0
- **Changes:**
  - Added `trigger_conditions` (6 conditions including phrase matches)
  - Added `## When to Use` section (5 use cases)
  - Added `## Not For` section (4 anti-patterns)
  - Added `## Pitfalls` section (7 pitfalls: pty hang, git repo, API key, yolo scope, worktree cleanup, stalling, branch mismatch)
- **Impact:** Reduces hang-on-startup failures (pty) and repo-less invocations

### 2. `blogwatcher` (research)
- **Version:** 2.0.0 (unchanged)
- **Changes:**
  - Added `trigger_conditions` (7 conditions including RSS phrase matches)
  - Added `## Pitfalls` section (7 pitfalls: JS-rendered feeds, Docker persistence, OPML duplicates, read-all prompt, article accumulation, rate limiting, category case sensitivity)
- **Impact:** Prevents data loss from Docker restarts and automation blocking in scripts

### 3. `find-nearby` (leisure)
- **Version:** 1.0.0 (unchanged)
- **Changes:**
  - Added `trigger_conditions` (6 conditions for location queries)
  - Added `## Pitfalls` section (7 pitfalls: sparse rural results, zip code ambiguity, informal geocoding, unreliable hours, multi-type limit, SKILL_DIR placeholder, Overpass timeout)
- **Impact:** Reduces incorrect "open now" assertions and geocoding failures

### 4. `youtube-content` (media)
- **Version:** unversioned (unchanged)
- **Changes:**
  - Added `metadata.hermes.trigger_conditions` (7 conditions including YouTube URL patterns)
  - Added `## Pitfalls` section (7 pitfalls: auto-caption corruption, partial transcripts, context overflow, short-link failure, livestream errors, auto-generated vs manual captions, age restriction)
- **Impact:** Prevents silent truncation of long videos and mis-handling of restricted content

### 5. `github-auth` (github)
- **Version:** 1.1.0 (unchanged)
- **Changes:**
  - Added `trigger_conditions` (6 conditions including auth error phrases)
  - Added `## Pitfalls` section (7 pitfalls: scope failures, expired tokens, ssh-agent loading, multi-account collision, port 22 blocking, gh setup-git missing, global identity leak)
  - Pitfalls inserted BEFORE existing `## Troubleshooting` section
- **Impact:** Catches most common auth setup failures before they happen

---

## Metrics

| Skill | Lines Added | Pitfalls Added | trigger_conditions |
|-------|-------------|----------------|--------------------|
| codex | +78 | 7 | 6 |
| blogwatcher | +42 | 7 | 7 |
| find-nearby | +38 | 7 | 6 |
| youtube-content | +44 | 7 | 7 |
| github-auth | +82 | 7 | 6 |
| **Total** | **+284** | **35** | **32** |

---

## Patch Files

- `patches/codex/gepa-cycle-3.patch`
- `patches/blogwatcher/gepa-cycle-3.patch`
- `patches/find-nearby/gepa-cycle-3.patch`
- `patches/youtube-content/gepa-cycle-3.patch`
- `patches/github-auth/gepa-cycle-3.patch`

---

## Notes

- Skills were written directly to `~/.hermes/hermes-agent/skills/` (the live skill store)
- `~/.hermes/skills/` is a separate directory — skills were NOT mirrored there (different directory tree)
- Patches generated from `git diff HEAD` in the hermes-agent repo
- Push to remote pending auth configuration
