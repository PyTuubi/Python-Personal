# Class keyword

class Dog():
    
    def __init__(self,breed,name,spots):
        
        # Expect string
        self.breed = breed
        self.name = name

        # Expect boolean
        self.spots = spots





my_dog = Dog(breed='Lab', name='Jyn', spots=True)

print(my_dog.name)


