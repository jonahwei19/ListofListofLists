#!/usr/bin/env python3
"""Generate interventions.json from markdown files."""
import json
import os
import re
from pathlib import Path

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
    
    return {
        'id': filepath.stem,
        'title': title,
        'tag': tag,
        'what_it_is': sections.get('What it is', ''),
        'why_it_matters': sections.get('Why it matters', ''),
        'current_state': sections.get('Current state', ''),
        'whos_working_on_it': sections.get("Who's working on it", ''),
        'sources': sections.get('Sources', ''),
        'file': str(filepath.relative_to(filepath.parent.parent))
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
