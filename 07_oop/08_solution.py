class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)


my_car = Car("Mahindra", "Xuv 3Xo")
my_car.model = "City"
print(my_car.model)


# @model.setter
# def model(self, value):
#   self._model = value  # Add setter to allow modification
