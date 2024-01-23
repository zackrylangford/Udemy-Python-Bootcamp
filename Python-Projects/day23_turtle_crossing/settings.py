from turtle import *
import random

GAME_UPDATE_INTERVAL = 10
PLAYER_SPEED = 20
MIN_CAR_SPEED = 1
MAX_CAR_SPEED = 4
GAME_LEVEL = 1
HIGH_SCORE_FILE = "/Users/zackrylangford/Desktop/python-learning/Udemy-Python-Bootcamp/Python-Projects/day23_turtle_crossing/data.txt"



screen = Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

def exit_game():
    screen.bye()


