import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review_data = {
            "text": "This is a test review",
            "place_id": "123",
            "user_id": "456"
        }
        self.review = Review(**self.review_data)

    def test_attributes(self):
        self.assertEqual(self.review.text, self.review_data["text"])
        self.assertEqual(self.review.place_id, self.review_data["place_id"])
        self.assertEqual(self.review.user_id, self.review_data["user_id"])

if __name__ == '__main__':
    unittest.main()
