class Restaurant:
    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"This describes the restaurant name and the name is: {self.name}")

    def open_restaurant(self):
        print(f"This tells if this restaurant is open and this restaurant is: {self.cuisine}")

# Create an instance of the Restaurant class
first_place = Restaurant("Ryans", "Open")

# Call methods on the instance
first_place.describe_restaurant()
first_place.open_restaurant()


   
    
