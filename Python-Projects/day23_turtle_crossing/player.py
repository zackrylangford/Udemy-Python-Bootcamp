from turtle import * 

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()