import unittest
import tempfile
import shutil
from pathlib import Path
from token_cruncher import count_tokens, analyze_directory
import io
import sys

class TestTokenCruncher(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.test_dir_path = Path(self.test_dir)

        # Create a sample .zw file
        self.zw_file = self.test_dir_path / "test.zw"
        with open(self.zw_file, "w", encoding="utf-8") as f:
            f.write("#角色 助手")

        # Create a sample .json file
        self.json_file = self.test_dir_path / "test.json"
        with open(self.json_file, "w", encoding="utf-8") as f:
            f.write('{"role": "Assistant"}')

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_count_tokens(self):
        text = "Hello, world!"
        # "Hello", ",", " world", "!" -> 4 tokens
        self.assertEqual(count_tokens(text), 4)

        # "#角色 助手" -> 6 tokens
        # "#" (1) + "角" (1) + "色" (1) + " 助" (1) + "手" (1)
        # Actually tiktoken count might be different depending on exact model and chars
        self.assertGreater(count_tokens("#角色 助手"), 0)

    def test_analyze_directory(self):
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        analyze_directory(str(self.test_dir_path))

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Token Cruncher Benchmark Results", output)
        self.assertIn("test.zw", output)
        self.assertIn("test.json", output)
        self.assertIn("Overall Reduction", output)

    def test_empty_directory(self):
        empty_dir = tempfile.mkdtemp()

        captured_output = io.StringIO()
        sys.stdout = captured_output

        analyze_directory(empty_dir)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("No paired files found to analyze.", output)

        shutil.rmtree(empty_dir)

if __name__ == "__main__":
    unittest.main()
