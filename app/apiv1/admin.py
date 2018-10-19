"""this is for the admin"""
from flask import Flask, jsonify
from tempdata.datamodal import PRODUCTS

STORE_MANAGER = Flask(__name__)

@STORE_MANAGER.route('/api/v1/products', methods=['GET'])
def get_all_products():
    """Return all available products"""
    if not PRODUCTS:
        return jsonify("No products available"), 200
    return jsonify(PRODUCTS), 200

if __name__ == "__main__":
    STORE_MANAGER.run(debug=True)
