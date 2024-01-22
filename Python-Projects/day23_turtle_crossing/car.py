from turtle import Turtle
import random
import settings

colors = ['red', 'blue', 'green', 'yellow']

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(colors))
        self.penup()
        self.goto(480, random.randint(-250, 250))
        self.speed = random.randint(settings.MIN_CAR_SPEED, settings.MAX_CAR_SPEED)  # Random speed

    def drive_forward(self):
        new_x = self.xcor() - self.speed  # Use the car's individual speed
        self.goto(new_x, self.ycor())

    def new_car(self):
        self.color(random.choice(colors))  # Correct the syntax for choosing a color
        self.goto(480, random.randint(-250, 250))  # Reset position
        self.speed = random.randint(settings.MIN_CAR_SPEED, settings.MAX_CAR_SPEED)  # Reset speed