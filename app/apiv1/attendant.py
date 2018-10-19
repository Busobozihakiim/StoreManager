"""this will cater for attendants"""
from flask import Flask, request, jsonify
from tempdata.datamodal import TempStore

STORE_MANAGER = Flask(__name__)

@STORE_MANAGER.route('/api/v1/sales', methods=["POST"])
def create_sale():
    """Function to create a sale """
    captured_data = request.get_json(force=True)
    one_sale = TempStore()
    one_sale.add_sale(captured_data['attendant_name'], captured_data['pdct_name'],
                      captured_data['pdct_quantity'], captured_data['pdct_cost'])
    return jsonify("Sale record added succesfully"), 201

if __name__ == "__main__":
    STORE_MANAGER.run(debug=True)
