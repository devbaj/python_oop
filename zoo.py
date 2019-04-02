class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100
    def display_info(self):
        print(f"Animal: {self.name}, Age: {self.age}, Health Index {self.health}, Happiness Index: {self.health}")
        return self
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 70
        self.happiness = 20

class Bear(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        self.health = 80
        self.happiness = 100

class Platypus(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 30
        self.happiness = 50

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age):
        self.animals.append( Lion(name, age) )
        return self
    def add_bear(self, name, age, color):
        self.animals.append( Bear(name, age, color) )
        return self
    def add_platypus(self, name, age):
        self.animals.append( Platypus(name, age))
        return self
    def print_zoo_info(self):
        print ("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Safari XTREME")
zoo1.add_lion("Nala", 8).add_bear("Koda", 4, "brown").add_platypus("Parry", 12).add_lion("Mufasa", 25)
zoo1.print_zoo_info()

zoo1.animals[1].feed()
zoo1.animals[3].feed()

zoo1.print_zoo_info()