"""this is for the admin"""
from flask import Flask, jsonify, request
from tempdata.datamodal import PRODUCTS, SALES, TempStore

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
    try:
        if PRODUCTS:
            oneproduct = [oneproduct for oneproduct in PRODUCTS if oneproduct['pdct_id'] == pdct_id]
            return jsonify({'oneproduct': oneproduct[0]}), 200
        return jsonify("No products available"), 200
    except IndexError:
        return jsonify("the product with id {} doesnt exist".format(pdct_id)), 400

@STORE_MANAGER.route('/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_sale_by_id(sale_id):
    """Returns a single sale based on a sale id"""
    try:
        if SALES:
            onesale = [onesale for onesale in SALES if onesale['sale_id'] == sale_id]
            return jsonify({'onesale': onesale[0]}), 200
        return jsonify("No sales available Yet"), 200
    except IndexError:
        return jsonify("the sale with id {} doesnt exist".format(sale_id)), 400

@STORE_MANAGER.route('/api/v1/products', methods=["POST"])
def create_product():
    """Function to create a product """
    try:
        captured_data = request.get_json(force=True)
        one_product = TempStore()
        one_product.add_pdct(captured_data['pdct_name'], captured_data['pdct_quantity'],
                             captured_data['pdct_cost'])
        return jsonify("Product added succesfully"), 201
    except KeyError:
        return jsonify("input should be in this format {'pdct_name':'Flask Disk','pdct_quantity':'2','pdct_cost':'5000'}"), 400

@STORE_MANAGER.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    """Returns all Attendant's sales"""
    if not SALES:
        return jsonify("No sales made yet"), 200
    return jsonify(SALES), 200

if __name__ == "__main__":
    STORE_MANAGER.run(debug=True)
    