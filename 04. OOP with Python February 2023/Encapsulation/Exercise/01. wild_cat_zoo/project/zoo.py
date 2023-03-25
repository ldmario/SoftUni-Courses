from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value):
        self.__budget = value
        
    @property
    def animal_capacity(self):
        return self.__animal_capacity
    
    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value
        
    @property
    def workers_capacity(self):
        return self.__workers_capacity
    
    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value

    def add_animal(self, animal: Animal, price: [int, float]):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        if self.__budget >= price and self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker: str):
        for w in self.workers:
            if w.name == worker:
                self.workers.remove(w)
                return f"{worker} fired successfully"
        return f"There is no {worker} in the zoo"

    def pay_workers(self):
        if sum([w.salary for w in self.workers]) <= self.__budget:
            self.__budget -= sum([w.salary for w in self.workers])
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_needed = 0
        for animal in self.animals:
            total_money_needed += animal.money_for_care
        if self.__budget >= total_money_needed:
            self.__budget -= total_money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:",
        ]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(str(x) for x in result)

    def workers_status(self):
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet'],
        ]

        return "\n".join(result)
