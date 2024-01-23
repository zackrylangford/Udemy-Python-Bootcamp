from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()  # Initialize high_score attribute
        self.color("blue")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear the previous score/high score text
        self.goto(0, 270)  # Position for score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0, 240)  # Position for high score, slightly lower
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def get_high_score(self):
        with open("Python-Projects/day20-snake/data.txt") as file:
            high_score = int(file.read())
            file.close()
            return high_score


    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Python-Projects/day20-snake/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
                file.close()
            self.clear()
            self.update_scoreboard()
        else:
            self.clear()
            self.update_scoreboard()