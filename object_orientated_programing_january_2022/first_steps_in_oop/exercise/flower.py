class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.is_happy = False
        self.name = name
        self.water_requirements = water_requirements

    def water(self, quantity):
        if self.water_requirements <= quantity:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"
