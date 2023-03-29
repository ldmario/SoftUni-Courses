from project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name: str, price: float, grams: float):
        super(ColdBeverage, self).__init__(name, price, grams)
