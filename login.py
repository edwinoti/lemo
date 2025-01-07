import unittest
import requests

# Define the base URL for the API
BASE_URL = "https://your-api-url.com/login"  # Replace with actual API URL

# Define the test case class
class TestLoginAPI(unittest.TestCase):

    # Test case for valid credentials
    def test_valid_login(self):
        # Define valid credentials
        valid_data = {
            "username": "validUser",
            "password": "validPassword123"
        }

        # Send POST request
        response = requests.post(BASE_URL, data=valid_data)

        # Check the response status code
        self.assertEqual(response.status_code, 200, "Expected status code to be 200 OK")
        
        # Check if token is returned in response JSON
        response_json = response.json()
        self.assertIn("token", response_json, "Token not found in response")

    # Test case for invalid credentials
    def test_invalid_login(self):
        # Define invalid credentials
        invalid_data = {
            "username": "invalidUser",
            "password": "wrongPassword"
        }

        # Send POST request
        response = requests.post(BASE_URL, data=invalid_data)

        # Check the response status code
        self.assertEqual(response.status_code, 401, "Expected status code to be 401 Unauthorized")
        
        # Check if error message is returned in response JSON
        response_json = response.json()
        self.assertIn("error", response_json, "Error message not found in response")
        self.assertEqual(response_json["error"], "Invalid credentials", "Unexpected error message")

# Run the tests
if __name__ == "__main__":
    unittest.main()

