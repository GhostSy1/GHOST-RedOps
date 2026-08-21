import importlib.util
import unittest
from pathlib import Path


class RedTeamToolTests(unittest.TestCase):
    def test_cli_execution_runs_cleanly(self):
        module_path = Path(__file__).parents[1] / "main.py"
        spec = importlib.util.spec_from_file_location("main_module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertTrue(hasattr(module, "run"))


if __name__ == "__main__":
    unittest.main()
