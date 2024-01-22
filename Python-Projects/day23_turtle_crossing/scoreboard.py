import settings
from turtle import *

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.level = 1
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    def reset_game(self):
        self.level = 1
        self.clear()
        self.goto(-80, 270)
        self.update_scoreboard()