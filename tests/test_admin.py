"""UNIT TESTING"""
import unittest
import requests

class Testadmin(unittest.TestCase):
    """Class for unit tests"""

    def test_get_all_products(self):
        """test the return of all products"""
        self.response = requests.get('http://127.0.0.1:5000/api/v1/products')
        self.assertEqual(self.response.status_code, 200)

    def test_get_single_product(self):
        """test the return of a single product based on id"""
        self.response = requests.get('http://127.0.0.1:5000/api/v1/products/{}'.format(2))
        self.assertEqual(self.response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
