"""POST-PRODUCT ENDPOINT"""
from flask import Flask, request, jsonify
from tempdata.datamodal import TempStore

STORE_MANAGER = Flask(__name__)
@STORE_MANAGER.route('/api/v1/products', methods=["POST"])
def create_product():
    """Function to create a product """
    captured_data = request.get_json(force=True)
    one_product = TempStore()
    one_product.add_pdct(captured_data['pdct_name'], captured_data['pdct_quantity'],
                         captured_data['pdct_cost'])
    return jsonify("Product added succesfully"), 201
    
if __name__ == "__main__":
    STORE_MANAGER.run(debug=True)
    