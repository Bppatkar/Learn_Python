# class Car:
#     brand = None
#     model = None


# my_car = Car()
# print(my_car)


class Car:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model
        # Car.total_car += 1


my_car = Car("Harrier", "Tata")
# print(my_car.brand)
# print(my_car.model)

my_new_car = Car("Toyota", "Corolla")
# print(my_new_car.brand)
# print(my_new_car.model)