class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1


class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)


my_car = Car("Mahindra", "Xuv 3Xo")

my_new_car = ElectricCar("Tata", "Safari")

print(Car.total_car)
