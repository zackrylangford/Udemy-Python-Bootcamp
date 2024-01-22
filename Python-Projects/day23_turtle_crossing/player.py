from turtle import * 
import settings
from settings import *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def go_up(self):
        new_y = self.ycor() + settings.PLAYER_SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - settings.PLAYER_SPEED
        self.goto(self.xcor(), new_y)