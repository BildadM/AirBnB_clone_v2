import unittest
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.user = User()
        self.user.id = 123
        self.user.name = "John Doe"

    def test_new(self):
        self.file_storage.new(self.user)
        self.assertTrue("User.123" in self.file_storage._FileStorage__objects)

    def test_all(self):
        self.file_storage.new(self.user)
        all_objects = self.file_storage.all(User)
        self.assertEqual(len(all_objects), 1)
        self.assertTrue("User.123" in all_objects)

    def test_save_and_reload(self):
        """ Creating a mock dictionary to simulate existing data"""
        self.file_storage._FileStorage__objects = {"User.123": self.user}
        
        """Creating a mock file object"""
        mock_file = MagicMock()
        
        """Patching the open function to return the mock file object"""
        with unittest.mock.patch('builtins.open', unittest.mock.mock_open(), create=True) as mock_open:
            mock_open.return_value = mock_file
            
            """Call the save method"""
            self.file_storage.save()
            
            """Verify that json.dump was called with the correct arguments"""
            mock_file.write.assert_called_once_with('{"User.123": {"__class__": "User", "id": 123, "name": "John Doe"}}')
        
        """Reset file storage to empty and reload from the saved file"""
        self.file_storage._FileStorage__objects = {}
        self.file_storage.reload()
        
        """Verify that the reloaded object is the same as the original object"""
        self.assertEqual(self.file_storage.all(), {"User.123": self.user})

    def test_delete(self):
        self.file_storage.new(self.user)
        self.file_storage.delete(self.user)
        self.assertTrue("User.123" not in self.file_storage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()
