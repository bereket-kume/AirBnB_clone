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

   
    def test_do_all(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("create Place")
            self.console.onecmd("create Amenity")
            self.console.onecmd("create Review")
            self.console.onecmd("do_all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertIn("User", output)
            self.assertIn("Place", output)
            self.assertIn("Amenity", output)
            self.assertIn("Review", output)

    def test_do_all_with_class_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("create Place")
            self.console.onecmd("create Amenity")
            self.console.onecmd("create Review")
            self.console.onecmd("do_all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertNotIn("User", output)
            self.assertNotIn("Place", output)
            self.assertNotIn("Amenity", output)
            self.assertNotIn("Review", output)

    def test_do_all_with_invalid_class_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_all InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    
    
if __name__ == '__main__':
    unittest.main()