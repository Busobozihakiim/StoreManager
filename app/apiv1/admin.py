"""this is for the admin"""
from flask import Flask, jsonify
from tempdata.datamodal import SALES

STORE_MANAGER = Flask(__name__)

@STORE_MANAGER.route('/api/v1/sales/<int:sale_id>', methods=['GET'])

def get_sale_by_id(sale_id):
    """Returns a single sale based on a sale id"""
    if SALES:
        onesale = [onesale for onesale in SALES if onesale['sale_id'] == sale_id]
        return jsonify({'onesale': onesale[0]}), 200
    return jsonify("No sales available Yet"), 200

if __name__ == "__main__":
    STORE_MANAGER.run(debug=True)
