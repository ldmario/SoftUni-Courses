from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel: float, horse_power: int):
        super(CrossMotorcycle, self).__init__(fuel, horse_power)

    def drive(self, kilometers: float):
        if self.fuel - kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION >= 0:
            self.fuel -= kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION
