from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.penup()  # Make sure to lift the pen up before moving
        self.goto(x, y)  # Move to the desired position
        self.color("white")
        self.hideturtle()  # Hide the turtle icon
        self.write(f"{self.score}", align="center", font=("Courier", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()  # Clear the previous score
        self.write(f"{self.score}", align="center", font=("Courier", 24, "normal"))
        if self.score == 2:
            self.goto(0, 0)
            self.write("YOU WIN!", align="center", font=("Courier", 24, "normal"))  