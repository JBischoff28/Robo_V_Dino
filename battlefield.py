import time
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:

    def __init__(self):
        self.robot = Robot()
        self.dino = Dinosaur()

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        time.sleep(3)

        if self.robot.health <= 0:
            print(f"{self.robot.name} is destroyed! {self.dino.name} has won the battle!")
        elif self.dino.health <= 0:
            print(f"{self.dino.name} is destroyed! {self.robot.name} has won the battle!")
        