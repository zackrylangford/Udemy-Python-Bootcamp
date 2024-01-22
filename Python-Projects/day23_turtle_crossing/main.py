from turtle import *
from settings import *
from player import Player
from car import Car
from scoreboard import Scoreboard
import random
import settings


# Place the player on the screen
player_1 = Player()


# #Place cars on the screen
cars = []
for _ in range(10):
    new_car = Car()
    cars.append(new_car)

# Place scoreboard on the screen
scoreboard = Scoreboard(-80, 270)

def restart_game():
    global is_game_on, cars, player_1, scoreboard
    is_game_on = True
    player_1.goto(0, -280)  # Reset player position
    scoreboard.reset_game()  # Reset scoreboard
    for car in cars:
        car.goto(480, random.randint(-250, 250))  # Reset cars
    main_game_loop()


# Keyboard bindings
screen.listen()
screen.onkey(exit_game, "Escape")
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")
screen.onkey(restart_game, "space")

is_game_on = True

def main_game_loop():
    global is_game_on
    if is_game_on:
        global cars 
        for car in cars:
            car.drive_forward()
            if car.xcor() < -400: 
                car.new_car() 

        #Detect if player makes it to the top
        if player_1.ycor() > 280:
            player_1.goto(0,-280)
            scoreboard.increase_level()
            scoreboard.update_scoreboard()
            settings.MIN_CAR_SPEED += 1
            settings.MAX_CAR_SPEED += 1

        #Detect collision with car
        for car in cars:
            if car.distance(player_1) < 20:
                scoreboard.game_over()
                is_game_on = False
                player_1.goto(0,-280)


    screen.update()
    if is_game_on:    
        screen.ontimer(main_game_loop, settings.GAME_UPDATE_INTERVAL)
        


main_game_loop()

screen.mainloop()


