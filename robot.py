import random
from weapons import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapons = []

    def attack(self, dinosaur):

        self.active_weapons.append(Weapon("Circular Saw Arm", 25))
        self.active_weapons.append(Weapon("Arm Cannon", 20))
        self.active_weapons.append(Weapon("Core Blast", 50))
        select_weapon = random.choice(self.active_weapons)

        if select_weapon == self.active_weapons[0]:
            print(f"{self.name} attacked {dinosaur.name} with {self.active_weapons[0].name},\n dealing {self.active_weapons[0].attack_power} damage!")
            dinosaur.health -= self.active_weapons[0].attack_power
        elif select_weapon == self.active_weapons[1]:
            print(f"{self.name} attacked {dinosaur.name} with {self.active_weapons[1].name},\n dealing {self.active_weapons[1].attack_power} damage!")
            dinosaur.health -= self.active_weapons[1].attack_power
        elif select_weapon == self.active_weapons[2]:
            print(f"{self.name} attacked {dinosaur.name} with {self.active_weapons[2].name},\n dealing {self.active_weapons[2].attack_power} damage!")
            dinosaur.health -= self.active_weapons[2].attack_power

        print(f"{self.name}'s Health: {self.health} ----- {dinosaur.name}'s Health: {dinosaur.health}")