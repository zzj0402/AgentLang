import unittest
import os
import tempfile
import shutil
from pathlib import Path
from embedding_benchmark import calculate_similarity, analyze_directory
import io
import sys

# Mock for SentenceTransformer
class MockModel:
    def encode(self, texts):
        if len(texts) == 2 and texts[0] == texts[1]:
            return [[1.0, 0.0], [1.0, 0.0]]
        return [[1.0, 0.0], [0.0, 1.0]]

class TestEmbeddingBenchmark(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_dir_path = Path(self.test_dir)

        self.zw_file = self.test_dir_path / "test.zw"
        with open(self.zw_file, "w", encoding="utf-8") as f:
            f.write("Hello world")

        self.json_file = self.test_dir_path / "test.json"
        with open(self.json_file, "w", encoding="utf-8") as f:
            f.write("Hello world")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_calculate_similarity(self):
        model = MockModel()

        # Identical texts
        sim_identical = calculate_similarity("hello", "hello", model)
        self.assertAlmostEqual(sim_identical, 1.0)

        # Different texts
        sim_different = calculate_similarity("hello", "world", model)
        self.assertAlmostEqual(sim_different, 0.0)

        # Empty text handling
        sim_empty = calculate_similarity("", "hello", model)
        self.assertEqual(sim_empty, 0.0)

    def test_analyze_directory(self):
        # We patch SentenceTransformer to return our MockModel to avoid downloading weights during tests
        import embedding_benchmark
        original_SentenceTransformer = embedding_benchmark.SentenceTransformer

        def mock_SentenceTransformer(model_name):
            return MockModel()

        embedding_benchmark.SentenceTransformer = mock_SentenceTransformer

        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Pass a list of models instead of a single string
        embedding_benchmark.analyze_directory(str(self.test_dir_path), ["dummy-model"])

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Restore original
        embedding_benchmark.SentenceTransformer = original_SentenceTransformer

        self.assertIn("Embedding Similarity Benchmark Results", output)
        self.assertIn("test.zw", output)
        self.assertIn("test.json", output)
        self.assertIn("Average Cosine Similarity", output)

if __name__ == "__main__":
    unittest.main()
