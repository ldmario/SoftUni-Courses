from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel: float, horse_power: int):
        super(SportCar, self).__init__(fuel, horse_power)

    def drive(self, kilometers: float):
        if self.fuel - kilometers * self.fuel_consumption >= 0:
            self.fuel -= kilometers * self.fuel_consumption
