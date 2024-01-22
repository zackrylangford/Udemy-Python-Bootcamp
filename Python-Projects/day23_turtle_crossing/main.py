from turtle import *
from settings import *
from player import Player
import settings


# Place the player on the screen
player_1 = Player()


# Keyboard bindings
screen.listen()
screen.onkey(exit_game, "Escape")
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")


def main_game_loop():
    
    screen.update()
    screen.ontimer(main_game_loop, settings.GAME_UPDATE_INTERVAL)
    pass


main_game_loop()

screen.mainloop()