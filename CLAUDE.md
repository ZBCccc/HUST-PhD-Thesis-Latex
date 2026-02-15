# CLAUDE.md

This file provides working guidance for the thesis project in this directory.

## Project Scope

- Project: HUST master thesis (searchable encryption)
- Main file: `main.tex`
- Active chapters:
  - `body/chapter/intro.tex`
  - `body/chapter/bf.tex`
  - `body/chapter/commitment.tex`
  - `body/chapter/experiments.tex`
  - `body/chapter/conclusion.tex`

## Current Writing Baseline (2026-02-13)

1. `intro.tex`: mostly drafted, needs polishing and citation checks.
2. `bf.tex`: first part drafted; algorithm/security sections still incomplete.
3. `commitment.tex`: skeleton with TODO blocks, needs full draft.
4. `experiments.tex`: evaluation structure exists, data/results pending.
5. `conclusion.tex`: outline only.

## Build

Recommended compile chain:

```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
bibtex main
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```

## Writing Rules for This Thesis

1. Keep notation consistent across chapters (system entities, leakage, correctness, verifiability).
2. For each new claim, provide either a formal argument or a citation.
3. In Chapter 2 and 3, always separate:
   - threat model
   - construction
   - correctness/verifiability analysis
   - leakage discussion
4. For Chapter 4, ensure each figure/table has:
   - metric definition
   - baseline comparison
   - concise interpretation
5. Do not use meta-writing phrases in chapter text (e.g., "for writing style", "for ease of exposition").
6. Replace any writing-process narration with technical statements about model, assumptions, or claims.
7. Avoid template AI phrasing in chapter text, including "本文将/我们将/总之/显而易见/值得注意的是/随着……发展".
8. Do not use vague adjectives (e.g., "huge", "revolutionary", "very important") without formal support.
9. If data, theorem constants, or empirical numbers are missing, mark placeholders as `【待补充】` and do not fabricate.
10. Security proof sections must follow "game/hybrid + reduction": specify adversary model, advantage function, reduction algorithm, bad events, and final bound derivation.
11. Keep paragraph tone review-ready: technical and constrained, no conversational wording.

## Citation Hygiene

- Bibliography file: `ref/thesis.bib`
- Check every cited key exists in `thesis.bib` before final compile.
- Prefer consistent venue naming and author formatting.

## Collaboration Notes

- When editing chapter text, update progress in root workspace docs:
  - `../控制面板.md`
  - `../01-论文生产/选题管理/00-选题记录.md`
  - `../记忆库/论文系统初始化总结.md`
- For PDF reading and quoting prep, prefer Markdown papers in:
  - `../01-论文生产/素材库/论文Markdown库/`
  - default format is Xray-style extraction (`ljg-xray-paper`), not raw full-text dump
