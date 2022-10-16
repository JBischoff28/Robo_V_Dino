import time
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:

    def __init__(self):
        self.robot = Robot("MetalMan")
        self.dino = Dinosaur("Titan", 0)

    def run_game(self):
        
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        
        print("This is the story of an epic battle!\n This battle was instigated when two large")
        print("companies decided that it was time to\n see who had the better military solution.")
        time.sleep(1.25)
        print("People from around the world gathered to watch\n and see who prevails. This is...")
        time.sleep(2)
        string_effect = "ROBOT VS. DINOSAUR!"
        for char in string_effect:
            print(char, end='', flush=True)
        time.sleep(3)

    def battle_phase(self):
        
        while self.dino.health and self.robot.health > 0:
            self.dino.attack(self.robot)
            print("")
            time.sleep(2)
            self.robot.attack(self.dino)
            print("")

    def display_winner(self):
        time.sleep(3)

        if self.robot.health <= 0:
            print(f"{self.robot.name} is destroyed! {self.dino.name} has won the battle!")
        elif self.dino.health <= 0:
            print(f"{self.dino.name} is destroyed! {self.robot.name} has won the battle!")
        