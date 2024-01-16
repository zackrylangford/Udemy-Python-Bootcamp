from turtle import *
import random
import time
import turtle

timmy = Turtle()
timmy.color("red")
timmy.shape("turtle")
timmy.name = "Timmy"

tommy = Turtle()
tommy.color("blue")
tommy.shape("turtle")
tommy.name = "Tommy"

tummy = Turtle()
tummy.color("purple")
tummy.shape("turtle")
tummy.name = "Tummy"

turtles = [timmy, tommy, tummy]

def move_forwards(turtle):
    turtle.forward(random.randint(1, 10))

# def move_backwards(turtle):
#     turtle.backward(10)

# def turn_left(turtle):
#     turtle.left(10)

# def turn_right(turtle):
#     turtle.right(10)

# def clear(turtle):
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()

screen = Screen()
screen.listen()

def race_reset():
    timmy.clear()
    tommy.clear()
    tummy.clear()
    timmy.penup()
    tommy.penup()
    tummy.penup()
    timmy.goto(-200, 0)
    tommy.goto(-200, 50)
    tummy.goto(-200, -50)
    timmy.pendown()
    tommy.pendown()
    tummy.pendown()
    prediction = place_your_bet()
    race(start=True, prediction=prediction)

def place_your_bet():
    prediction = screen.textinput("Place Your Bet", "Who do you think will win?")
    return prediction

def race(start, prediction):
    race_on = start
    while race_on:
        for turtle in turtles:
            move_forwards(turtle)
            xcor = int(turtle.xcor())
            if xcor > 200:
                race_on = False
                winner = f"{turtle.name} has won the race!"
                if prediction == turtle.name.lower():
                    result = "You won!"
                else:
                    result = "You lost."
                screen.title(f"{winner}-{result}")
                race_reset()

## Key bindings for racing
            
screen.onkey(lambda: race_reset(), "space")
screen.onkey(lambda: race(True), "s")
screen.onkey(lambda: race(False), "f")


screen.exitonclick()



# # Key bindings for timmy
# screen.onkey(lambda: move_forwards(timmy), "w")
# screen.onkey(lambda: move_backwards(timmy), "s")
# screen.onkey(lambda: turn_left(timmy), "a")
# screen.onkey(lambda: turn_right(timmy), "d")
# screen.onkey(lambda: clear(timmy), "c")

# # Key bindings for tommy
# screen.onkey(lambda: move_forwards(tommy), "Up")  # Fix: Replace "up" with "Up"
# screen.onkey(lambda: move_backwards(tommy), "Down")
# screen.onkey(lambda: turn_left(tommy), "Left")
# screen.onkey(lambda: turn_right(tommy), "Right")
# screen.onkey(lambda: clear(tommy), "r")

