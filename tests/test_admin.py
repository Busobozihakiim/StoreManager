"""UNIT TESTING"""
import unittest
import json
import requests

DATA = {"attendant_name":"Mary", "pdct_name":"flash", "pdct_quantity":"2", "pdct_cost":"5000"}
SALES = {'sale_id': 1, 'attendant_name':'jane', 'pdct_name' :'drive', 'pdct_quantity' :3,
          'pdct_cost' : 500, 'pdct_total':1500}


class Testadmin(unittest.TestCase):
    """Class for unit tests"""

    def test_get_all_products(self):
        """test the return of all products"""
        self.response = requests.get('http://127.0.0.1:5000/api/v1/products')
        self.assertEqual(self.response.status_code, 200)

    def test_get_all_sales(self):
        """test the return of all sales"""
        self.response = requests.get('http://127.0.0.1:5000/api/v1/sales')
        self.assertEqual(self.response.status_code, 200)
    
    def test_get_single_product(self):
        """test the return of a single product based on id"""
        try:
            if DATA:
                self.response = requests.get('http://127.0.0.1:5000/api/v1/products/{}'.format(8))
                self.assertEqual(self.response.status_code, 200)
        except IndexError:
            self.assertEqual(self.response.status_code, 400)

    def test_get_single_sale(self):
        """test the return of a single sale based on id"""
        try:
            self.response = requests.get('http://127.0.0.1:5000/api/v1/sales/{}'.format(2))
            self.assertEqual(self.response.status_code, 200)
        except IndexError:
            self.assertEqual(self.response.status_code, 400)

    def test_create_product(self):
        """test the creation of a product"""
        try:
            self.response = requests.post('http://127.0.0.1:5000/api/v1/products', json.dumps(DATA))
            self.assertEqual(self.response.status_code, 201)
        except KeyError:
            self.assertEqual(self.response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
