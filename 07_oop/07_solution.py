# //? Static method -> A method that belongs to a class rather than an instance of the class


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "Cars are means of transport"


class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)


my_car = Car("Mahindra", "Xuv 3Xo")

my_new_car = ElectricCar("Tata", "Safari")

# On the class directly
print(Car.general_description())
# "Cars are means of transport"

# On the subclass instance
print(my_new_car.general_description())
# TypeError: "Cars are means of transport" if we dont use static method keyword

# On the subclass itself
print(ElectricCar.general_description())
# "Cars are means of transport"

""" 
When to Use Static Methods
Static methods are useful for:

Utility functions related to the class

Helper methods that don't need instance data

Alternative constructors

Validation methods 
"""

# //! Example with Utility Methods

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @staticmethod
    def is_vintage(year):
        return year < 1990

    @staticmethod
    def create_from_string(car_string):
        brand, model, year = car_string.split(",")
        return Car(brand, model, int(year))

# Usage
print(Car.is_vintage(1985))  # True
print(Car.is_vintage(2020))  # False

my_car = Car.create_from_string("Toyota,Corolla,2022")
print(f"{my_car.brand} {my_car.model}")  # Toyota Corolla
