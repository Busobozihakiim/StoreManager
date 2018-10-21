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

@STORE_MANAGER.route('/api/v1/products/<int:pdct_id>', methods=['GET'])
def get_single_product(pdct_id):
    """This will return a single product based on its id"""
    if PRODUCTS:
        oneproduct = [oneproduct for oneproduct in PRODUCTS if oneproduct['pdct_id'] == pdct_id]
        return jsonify({'oneproduct': oneproduct[0]}), 200
    return jsonify("No products available"), 200


if __name__ == "__main__":
    STORE_MANAGER.run(debug=True)
