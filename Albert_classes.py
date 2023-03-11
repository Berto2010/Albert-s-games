class Animal():
    def __init__(self, type, animal_class, age):
        self.type = type
        self.animal_class = animal_class
        self.age = age
        

class Dog(Animal):
    def __init__(self, type, animal_class, age, fur_length):
        Animal.__init__(self, type, animal_class, age)
        self.fur_length = fur_length
        
capybara = Dog("Dog", "Mammal", 30000000000000000000, "Long")
print(vars(capybara))

class Frog(Animal):
    def __init__(self, type, animal_class, age, size):
        Animal.__init__(self, type, animal_class, age)
        self.size = size
        
capybara = Frog("Frog", "Amphibian", 10000000000000000000000000000, "Small")
print(vars(capybara))

def finding_the_root(num):
    for x in range(num):
        if x**2 == num:
            return x
result = finding_the_root(26)
print (result)