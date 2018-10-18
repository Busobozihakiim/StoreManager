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

if __name__ == "__main__":
    storeManager.run(debug=True)