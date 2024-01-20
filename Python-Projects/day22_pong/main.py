from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import settings
from settings import *

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Right paddle setup
right_paddle = Paddle()
right_paddle.goto(350, 0)

# Left paddle setup
left_paddle = Paddle()
left_paddle.goto(-350, 0)

# Ball setup
ball = Ball()

# Scoreboard setup
right_scoreboard = Scoreboard(100, 240)
left_scoreboard = Scoreboard(-100, 240)


# On escape key press exit the game
def exit_game():
    screen.bye()

# Keyboard bindings
screen.listen()
screen.onkey(exit_game, "Escape")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


def main_game_loop():
    # Any game logic or updates go here
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 60 and ball.ycor() > right_paddle.ycor() - 50):
        ball.bounce_x()
        increase_ball_speed()

    # Check for collision with left paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 60 and ball.ycor() > left_paddle.ycor() - 50):
        ball.bounce_x()
        increase_ball_speed()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        left_scoreboard.increase_score()
        reset_ball_speed()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        right_scoreboard.increase_score()
        reset_ball_speed()

    screen.update()  # Manually update the screen

    # Schedule the next update
    screen.ontimer(main_game_loop, settings.GAME_UPDATE_INTERVAL) 

# Initialize the main game loop
main_game_loop()

# Start the event loop
screen.mainloop()