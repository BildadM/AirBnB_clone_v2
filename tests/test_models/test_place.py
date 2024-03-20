import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review
from os import getenv


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place_data = {
            "city_id": "123",
            "user_id": "456",
            "name": "Test Place",
            "description": "This is a test place",
            "number_rooms": 2,
            "number_bathrooms": 2,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 40.7128,
            "longitude": -74.0060,
        }
        self.place = Place(**self.place_data)

    def test_attributes(self):
        self.assertEqual(self.place.city_id, self.place_data["city_id"])
        self.assertEqual(self.place.user_id, self.place_data["user_id"])
        self.assertEqual(self.place.name, self.place_data["name"])
        self.assertEqual(self.place.description, self.place_data["description"])
        self.assertEqual(self.place.number_rooms, self.place_data["number_rooms"])
        self.assertEqual(self.place.number_bathrooms, self.place_data["number_bathrooms"])
        self.assertEqual(self.place.max_guest, self.place_data["max_guest"])
        self.assertEqual(self.place.price_by_night, self.place_data["price_by_night"])
        self.assertEqual(self.place.latitude, self.place_data["latitude"])
        self.assertEqual(self.place.longitude, self.place_data["longitude"])

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Only relevant for database storage")
    def test_relationships(self):
        """Testing relationship with City"""
        self.assertTrue(hasattr(self.place, 'city'))
        self.assertIsInstance(self.place.city, City)

        """Testing relationship with User"""
        self.assertTrue(hasattr(self.place, 'user'))
        self.assertIsInstance(self.place.user, User)

        """Testing relationship with Review"""
        self.assertTrue(hasattr(self.place, 'reviews'))
        self.assertEqual(self.place.reviews, [])

        """Testing relationship with Amenity"""
        self.assertTrue(hasattr(self.place, 'amenities'))
        self.assertEqual(self.place.amenities, [])

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Only relevant for database storage")
    def test_amenities_relationship(self):
        """Create a new amenity and associate it with the place"""
        amenity = Amenity(name="WiFi")
        self.place.amenities.append(amenity)
        self.assertIn(amenity, self.place.amenities)


if __name__ == '__main__':
    unittest.main()
