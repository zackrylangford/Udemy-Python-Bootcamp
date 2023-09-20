from turtle import Turtle, Screen
import turtle as t
import random


# tom = Turtle()
# terry = Turtle()

# tom.shape("turtle")
# terry.shape("turtle")

timmy = Turtle()
timmy.color("red")
timmy.shape("turtle")

color = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"] 

# Drawing a bunch of shapes overlayed
# size = 7
# for number in range(3, 11):
#     for _ in range(number):
#         for _ in range(size):
#             timmy.forward(size)
#         timmy.left(360/number)
#     timmy.color(random.choice(color))

# Drawing a random walk
# timmy.width(10)
# for _ in range(100):
#     timmy.forward(30)
#     timmy.setheading(random.choice([0, 90, 180, 270]))
#     timmy.color(random.choice(color))


t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    print(r, g, b)
    return (r, g, b)

# timmy.width(10)
# for _ in range(100):
#     timmy.forward(30)
#     timmy.setheading(random.choice([0, 90, 180, 270]))
#     timmy.color(random_color())

# Draw a spirograph
timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)


draw_spirograph(1)
screen = Screen()
screen.exitonclick()