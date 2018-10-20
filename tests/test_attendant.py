"""UNIT TESTING"""
import unittest
import requests

class Testattendant(unittest.TestCase):
    """Class for unit tests"""

    def test_get_single_sale(self):
        """test the return of a single sale based on id"""
        self.response = requests.get('http://127.0.0.1:5000/api/v1/sales/{}'.format(2))
        self.assertEqual(self.response.status_code, 200)

if __name__ == "__main__":
    unittest.main()