# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ToolShed
def bulk_delete_tools(confirmation_flag):
    if not confirmation_flag:
        return 0
    deleted = 0
    for tool in tools_list:
        del tools_list[tools_list.index(tool)]
        deleted += 1
    return deleted
