import unittest
from app import app


class TestHomeRoute(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_hello_message(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_data(as_text=True),
            "Hello from my DevOps project!"
        )


if __name__ == "__main__":
    unittest.main()
