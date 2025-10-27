

# //! Polymorphism --> Polymorphism is the ability of something to take on many forms or behave in different ways. [fuel_type here]


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Mahindra", "Xuv 3Xo")
# print(my_car.brand)
print(my_car.fuel_type())


my_new_car = ElectricCar("Tata", "Safari")
print(my_new_car.fuel_type())
