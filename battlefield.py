import time
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:

    def __init__(self):
        self.robot = Robot("MetalMan")
        self.dino = Dinosaur("Titan", 0)

    def run_game(self):
        
        self.display_welcome()
        print("")
        self.battle_phase()
        print("")
        self.display_winner()


    def display_welcome(self):
        
        print("Please wait, loading game")
        load_text = "....."
        for char in load_text:
            print(char)
            time.sleep(0.20)

        print("This is the story of an epic battle!\n This battle was instigated when two large")
        print("companies decided that it was time to\n see who had the better military solution.")
        print("A robot named MetalMan, or a dinosaur named Titan.")
        print("")
        time.sleep(3)
        print("People from around the world gathered to watch\n and see who prevails. This is...")
        print("")
        time.sleep(3)
        string_effect = "ROBOT VS. DINOSAUR!"
        for char in string_effect:
            print(char, end='', flush=True)
            time.sleep(0.2)
        print("")
        time.sleep(5)

    def battle_phase(self):

        battling = True
        while battling == True:

            self.dino.attack(self.robot)
            print("")
            time.sleep(3)

            if self.robot.health <= 0:
                battling = False
                break

            self.robot.attack(self.dino)
            print("")
            time.sleep(3)

            if self.dino.health <= 0:
                battling = False
                break

    def display_winner(self):
        time.sleep(3)

        if self.robot.health <= 0:
            print(f"{self.robot.name} is destroyed! {self.dino.name} has won the battle!")
        elif self.dino.health <= 0:
            print(f"{self.dino.name} is destroyed! {self.robot.name} has won the battle!")