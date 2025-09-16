import random

def getInfo():
    name = input("What is your name?: ")

    try:
        age = int(input("What is your age?: "))
    except Exception:
        print("Sorry, you didn't enter an age.")
        getInfo()

class Player():

    def __init__(self, name, age, health, energy, fighterType):
        self.name = name
        self.age = age
        self.health = health
        self.energy = energy
        self.fighterType = fighterType
        self.weaponUsing = fists.name
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
        hitChance = random.randint(0, 100)
        if hitChance - weapon.accuracy <= 0 and self.energy >= weapon.energyUsed:
            print("Hit Successful!")
            enemy.health - weapon.damage
            weapon.energyUsed -= self.energy
        else:
            print("Hit Failed...")

    def useHeal(self, heal):
        print(f"Nice! Using {heal.name} for {heal.healAmount} HP")
        self.health += heal.healAmount

class Weapon():

    def __init__(self, name, damage, durability, energyUsed, accuracy):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.energyUsed = energyUsed
        self.accuracy = accuracy

class Heal:
    def __init__(self, name, healAmount, uses):
        self.name = name
        self.healAmount = healAmount
        self.uses = uses

fists = Weapon("Fists", 10, 999999999999, 5, 100)
player = Player("Akbar", 23, 67, 67, "Aura Farmer")
