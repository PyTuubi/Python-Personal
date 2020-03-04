class Dog():

    # Class object attribute
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self,breed,name,spots):

        self.breed = breed
        self.name = name

        # Boolean
        self.spots = spots

    # Operations / Actions --> Methods
    def bark(self, number):
        print(f"Woof! My name is {self.name}! " * number)


my_dog = Dog('Golden', 'Jemma', False)

# Remember () for methods to execute
print(my_dog.bark(2))


class Circle():

    # Class object attribute
    pi = 3.14

    # Default value passed in for radius
    def __init__(self, radius=1):

        self.radius = radius

    def get_circumference(self):
        return self.radius * Circle.pi * 2



my_circle = Circle(2)

print(my_circle.get_circumference())

