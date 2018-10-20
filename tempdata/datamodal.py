"""temporary data store"""
PRODUCTS = []

class TempStore:
    """Temp data store"""

    def __init__(self):
        pass

    def add_pdct(self, pdct_name, pdct_quantity, pdct_cost):
        """function to add a products"""
        product = {
            'pdct_id': len(PRODUCTS) + 1,
            'pdct_name' :pdct_name,
            'pdct_quantity' :pdct_quantity,
            'pdct_cost' :pdct_cost
        }
        PRODUCTS.append(product)
        return PRODUCTS
