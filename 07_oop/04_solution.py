
 # //! Encapsulation


class Car:
    def __init__(self, model, brand):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"


class ElectricCar(Car):
    def __init__(self, model, brand):
        super().__init__(model, brand)
       


my_electric_car = ElectricCar("Tesla", "Model S")
# print(my_electric_car.__brand)
print(my_electric_car.get_brand())
