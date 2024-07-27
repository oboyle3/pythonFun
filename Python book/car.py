class Car:
    def __init__(self, make, model, year):
        # Initialize attributes to describe a car
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        # Return a neatly formatted name
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
pats_car = Car('audi', 'a4', 2024)
print(pats_car.get_descriptive_name())
