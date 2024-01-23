from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

sammy = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if sammy.head.distance(food) < 15:
        food.refresh()
        sammy.extend()
        scoreboard.increase_score()
        scoreboard.update_high_score()

    # Detect collision with wall
    if sammy.head.xcor() > 280 or sammy.head.xcor() < -280 or sammy.head.ycor() > 280 or sammy.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        print("Game Over")


    # Detect collision with tail
    for segment in sammy.segments[1:]:
        if sammy.head.distance(segment) < 10:
            game_is_on = False
            print("Game Over")
            scoreboard.game_over()
        

screen.exitonclick()







