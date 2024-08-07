class Pip:
    def __init__(self, health, name, age, rank, vault):
        # Initialize attributes to describe the player
        self.health = health
        self.name = name
        self.age = age
        self.rank = rank
        self.vault = vault

    def get_all_info(self):
        # Return a neatly formatted info
        all_info = f"{self.health} {self.name} {self.age} {self.rank} {self.vault}"
        return all_info.title()
    
player1 = Pip('100%', 'Henry Smith', 23, 'Private', 32)
print(player1.get_all_info())
player2 = (Pip'98%','Dan Carney',42,'Sargent',92)

#pats_car = Car('audi', 'a4', 2024)
#print(pats_car.get_descriptive_name())
#pats_car.odometer_reading = 23
##pats_car.read_odometer()