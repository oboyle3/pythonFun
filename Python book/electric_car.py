# electric_car.py
from car import Car



class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        print(f"The battery size is {self.battery_size} kWh")

my_leaf = ElectricCar('Nissan', 'Leaf Hybrid x2', 2024)
my_car = ElectricCar('chevy','bolt', 2021)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


