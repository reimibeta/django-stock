class StockAlgorithm:

    @classmethod
    def supply_stock(cls, current_stock, new_stock, old_stock=None):
        if old_stock is None:
            return current_stock + new_stock
        else:
            return current_stock - old_stock + new_stock

    @classmethod
    def outlet_stock(cls, current_stock, new_stock, old_stock=None):
        if old_stock is None:
            return current_stock - new_stock
        else:
            return current_stock + old_stock - new_stock

    """ refund stock to store """
    @classmethod
    def refund_stock(cls, current_stock, old_stock):
        return current_stock + old_stock

    """ return stock to supplier """
    @classmethod
    def return_stock(cls, current_stock, old_stock):
        return current_stock - old_stock
