```
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
```

## Repository Overview

This is the **HUST-PhD-Thesis-Latex** repository, containing an unofficial LaTeX class for the Ph.D. Thesis Template of Huazhong University of Science and Technology (HUST). The template is maintained by Xinze Zhang and contributors, with the latest version being V3.1.4x (July 2025).

## Key Files and Structure

### Core LaTeX Files
- **`main.tex`**: Main entry point of the thesis. Configures document class, packages, and includes all thesis components.
- **`HUSTthesis.cls`**: Thesis class file defining the overall document structure and formatting.
- **`HUSTtils.sty`**: Style package with additional utilities and customizations.
- **`HUSTThesis.bst`**: BibTeX style file for formatting references.

### Document Structure
```
body/
├── cover.tex          # Thesis cover page and copyright information
├── chapter/
│   ├── intro.tex      # Introduction
│   ├── cryptographic_primitives.tex  # Cryptographic primitives chapter
│   ├── bf.tex         # Chapter on some topic (abbreviation: bf)
│   ├── univ.tex       # Chapter on another topic (abbreviation: univ)
│   ├── overview.tex   # Overview chapter
│   └── ack.tex        # Acknowledgments
└── appendix/
    └── app.tex        # Appendix

ref/
└── thesis.bib         # Bibliography database

supply/
├── figures/           # Figure files
└── font/              # Font files

float/                 # Floating figure directories per chapter
mdbody/                # Markdown versions of chapters (for reference)
```

## Building the Thesis

### Recommended Setup
- **Editor**: VSCode with LaTeX Workshop extension (configuration provided in `.vscode/settings.json`)
- **TeX Distribution**: TeXLive (latest version recommended)

### Compilation Process
The LaTeX Workshop extension is configured for automatic compilation on save. The default recipe is:
```
xelatex -> bibtex -> xelatex*2
```

To manually compile:
```bash
# Compile with xelatex
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex

# Generate bibliography
bibtex main

# Compile twice more to resolve references
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```

### Cleanup
The LaTeX Workshop extension automatically cleans auxiliary files on successful compilation. To manually clean:
```bash
rm -f main.aux main.bbl main.blg main.idx main.ind main.lof main.lot main.out main.toc main.acn main.acr main.alg main.glg main.glo main.gls main.fls main.fdb_latexmk main.snm main.synctex.gz main.nav main.vrb main.thm main.xdv
```

## Document Class Options

**Format Options (choose one)**:
- `draftformat`: Draft version with headers (default)
- `finalformat`: Blind review version without headers

**Header Color Options (choose one)**:
- `blackhead`: Black header text (default)
- `redhead`: Red header text

Example usage:
```latex
\documentclass[draftformat,blackhead]{HUSTthesis}
```

## Customization

### Packages and Macros
- All additional packages are loaded in `main.tex`
- Custom macros for mathematical notation are defined in `main.tex`
- The `HUSTtils.sty` file contains reusable style definitions

### Figures
- Figures are stored in `supply/figures/`
- Chapter-specific figures can be placed in `float/` subdirectories

### References
- Bibliography entries are stored in `ref/thesis.bib`
- Chinese references require `language=chinese` or `langid=chinese` field

## Beamer Template

A separate beamer template is available in `_ThesisBeamer/` directory:
- Main file: `_ThesisBeamer/slice.tex`
- Theme file: `_ThesisBeamer/beamerthemeBFH.sty`
- VSCode configuration: `_ThesisBeamer/.vscode/settings.json`

## Version History

Key versions (with 'x' indicating Xinze Zhang's modifications):
- **V3.1.4x (2025-07)**: Updated appendices
- **V3.1.3x (2025-04)**: Added dual supervisor support
- **V3.1.2x (2024-01)**: Reorganized file structure, added beamer template
- **V3.1 (2021-09)**: Updated committee page, indentation, references
- **V3.0 (2020-11)**: Updated cover page, font handling

## Research Writing Guidelines

### Literature Review Best Practices

Based on experience writing the searchable encryption survey sections, follow these principles:

#### 1. Verify All Citations Rigorously
- **Never rely on memory** for paper titles, authors, or venues
- Always cross-check with Google Scholar or DBLP before adding bib entries
- Common mistakes to avoid:
  - Incorrect author lists (e.g., omitting or adding wrong authors)
  - Wrong paper titles (e.g., confusing similar-sounding papers)
  - Wrong publication years or venues
- Example: The paper "Forward and Backward Private Searchable Encryption" is by Bost, Minaud, and Ohrimenko (CCS 2017), not the BKC construction from CRYPTO 2013

#### 2. Structure Surveys by Technical Evolution
Organize related work sections chronologically within each theme:
```
Foundational Work (Year) → Technical Breakthrough (Year+1) →
Optimization/Extension (Year+2) → Recent Advances (Current)
```

For example, in backward privacy for SSE:
- 2016: Bost's Σoφoς (forward privacy foundation)
- 2017: Bost et al. (first backward privacy construction)
- 2018: Sun et al. (Janus++, practical SPE-based) & Chamani et al. (algebraic approach)
- 2019: Zuo et al. (stronger Type-III backward privacy)
- 2020: Demertzis et al. (sublinear client storage)

#### 3. Ensure Every Claim Has Citations
- Avoid unsupported statements like "existing research explores X approach"
- Each technical route/direction must have specific paper citations
- If no specific paper exists, rephrase to indicate it's a general direction

#### 4. Key Papers by Research Direction

**Dynamic SSE with Forward/Backward Privacy:**
- Forward Privacy: Bost CCS 2016 (Σoφoς)
- Backward Privacy (foundational): Bost et al. CCS 2017
- Practical Backward Privacy: Sun et al. CCS 2018 (Janus++)
- Stronger Backward Privacy: Zuo et al. ESORICS 2019

**Multi-User SSE:**
- Multi-Key SSE: Popa et al. CCS 2013
- Attribute-Based: Zheng et al. INFOCOM 2014 (VABKS), Sun et al. TPDS 2016
- Proxy Re-Encryption: Shao et al. Information Sciences 2010, Wang et al. JSS 2012

**Verifiable SSE:**
- Early work: Kurosawa & Ohtaki CANS 2013 (verifiable updates)
- iO-based: Cheng et al. CCS 2015
- Conjunctive queries: Sun et al. INFOCOM 2015
- No-dictionary: Ogata & Kurosawa FC 2017
- Multi-user: Liu et al. TDSC 2020
- Forward secure + verifiable: Zhang et al. ESORICS 2019

#### 5. Common Pitfalls to Avoid
- Don't confuse similar acronyms (e.g., VSE vs VSSE vs VABKS)
- Distinguish between "first to propose" vs "first practical" vs "first with property X"
- Be careful with multi-author papers - verify all author names exactly
- Check that venue abbreviations are correct (e.g., CCS vs ACM CCS, ESORICS vs EuroS&P)
- Ensure page numbers and DOIs are accurate for top-tier conference papers

#### 6. Writing the Survey Section
For each technical direction, cover:
1. **Problem definition**: What challenge does this direction address?
2. **Key papers**: 2-4 seminal works with specific contributions
3. **Technical evolution**: How did the field progress?
4. **Current limitations**: What remains unsolved?
5. **Connection to your work**: Why is this relevant to your research?

#### 7. BibTeX Entry Standards
- Use consistent formatting across all entries
- Include DOIs for all recent papers (2010+)
- Use proper LaTeX escaping for special characters (e.g., `\"o` for ö)
- For Chinese papers, add `language={chinese}` or `langid={chinese}`
- Verify author name capitalization (e.g., "van Dijk" vs "Van Dijk")
