import unittest
import os
import json

class TestRedOpsEngine(unittest.TestCase):
    def test_payload_db_exists(self):
        db_path = os.path.join(os.path.dirname(__file__), '../db/payloads.json')
        self.assertTrue(os.path.exists(db_path), "Payloads database missing.")
        with open(db_path, 'r') as f:
            data = json.load(f)
            self.assertGreater(len(data), 1000, "Database should contain 1000+ entries.")

if __name__ == '__main__':
    unittest.main()
