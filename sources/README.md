# Sources

Input documents for the resilience proposals database.

## Structure

Each source gets its own folder:

```
sources/
├── index.json              # Master list of all sources
├── README.md               # This file
└── <source-id>/            # One folder per source
    ├── source.pdf          # Original document (or source.md, etc.)
    ├── index.md            # Human-readable TOC with entry links
    ├── <source>-full.md    # Full extracted text (optional)
    └── proposals/          # Individual proposal extractions
        ├── proposal-1.md
        └── ...
```

## Proposal File Format

Each proposal markdown file should have this header format:

```markdown
# Proposal Title

**Source**: Source Name, Section/Proposal #X
**Original**: https://original-url.com/document

## Quoted passage(s)
> Exact text from the original source...

## Summary (optional)
Brief interpretation or context.
```

The **Original** URL links to the public source document. This allows readers to verify quotes and access the full context.

## Public vs Private Sources

Most sources are public and published to the GitHub Pages site. Two sources are private:
- `cltr-defacc-uk` - Internal CLTR document (not published) — **Private Source #1**
- `entente-threats` - Internal threat analysis (not published) — **Private Source #2**

Private sources are:
- Listed in `.gitignore` and excluded from the public repository
- Remain in the local working copy for reference
- Can be linked from interventions using relative paths (works locally, shows 404 on GitHub)

### Linking to Private Sources

When an intervention references a private source, use this format:
```markdown
## Sources
- [Private Source #1: CLTR DefAcc](../sources/cltr-defacc-uk/proposals/example.md) *(local only)*
- [Private Source #2: Entente](../sources/entente-threats/proposals/example.md) *(local only)*
```

The `*(local only)*` annotation signals to readers that this link only works in local copies.

## Adding a New Source

1. **Create folder**: `sources/<source-id>/`
2. **Add document**: Copy PDF/URL/text to `source.pdf` (or appropriate format)
3. **Register in index.json**:
   ```json
   {
     "id": "source-id",
     "name": "Human-readable name",
     "url": "https://...",
     "type": "pdf|url|text",
     "status": "pending",
     "folder": "source-id/"
   }
   ```
4. **Extract**: Create `raw/` folder with per-section extractions
5. **Process**: Use tiling tree method to create problem/intervention entries
6. **Map**: Create `mapping.json` linking source sections to entries
7. **Update status**: Change `status` to "processed" when done

## Processing Workflow

See `guide-to-making-problems.md` for the full extraction methodology:
- Tiling tree method for identifying problems
- Intervention scoping and pipeline structure
- Sub-intervention criteria
- Research requirements for implementers

**Meta-lists**: When a source is a "list of lists", extract useful sub-lists as separate sources before processing. Add each referenced list to `index.json` with its own folder.

## Current Sources

| ID | Name | Status | Notes |
|----|------|--------|-------|
| peregrine-2025 | The 2025 Peregrine Report | processed | 208 proposals → problem/intervention entries |
| cltr-defacc-uk | CLTR Defensive Acceleration List (UK) | processed | 29 UK-centric interventions, ~5 generalizable |
| convergent-gap-map | Convergent Research Gap Map | pending | 101 R&D gaps. Filter for AI safety/biosecurity only |
| mit-risk-repository | MIT AI Risk Repository | pending | 2244 entries. Taxonomy stress-test, not bulk import |
| epistemic-security | Epistemic Security (early thinking) | pending | Already a tiling tree - could become problem entry |
| project-grasp | Project GRASP (CeSIA) | pending | Notion DB, needs manual export |
| openagent-ecosystem | Secure AI Agent Ecosystem | pending | Schmidt Sciences PDF on agent security |
| bowman-checklist | Sam Bowman's AI Safety Checklist | pending | ~25 goals across 3 chapters, narrative format |
| biosecurity-lists | List of Lists of Biosecurity Projects | pending | Meta-list of 8 sources, may overlap with Peregrine |
| atlas-ai-resilience | Atlas AI Resilience Gap Map | pending | 119 gaps + related lists |
| atlas-cyber | Atlas Cybersecurity Projects | pending | 23 fundable projects |
| ai-safety-lists | List of Lists of AI Safety Projects | pending | Meta-list, Notion page |
