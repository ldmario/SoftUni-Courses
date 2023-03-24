from project.car import Car


class FamilyCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int):
        super(FamilyCar, self).__init__(fuel, horse_power)

    def drive(self, kilometers: float):
        if self.fuel - kilometers * self.fuel_consumption >= 0:
            self.fuel -= kilometers * self.fuel_consumption
