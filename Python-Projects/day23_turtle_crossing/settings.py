from turtle import *

GAME_IS_ON = True
GAME_UPDATE_INTERVAL = 40
PLAYER_SPEED = 20


screen = Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

def exit_game():
    screen.bye()



