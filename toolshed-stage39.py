# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ToolShed
def repair_simple_integrity(connection):
    """Fix common data integrity issues in the ToolShed database.
    
    This function handles:
    1. Removing duplicate entries in the tools table
    2. Fixing any non-unique values in the location table
    3. Ensuring all loans have valid tool references
    """
    cursor = connection.cursor()
    
    # Fix duplicate tools by keeping the most recent entry
    cursor.execute("""
        DELETE FROM tools 
        WHERE id NOT IN (
            SELECT MAX(id) FROM tools 
            GROUP BY name, condition
        )
    """)
    
    # Fix duplicate locations by keeping the most recent entry
    cursor.execute("""
        DELETE FROM locations 
        WHERE id NOT IN (
            SELECT MAX(id) FROM locations 
            GROUP BY name
        )
    """)
    
    # Remove loans that reference non-existent tools
    cursor.execute("""
        DELETE FROM loans 
        WHERE tool_id NOT IN (SELECT id FROM tools)
    """)
    
    connection.commit()
    print("Data integrity issues have been repaired.")
