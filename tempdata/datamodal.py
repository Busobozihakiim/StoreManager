#temporary data store
products = []
sales = []

class tempStore:
    
    def __init__(self):
        pass

    def add_pdct(self, pdct_name, pdct_quantity, pdct_cost):
        product = {
            'pdct_id': len(products) + 1,
            'pdct_name' :pdct_name,
            'pdct_quantity' :pdct_quantity,
            'pdct_cost' :pdct_cost
        }
        products.append(product)
        return products