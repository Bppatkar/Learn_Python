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


class Battery:
    def battery_info(self):
        return "this is battery"


class Engine:
    def engine_info(self):
        return "this is engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
