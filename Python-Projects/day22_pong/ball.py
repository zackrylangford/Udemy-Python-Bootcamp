import settings
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = settings.BALL_MOVE_SPEED
        self.y_move = settings.BALL_MOVE_SPEED

    def move(self):
        """ Move the ball """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        """ Bounce the ball off the top and bottom walls """
        self.y_move *= -1  # Reverse the y-direction

    def bounce_x(self):
        """ Bounce the ball off the paddles """
        self.x_move *= -1

    def reset_position(self):
        """ Reset the ball position """
        self.goto(0, 0)
        self.bounce_x()