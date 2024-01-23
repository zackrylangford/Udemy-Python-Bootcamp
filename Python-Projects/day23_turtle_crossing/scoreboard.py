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
        self.display_high_score()
        

    def update_scoreboard(self):
        self.clear()
        self.display_high_score()  # Display high score
        self.goto(-80, 270)  # Position for the level display
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        if self.update_high_score():  # Check if high score needs to be updated
            self.display_high_score()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


    def reset_game(self):
        self.level = 1
        self.clear()
        self.goto(-80, 270)
        self.update_scoreboard()

    def update_high_score(self):
        with open(settings.HIGH_SCORE_FILE, mode="r") as file:
            high_score = int(file.read())
        if self.level > high_score:
            with open(settings.HIGH_SCORE_FILE, mode="w") as file:
                file.write(str(self.level))
                file.close()
            return True
        else:
            file.close()
            return False
        
    def display_high_score(self):
        with open(settings.HIGH_SCORE_FILE, mode="r") as file:
            high_score = int(file.read())
            self.goto(200, 270)  # Position for high score display
            self.write(f"High Score: {high_score}", align="left", font=("Courier", 24, "normal"))
            file.close()