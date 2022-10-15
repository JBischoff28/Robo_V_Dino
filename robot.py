import random
from weapons import Weapon
from dinosaur import Dinosaur

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapons = []

    def attack(self, dinosaur):
        
        dinosaur = Dinosaur("")

        self.active_weapons[0] = Weapon("Circular Saw Arm", 45)
        self.active_weapons[1] = Weapon("Arm Cannon", 35)
        self.active_weapons[2] = Weapon("Core Blast", 75)
        select_weapon = random.choice(self.active_weapons)

        if select_weapon == self.active_weapons[0]:
            print(f"{self.name} attacked {dinosaur} with {select_weapon},\n dealing {self.active_weapons[0].attack_power}!")
            dinosaur.health -= self.active_weapons[0].attack_power
        elif select_weapon == self.active_weapons[1]:
            print(f"{self.name} attacked {dinosaur} with {select_weapon},\n dealing {self.active_weapons[1].attack_power}!")
            dinosaur.health -= self.active_weapons[1].attack_power
        if select_weapon == self.active_weapons[2]:
            print(f"{self.name} attacked {dinosaur} with {select_weapon},\n dealing {self.active_weapons[2].attack_power}!")
            dinosaur.health -= self.active_weapons[2].attack_power

        print(f"{self.name}'s Health: {self.health} ----- {dinosaur.name}'s Health: {dinosaur.health}")
