class StockAlgorithm:

    @classmethod
    def supply_stock_new(cls, current_stock, new_stock):
        return current_stock + new_stock

    @classmethod
    def supply_stock_old(cls, current_stock, new_stock, old_stock):
        return current_stock - old_stock + new_stock

    @classmethod
    def outlet_stock_new(cls, current_stock, new_stock):
        return current_stock - new_stock

    @classmethod
    def outlet_stock_old(cls, current_stock, new_stock, old_stock):
        return current_stock + old_stock - new_stock

    """ refund stock to store """

    @classmethod
    def refund_stock(cls, current_stock, old_stock):
        return current_stock + old_stock

    """ return stock to supplier """

    @classmethod
    def return_stock(cls, current_stock, old_stock):
        return current_stock - old_stock
