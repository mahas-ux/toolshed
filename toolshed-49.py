# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ToolShed
import unittest
from toolshed.models import Tool
from toolshed.db import ToolDB


class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.db = ToolDB(":memory:")

    def tearDown(self):
        self.db.close()

    def test_delete_nonexistent_tool(self):
        self.db.add({"name": "drill", "type": "power", "status": "in_shed"})
        result = self.db.delete_tool("nonexistent")
        self.assertFalse(result)
        tools = self.db.get_all()
        self.assertEqual(len(tools), 1)
        self.assertEqual(tools[0]["name"], "drill")

    def test_update_nonexistent_tool(self):
        result = self.db.update_tool("missing", status="borrowed")
        self.assertFalse(result)
        tools = self.db.get_all()
        self.assertEqual(len(tools), 0)

    def test_delete_all_tools(self):
        self.db.add({"name": "screwdriver", "type": "manual", "status": "in_shed"})
        self.db.add({"name": "tape", "type": "manual", "status": "in_shed"})
        result = self.db.delete_all()
        self.assertTrue(result)
        tools = self.db.get_all()
        self.assertEqual(len(tools), 0)

    def test_update_status_with_invalid_enum(self):
        self.db.add({"name": "hammer", "type": "manual", "status": "in_shed"})
        result = self.db.update_tool("hammer", status="invalid_status")
        self.assertFalse(result)
        tools = self.db.get_all()
        self.assertEqual(len(tools), 1)
        self.assertEqual(tools[0]["status"], "in_shed")


if __name__ == "__main__":
    unittest.main()
