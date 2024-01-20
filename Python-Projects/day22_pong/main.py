from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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

scoreboard = Scoreboard()

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
        ball.bounce()

    screen.update()  # Manually update the screen

    # Schedule the next update
    screen.ontimer(main_game_loop, 30) 
    
# Initialize the main game loop
main_game_loop()

# Start the event loop
screen.mainloop()