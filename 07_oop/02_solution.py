class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car('Harrier',"Tata")
print(my_car.full_name())