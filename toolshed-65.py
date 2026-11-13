# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ToolShed
import re


def merge_imports(existing_lines, new_lines):
    existing_imports = parse_imports(existing_lines)
    new_imports = parse_imports(new_lines)

    merged = list(existing_imports)
    for imp in new_imports:
        if not any(existing == imp for existing in merged):
            merged.append(imp)

    merged_lines = []
    for imp in merged:
        if imp.startswith("import "):
            if imp.startswith("import ") and imp.endswith(","):
                merged_lines.append(imp.rstrip(",") + ",")
            else:
                merged_lines.append(imp)
        else:
            merged_lines.append(imp)

    return merged_lines


def parse_imports(lines):
    imports = []
    for line in lines:
        line = line.strip()
        if line.startswith("import ") or line.startswith("from "):
            imports.append(line)
    return imports


def consolidate_imports(lines):
    all_imports = []
    for line in lines:
        line = line.strip()
        if line.startswith("import "):
            all_imports.append(line)
        elif line.startswith("from "):
            all_imports.append(line)

    deduplicated = []
    seen = set()
    for import_line in all_imports:
        if import_line not in seen:
            seen.add(import_line)
            deduplicated.append(import_line)

    return deduplicated
