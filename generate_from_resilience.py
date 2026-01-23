#!/usr/bin/env python3
"""Generate projects-v2.json from resilience-proposals markdown files.
Preserves all rich content: Problem, Approach, Current State, Uncertainties, Next Steps, Sources.
"""
import json
import re
from pathlib import Path

SOURCE_DIR = Path('/Users/jonahweinbaum/Desktop/Claude Code/projects/resilience-proposals/interventions-new-new/entries')
OUTPUT_FILE = Path('/Users/jonahweinbaum/Desktop/Claude Code/projects/ListofListofLists/data/projects-v2.json')

GITHUB_BASE = 'https://github.com/jonahwei19/ListofListofLists/blob/main'


def parse_sources_from_text(text):
    """Extract markdown links (http/https) from text."""
    if not text:
        return []
    sources = []
    seen_urls = set()
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(pattern, text):
        url = match.group(2)
        if url.startswith('http') and url not in seen_urls:
            seen_urls.add(url)
            sources.append({
                'text': match.group(1),
                'url': url
            })
    return sources


def extract_peregrine_proposals(raw_content):
    """Extract Peregrine proposal references from RAW EXTRACTION section."""
    proposals = []
    if '## Proposals' in raw_content:
        proposals_section = raw_content.split('## Proposals')[1]
        # Stop at next section or end
        if '\n## ' in proposals_section:
            proposals_section = proposals_section.split('\n## ')[0]

        for line in proposals_section.split('\n'):
            line = line.strip()
            if line.startswith('- Peregrine'):
                # Extract the proposal number
                match = re.search(r'Peregrine\s*#?(\d+)', line)
                if match:
                    num = match.group(1).zfill(3)
                    proposals.append({
                        'text': f'Peregrine 2025 #{num}',
                        'url': f'{GITHUB_BASE}/sources/peregrine-2025/interventions/peregrine-{num}.md'
                    })
    return proposals


def parse_intervention(filepath):
    """Parse a markdown intervention file into structured data."""
    with open(filepath, 'r') as f:
        full_content = f.read()

    # Extract Peregrine proposals from RAW EXTRACTION before cutting it
    peregrine_sources = []
    if '# RAW EXTRACTION' in full_content:
        raw_section = full_content.split('# RAW EXTRACTION')[1]
        peregrine_sources = extract_peregrine_proposals(raw_section)

    # Now cut at RAW EXTRACTION for main content parsing
    content = full_content
    if '# RAW EXTRACTION' in content:
        content = content.split('# RAW EXTRACTION')[0]

    # Extract title (first H1)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem

    # Extract tag
    tag_match = re.search(r'\*\*Tag\*\*:\s*(\w+)', content)
    tag = tag_match.group(1) if tag_match else "Science"

    # Extract status
    status_match = re.search(r'\*\*Status\*\*:\s*(.+)', content)
    status = status_match.group(1).strip() if status_match else "Unknown"

    # Extract sections
    sections = {}
    current_section = None
    current_content = []

    for line in content.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)

    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()

    # Get all sections
    problem = sections.get('Problem', '')
    approach = sections.get('Approach', '')
    current_state = sections.get('Current State', '')
    uncertainties = sections.get('Uncertainties', '')
    next_steps = sections.get('Next Steps', '')
    sources_section = sections.get('Sources', '')

    # Extract enrichment sources from Sources section
    enrichment_sources = parse_sources_from_text(sources_section)

    # Also extract any inline links from Current State (often has org links)
    inline_sources = parse_sources_from_text(current_state)

    # Deduplicate by URL
    seen_urls = set()
    all_external = []
    for s in enrichment_sources + inline_sources:
        if s['url'] not in seen_urls:
            seen_urls.add(s['url'])
            all_external.append(s)

    # Combine: Peregrine proposals (list of lists) + external enrichment sources
    all_sources = peregrine_sources + all_external

    return {
        'filename': filepath.stem,
        'title': title,
        'tag': tag,
        'status': status,
        'problem': problem,
        'approach': approach,
        'currentState': current_state,
        'uncertainties': uncertainties,
        'nextSteps': next_steps,
        'sources': all_sources,
    }


def main():
    if not SOURCE_DIR.exists():
        print(f"Source directory not found: {SOURCE_DIR}")
        return

    interventions = []
    for filepath in sorted(SOURCE_DIR.glob('*.md')):
        try:
            intervention = parse_intervention(filepath)
            interventions.append(intervention)
        except Exception as e:
            print(f"Error parsing {filepath.name}: {e}")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(interventions, f, indent=2)

    print(f"Generated {len(interventions)} projects to {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
