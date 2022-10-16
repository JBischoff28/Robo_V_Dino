import random

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.attack_type = ["Bite", "Claw", "Ram"]

    def attack(self, robot):
        
        set_attack_type = random.choice(self.attack_type)

        if set_attack_type == "Bite":
            self.attack_power = 20
            print(f"{self.name} attacked {robot.name} with {set_attack_type}, dealing {self.attack_power} damage!")
            robot.health -= self.attack_power
        elif set_attack_type == "Claw":
            self.attack_power = 25
            print(f"{self.name} attacked {robot.name} with {set_attack_type}, dealing {self.attack_power} damage!")
            robot.health -= self.attack_power
        elif set_attack_type == "Ram":
            self.attack_power = 30
            self.health -= 10
            print(f"{self.name} attacked {robot.name} with {set_attack_type}, dealing {self.attack_power} damage!\n {self.name} took 10 self-damage.")
            robot.health -= self.attack_power

        print(f"{robot.name}'s Health: {robot.health} ----- {self.name}'s Health: {self.health}")