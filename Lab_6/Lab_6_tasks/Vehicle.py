from typing import override
class Vehicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

    def get_info(self):
        return f"Марка : {self.mark}, Модель: {self.model}"

class Car(Vehicle):
    @override
    def __init__(self, mark, model, fuel_type):
        super().__init__(mark, model)
        self.fuel_type = fuel_type

    @override
    def get_info(self):
        return f"Марка: {self.mark}, Модель: {self.model}, Тип топлива: {self.fuel_type}"

vehicle = Vehicle("Tesla", "Model S")
car = Car("Tesla", "Model S", "Электричество")
print(vehicle.get_info())
print(car.get_info())
