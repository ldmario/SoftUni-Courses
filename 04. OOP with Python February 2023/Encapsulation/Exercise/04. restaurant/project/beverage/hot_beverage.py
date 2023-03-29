from project.beverage.beverage import Beverage


class HotBeverage(Beverage):
    def __init__(self, name: str, price: float, milliliters: float):
        super(HotBeverage, self).__init__(name, price, milliliters)
