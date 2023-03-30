from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name: str, price: float, grams: float = GRAMS):
        super(Salmon, self).__init__(name, price, grams)
