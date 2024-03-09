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

    
    def test_do_update_missing_class_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_update")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_update_invalid_class_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_update InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update_missing_instance_id(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_update BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_update_instance_not_found(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_update BaseModel 1234")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_update_missing_attribute_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_update BaseModel 1234")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_do_update_missing_value(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_update BaseModel 1234 name")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    # Add more test cases for valid updates...

    def test_do_count_missing_class_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_count")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_count_invalid_class_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_count InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_count_with_instances(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("do_count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "2")

    def test_do_count_with_no_instances(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "0")

    
    def test_do_destroy_missing_class_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_destroy")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_destroy_invalid_class_name(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_destroy InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_destroy_missing_instance_id(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_destroy BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_instance_found(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"do_destroy BaseModel {instance_id}")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(f"BaseModel.{instance_id}", self.console.all_objects)

    def test_do_destroy_instance_not_found(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            self.console.onecmd("do_destroy BaseModel 1234")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
if __name__ == '__main__':
    unittest.main()