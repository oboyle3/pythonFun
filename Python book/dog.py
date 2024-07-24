class Dog:
    def __init__(self, name, age):
        # Initialize name and age attributes
        self.name = name
        self.age = age

    def sit(self):
        # Simulate dog sitting command
        print(f"{self.name} is now sitting")

    def roll_over(self):
        # Simulate dog rolling over command
        print(f"{self.name} rolled over")

# Create an instance of the Dog class
my_dog = Dog('Wille', 6)

# Print the dog's name
print(f"My dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")


my_dog.sit()
my_dog.roll_over()