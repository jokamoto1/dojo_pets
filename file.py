class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def sleep(self):
        self.energy += 25
        ("Energy is: " + str(self.energy))
        return self
    def eat(self):
        self.energy += 5 
        self.health += 10
        print("Health is: " + str(self.health))
        print("Energy is: " + str(self.energy))
        return self
    def play(self):
        self.health += 5
        print("Health is: " + str(self.health))
        return self
    def noise(self):
        print("sound")
        return self
        
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats =treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self
        
pet1 = Ninja("jeremy", "okamoto", "bone", "canned", Pet("doggyboy", "dog", "none"))
pet1.walk().bathe().feed()