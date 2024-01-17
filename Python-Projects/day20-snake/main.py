from turtle import *
from snake import Snake
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

sammy = Snake()

screen.listen()
screen.onkey(sammy.up, "Up")
screen.onkey(sammy.down, "Down")
screen.onkey(sammy.left, "Left")
screen.onkey(sammy.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sammy.move()

    # Detect collision with wall
    if sammy.head.xcor() > 280 or sammy.head.xcor() < -280 or sammy.head.ycor() > 280 or sammy.head.ycor() < -280:
        game_is_on = False
        print("Game Over")


screen.exitonclick()






