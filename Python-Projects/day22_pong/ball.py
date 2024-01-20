from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10  # Movement in the x-direction
        self.y_move = 10  # Movement in the y-direction

    def move(self):
        """ Move the ball """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce(self):
        """ Bounce the ball off the top and bottom walls """
        self.y_move *= -1  # Reverse the y-direction

