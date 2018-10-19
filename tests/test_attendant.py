"""UNIT TESTING"""
import unittest
import requests
import json

DATA = {"attendant_name":"Mary", "pdct_name":"flash", "pdct_quantity":"2", "pdct_cost":"5000"}

class Testattendant(unittest.TestCase):
    """Class for unit tests"""

    def test_create_sale(self):
        """test the creation of a sale record"""
        self.response = requests.post('http://127.0.0.1:5000/api/v1/sales', json.dumps(DATA))
        self.assertEqual(self.response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
