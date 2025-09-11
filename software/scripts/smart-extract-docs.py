#!/usr/bin/env python3
"""
Smart Documentation Extractor for UNIT Touch Capacitive Sensor
Extracts content from README files with intelligent processing to avoid duplication.
"""

import os
import re
import json
from pathlib import Path
import subprocess

def read_file_content(file_path):
    """Read content from a file with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return ""

def write_file_content(file_path, content):
    """Write content to a file with proper directory creation."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")
        return False

def fix_image_sizes(content):
    """Add size constraints to images for better display."""
    # Pattern to match ![alt](path) or <img> tags
    img_patterns = [
        (r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" style="max-width: 80%; height: auto; display: block; margin: 1em auto;">'),
        (r'<img\s+([^>]*?)src="([^"]+)"([^>]*?)>', r'<img \1src="\2"\3 style="max-width: 80%; height: auto; display: block; margin: 1em auto;">')
    ]
    
    for pattern, replacement in img_patterns:
        content = re.sub(pattern, replacement, content)
    
    return content

def preserve_external_links(content):
    """Preserve external links and fix internal ones."""
    # Fix relative paths in links
    content = re.sub(r'\]\(\.\./', '](../', content)
    content = re.sub(r'\]\(\./', '](', content)
    return content

def extract_content_without_main_title(content):
    """Extract content without the main title to avoid duplication."""
    lines = content.split('\n')
    filtered_lines = []
    skip_next_empty = False
    title_found = False
    
    for i, line in enumerate(lines):
        # Skip main title (first # header)
        if not title_found and line.strip().startswith('#') and not line.strip().startswith('##'):
            title_found = True
            skip_next_empty = True
            continue
        
        # Skip empty line after title
        if skip_next_empty and line.strip() == '':
            skip_next_empty = False
            continue
        
        filtered_lines.append(line)
    
    return '\n'.join(filtered_lines)

def process_hardware_readme():
    """Process hardware README and create mdBook sections."""
    hardware_readme = Path("hardware/README.md")
    
    if not hardware_readme.exists():
        print("Warning: hardware/README.md not found")
        return {}
    
    content = read_file_content(hardware_readme)
    if not content:
        return {}
    
    # Extract content without main title
    processed_content = extract_content_without_main_title(content)
    processed_content = fix_image_sizes(processed_content)
    processed_content = preserve_external_links(processed_content)
    
    # Create overview file
    overview_content = f"""# Hardware Overview

{processed_content}
"""
    
    return {
        "hardware/overview.md": overview_content,
    }

def process_software_content():
    """Process software README and examples."""
    software_readme = Path("software/README.md")
    
    if not software_readme.exists():
        print("Warning: software/README.md not found")
        return {}
    
    content = read_file_content(software_readme)
    if not content:
        return {}
    
    # Extract content without main title
    processed_content = extract_content_without_main_title(content)
    processed_content = fix_image_sizes(processed_content)
    processed_content = preserve_external_links(processed_content)
    
    # Split into getting started and examples sections
    sections = processed_content.split('##')
    
    getting_started_content = "# Getting Started\n\n"
    examples_content = "# Examples\n\n"
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        if any(keyword in section.lower() for keyword in ['example', 'código', 'code']):
            examples_content += f"## {section}\n\n"
        else:
            getting_started_content += f"## {section}\n\n"
    
    return {
        "software/getting-started.md": getting_started_content,
        "software/examples.md": examples_content,
    }

def process_license():
    """Process LICENSE file."""
    license_file = Path("LICENSE")
    
    if not license_file.exists():
        print("Warning: LICENSE file not found")
        return {}
    
    content = read_file_content(license_file)
    if not content:
        return {}
    
    license_content = f"""# License

```
{content}
```
"""
    
    return {
        "license.md": license_content
    }

def create_summary():
    """Create the SUMMARY.md file for mdBook navigation."""
    return """# Summary

[Introduction](./introduction.md)

# Hardware
- [Overview](./hardware/overview.md)

# Software  
- [Getting Started](./software/getting-started.md)
- [Examples](./software/examples.md)

---

[License](./license.md)
"""

def create_introduction():
    """Create introduction from main README without title duplication."""
    main_readme = Path("README.md")
    
    if not main_readme.exists():
        return "# Introduction\n\nWelcome to UNIT Touch Capacitive Sensor documentation."
    
    content = read_file_content(main_readme)
    if not content:
        return "# Introduction\n\nWelcome to UNIT Touch Capacitive Sensor documentation."
    
    # Extract content without main title
    processed_content = extract_content_without_main_title(content)
    processed_content = fix_image_sizes(processed_content)
    processed_content = preserve_external_links(processed_content)
    
    return f"""# Introduction

{processed_content}
"""

def copy_resources():
    """Copy resource files to book directory."""
    resources_copied = []
    
    # Define resource directories to copy
    resource_dirs = [
        ("hardware/resources", "hardware/resources"),
        ("hardware/resources", "resources"),  # Also copy to root resources for compatibility
    ]
    
    for src_dir, dest_dir in resource_dirs:
        src_path = Path(src_dir)
        if src_path.exists():
            dest_path = Path("software/book/src") / dest_dir
            os.makedirs(dest_path, exist_ok=True)
            
            for file_path in src_path.rglob("*"):
                if file_path.is_file():
                    relative_path = file_path.relative_to(src_path)
                    dest_file = dest_path / relative_path
                    os.makedirs(dest_file.parent, exist_ok=True)
                    
                    try:
                        import shutil
                        shutil.copy2(file_path, dest_file)
                        resources_copied.append(str(dest_file))
                    except Exception as e:
                        print(f"Warning: Could not copy {file_path}: {e}")
    
    return resources_copied

def main():
    """Main extraction process."""
    print("🚀 Starting smart content extraction...")
    
    # Create book source directory
    book_src = Path("software/book/src")
    book_src.mkdir(parents=True, exist_ok=True)
    
    # Process all content
    all_files = {}
    
    # Create introduction
    all_files["introduction.md"] = create_introduction()
    
    # Process hardware
    all_files.update(process_hardware_readme())
    
    # Process software
    all_files.update(process_software_content())
    
    # Process license
    all_files.update(process_license())
    
    # Create SUMMARY.md
    all_files["SUMMARY.md"] = create_summary()
    
    # Write all files
    extraction_report = {
        "files_created": [],
        "files_failed": [],
        "resources_copied": []
    }
    
    for relative_path, content in all_files.items():
        file_path = book_src / relative_path
        if write_file_content(file_path, content):
            extraction_report["files_created"].append(str(relative_path))
        else:
            extraction_report["files_failed"].append(str(relative_path))
    
    # Copy resources
    extraction_report["resources_copied"] = copy_resources()
    
    # Write extraction report
    report_path = Path("software/book/extraction_report.json")
    with open(report_path, 'w') as f:
        json.dump(extraction_report, f, indent=2)
    
    print(f"✅ Extraction complete!")
    print(f"📝 Created {len(extraction_report['files_created'])} files")
    print(f"📁 Copied {len(extraction_report['resources_copied'])} resources")
    
    if extraction_report['files_failed']:
        print(f"⚠️  Failed to create {len(extraction_report['files_failed'])} files")
    
    return len(extraction_report['files_failed']) == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
