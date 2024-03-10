import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        self.storage._FileStorage__objects = {}
        if self.storage._FileStorage__file_path:
            with open(self.storage._FileStorage__file_path, "w") as f:
                f.write("")

    
if __name__ == "__main__":
    unittest.main()