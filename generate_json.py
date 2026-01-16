#!/usr/bin/env python3
"""Generate interventions.json from markdown files."""
import json
import re
from pathlib import Path

def parse_bullet_list(text):
    """Parse markdown bullet list into array of strings."""
    if not text:
        return []
    lines = []
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('- '):
            lines.append(line[2:].strip())
        elif line.startswith('* '):
            lines.append(line[2:].strip())
    return lines if lines else [text] if text else []

def parse_sources(text):
    """Parse sources section into array of {text, url} objects."""
    if not text:
        return []
    sources = []
    # Match markdown links: [text](url)
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(pattern, text):
        sources.append({
            'text': match.group(1),
            'url': match.group(2)
        })
    return sources

def parse_intervention(filepath):
    """Parse a markdown intervention file into structured data."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract title (first H1)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem

    # Extract tag
    tag_match = re.search(r'\*\*Tag\*\*:\s*(\w+)', content)
    tag = tag_match.group(1) if tag_match else "Unknown"

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

    # Parse whyItMatters as bullet list
    why_it_matters_raw = sections.get('Why it matters', '')
    why_it_matters = parse_bullet_list(why_it_matters_raw)

    return {
        'filename': filepath.stem,
        'title': title,
        'tag': tag,
        'whatItIs': sections.get('What it is', ''),
        'whyItMatters': why_it_matters,
        'currentState': sections.get('Current state', ''),
        'whoWorking': sections.get("Who's working on it", ''),
        'sources': parse_sources(sections.get('Sources', ''))
    }

def main():
    interventions_dir = Path('/Users/jonahweinbaum/Desktop/Claude Code/projects/ListofListofLists/interventions-new')
    output_file = Path('/Users/jonahweinbaum/Desktop/Claude Code/projects/ListofListofLists/data/interventions.json')

    interventions = []
    for filepath in sorted(interventions_dir.glob('*.md')):
        try:
            intervention = parse_intervention(filepath)
            interventions.append(intervention)
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")

    with open(output_file, 'w') as f:
        json.dump(interventions, f, indent=2)

    print(f"Generated {len(interventions)} interventions to {output_file}")

if __name__ == '__main__':
    main()
