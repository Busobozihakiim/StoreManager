"""temporary data store"""
SALES = []

class TempStore:
    """temp store class"""

    def __init__(self):
        pass

    def add_sale(self, attendant_name, pdct_name, pdct_quantity, pdct_cost):
        """method to create a sales record"""
        sale = {
            'sale_id': len(SALES) + 1,
            'attendant_name':attendant_name,
            'pdct_name' :pdct_name,
            'pdct_quantity' :pdct_quantity,
            'pdct_cost' :pdct_cost,
            'pdct_total':int(pdct_quantity) * int(pdct_cost)
        }
        SALES.append(sale)
        return SALES
