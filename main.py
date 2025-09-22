import random

class Player():

    def __init__(self, name, age, health, energy, fighterType, weaponUsing):
        self.name = name
        self.age = age
        self.health = health
        self.energy = energy
        self.fighterType = fighterType
        self.weaponUsing = weaponUsing
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
staff = Weapon("Staff", 15, 999999999999, 8, 95)
bow = Weapon("Bow", 20, 999999999999, 15, 85)
fighterTypes = [{"name": "Mage", "health": 80, "energy": 120, "weapon": staff}, {"name": "Brute", "health": 150, "energy": 150, "weapon": fists}, {"name": "Archer", "health": 90, "energy": 90, "weapon": bow}]

def getInfo():
    name = input("What is your name?: ")

    try:
        age = int(input("What is your age?: "))
        for index, fighterType in enumerate(fighterTypes):
            print(f"{index + 1}. {fighterType["name"]}")
        fighterType = input("What is your fighter type?: ")
        if fighterType == "Mage" or "mage" or 1:
            player = Player(name, age, fighterTypes[0]["health"], fighterTypes[0]["energy"], fighterTypes[0]["name"], fighterTypes[0]["weapon"])
        elif fighterType == "Brute" or "brute" or 2:
            player = Player(name, age, fighterTypes[1]["health"], fighterTypes[1]["energy"], fighterTypes[1]["name"], fighterTypes[1]["weapon"])
        elif fighterType == "Archer" or "archer" or 3:
            player = Player(name, age, fighterTypes[2]["health"], fighterTypes[2]["energy"], fighterTypes[2]["name"], fighterTypes[2]["weapon"])
        else:
            print("Invalid Intent: Please enter a given fighter type.")
            getInfo()
    except Exception:
        print("Invalid Intent: Please double check your responses.")
        getInfo()

getInfo()
