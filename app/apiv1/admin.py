#this is for the admin
from flask import Flask, request, jsonify
from tempdata.datamodal import *

storeManager = Flask(__name__)

@storeManager.route('/api/v1/products', methods=['GET'])
def getAllProducts():
    """Return all available products"""
    if len(products) == 0:
        return jsonify("No products available"),200
    else:
        return jsonify(products), 200

@storeManager.route('/api/v1/products/<int:pdct_id>', methods=['GET'])
def getSingleProduct(pdct_id):
    """This will return a single product based on its id"""
    if len(products) != 0:
        oneproduct = [ oneproduct for oneproduct in products if oneproduct['pdct_id'] == pdct_id]
        return jsonify({'oneproduct': oneproduct[0]}), 200
    else:
        return "No products available",200

@storeManager.route('/api/v1/products', methods=["POST"])
def createProduct():
    """Function to create a product """ 
    captured_data = request.get_json(force=True) 
    oneProduct = tempStore()
    oneProduct.add_pdct(captured_data['pdct_name'], captured_data['pdct_quantity'], captured_data['pdct_cost']) 
    return "Product added succesfully",201
    
if __name__ == "__main__":
    storeManager.run(debug=True)