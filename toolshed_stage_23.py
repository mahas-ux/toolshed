# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ToolShed
def add_tag(item, tag_name):
    if tag_name not in item["tags"]:
        item["tags"].append(tag_name)
    return item

def remove_tag(item, tag_name):
    if tag_name in item["tags"]:
        item["tags"].remove(tag_name)
    return item

def tag_summary(items, tag_name):
    return [i for i in items if tag_name in i["tags"]]
