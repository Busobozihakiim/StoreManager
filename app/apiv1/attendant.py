#this will cater for attendants 
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

@storeManager.route('/api/v1/sales', methods=["POST"])
def createSale():
    """Function to create a sale """ 
    captured_data = request.get_json(force=True) 
    oneSale = tempStore()
    oneSale.add_sale(captured_data['attendant_name'],captured_data['pdct_name'], captured_data['pdct_quantity'], captured_data['pdct_cost']) 
    return "Sale record added succesfully",201

@storeManager.route('/api/v1/sales/<int:sale_id>',methods=['GET'])
def getSaleById(sale_id):
    """Returns a single sale based on a sale id"""
    if len(sales) != 0:
        onesale = [ onesale for onesale in sales if onesale['sale_id'] == sale_id]
        return jsonify({'onesale': onesale[0]}), 200
    else:
        return "No sales available Yet",200

if __name__ == "__main__":
    storeManager.run(debug=True)