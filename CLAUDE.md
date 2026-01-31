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
