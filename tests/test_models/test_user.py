import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe"
        }
        self.user = User(**self.user_data)

    def test_attributes(self):
        self.assertEqual(self.user.email, self.user_data["email"])
        self.assertEqual(self.user.password, self.user_data["password"])
        self.assertEqual(self.user.first_name, self.user_data["first_name"])
        self.assertEqual(self.user.last_name, self.user_data["last_name"])

    def test_relationship_places(self):
        self.assertTrue(hasattr(self.user, 'places'))
        self.assertEqual(self.user.places, [])

    def test_relationship_reviews(self):
        self.assertTrue(hasattr(self.user, 'reviews'))
        self.assertEqual(self.user.reviews, [])

if __name__ == '__main__':
    unittest.main()
