import unittest
from unittest.mock import patch
import io
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_create(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith(""))

    def test_show(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel 1234-5678")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("** no instance found **"))

   

if __name__ == '__main__':
    unittest.main()