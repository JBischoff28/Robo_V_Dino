

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.attack_type = ["Bite", "Claw", "Ram"]

    def attack(self, robot):
        
        if self.attack_type == "Bite":
            print(f"{self.name} attacked {}")

    