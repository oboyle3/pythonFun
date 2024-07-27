# electric_car.py
from car import Car
#
# class Car:
#     def __init__(self, make, model, year):
#         # Initialize attributes to describe a car
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         # Return a neatly formatted name
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()



class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        print(f"The battery size is {self.battery_size} kWh")

my_leaf = ElectricCar('Nissan', 'Leaf Hybrid x2', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
