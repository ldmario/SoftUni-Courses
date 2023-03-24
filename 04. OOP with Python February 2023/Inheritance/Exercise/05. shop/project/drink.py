from project.product import Product


class Drink(Product):
    def __init__(self, name: str, quantity: int = 10):
        super(Drink, self).__init__(name, quantity)

    def __repr__(self):
        return self.name
