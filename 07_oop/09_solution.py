class Car:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.model} {self.brand}"


class ElectricCar(Car):
    def __init__(self, model, brand, batterySize):
        super().__init__(model, brand)
        self.batterySize = batterySize


my_electric_car = ElectricCar("Tesla", "Model S", "80KwH")

print(isinstance(my_electric_car, Car))
print(isinstance(my_electric_car, ElectricCar))
