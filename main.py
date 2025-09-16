def getInfo():
    name = input("What is your name?: ")

    try:
        age = int(input("What is your age?: "))
    except Exception:
        print("Sorry, you didn't enter an age.")
        getInfo()

class Player():

    def __init__(self, name, age, health, energy, fighterType, weaponUsing):
        self.name = name
        self.age = age
        self.health = health
        self.energy = energy
        self.fighterType = fighterType
        self.weaponUsing = Fists.name
        self.inventory = []

    def printStats(self):
        print(f"Name: {self.name}")
        print(f"Fighter Type: {self.fighterType}")
        self.printInventory()

    def printInventory(self):
        print("Inventory:")
        for index, item in enumerate(self.inventory):
            print(f"{index + 1}. {item}")

    def takeDamage(self, damage, reason=""):
        print(f"Oof! Took {damage} damage because {reason}...")
        self.health -= damage

    def attack(self, weapon, enemy):
        print(f"{self.name} attacked {enemy.name}")
        enemy.health - weapon.damage

class Item():

    def __init__(self, name):
        self.name = name

class Weapon(Item):

    def __init__(self, damage, durability, accuracy):
        self.damage = damage
        self.durability = durability
        self.accuracy = accuracy

Fists = Weapon("Fists", 10, 999999999999, 100)
