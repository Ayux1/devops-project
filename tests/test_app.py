
import unittest
from app import app


class TestHomeRoute(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_portfolio(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.content_type)
        self.assertIn("Ayush Asthana", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
