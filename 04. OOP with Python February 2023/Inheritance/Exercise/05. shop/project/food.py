from project.product import Product


class Food(Product):
    def __init__(self, name: str, quantity: int = 15):
        super(Food, self).__init__(name, quantity)

    def __repr__(self):
        return self.name
