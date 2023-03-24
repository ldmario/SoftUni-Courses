from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers: float):
        if self.fuel - kilometers * Vehicle.DEFAULT_FUEL_CONSUMPTION >= 0:
            self.fuel -= kilometers * Vehicle.DEFAULT_FUEL_CONSUMPTION
