import colorgram
import turtle as t
import random

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 20)

# Create tuples in a list for each color without the name and hsl

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)


# Function to return a random color from the list of colors
def random_color(colors_tuple):
    return random.choice(colors_tuple)


t.colormode(255)
# Create a turtle object
tim = t.Turtle()

# Set the speed of the turtle
tim.speed(0)

# Set the width of the pen
tim.width(20)

# Move and draw circles across screen like Hirst based on the colors extracted from the image and use random colors
for i in range(10):
    for j in range(10):
        tim.penup()
        tim.goto(i * 50 - 250, j * 50 - 250)
        tim.pendown()
        tim.dot(20, random_color(rgb_colors))

# Hide the turtle
tim.hideturtle()

# Draw a screen
t.Screen()
# Exit on click
t.exitonclick()
