# Analog IC Notes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a public analog IC knowledge repository organized from MOS device physics to analog blocks, stability, non-idealities, layout, and simulation.

**Architecture:** Markdown-first technical notebook with one focused chapter per topic, a central README learning map, and a small Python verifier for relative links and public-release safety.

**Tech Stack:** Markdown, Mermaid, LaTeX math, Python 3 standard library, pytest.

**Spec:** `docs/superpowers/specs/2026-09-05-analog-ic-notes-design.md`

## Global Constraints
- Process-independent content only.
- No proprietary PDK / model / rule-deck / techfile / production netlist data.
- Avoid overlap with the separate tape-out workflow repository.
- Current technical identity is analog/mixed-signal IC; antenna work is historical and excluded from this repository.

---

### Task 1: Repository structure
- [x] Create README learning map and repository policy files.
- [x] Create focused topic chapters from MOS physics through simulation methods.

### Task 2: Public-release verification
- [x] Add `tools/verify_notes.py` to reject sensitive file types/directories and broken relative links.
- [x] Add four pytest cases covering clean tree, broken link, forbidden extension, and forbidden directory.

### Task 3: Verification
- [x] Run `pytest -q`.
- [x] Run `python tools/verify_notes.py .`.
- [x] Confirm the repository contains no unfinished markers and create a clean ZIP artifact.
