from turtle import *

GAME_IS_ON = True
GAME_UPDATE_INTERVAL = 40


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

def exit_game():
    screen.bye()



