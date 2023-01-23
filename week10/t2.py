class Dog:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def bark(self):
        print("Woof Woof!")

    def get_age(self):
        return self.age
    
dog1 = Dog("Fido",3)
dog1.bark() #Output:"Woof Woof!"
print(dog1.get_age()) #Output: 3