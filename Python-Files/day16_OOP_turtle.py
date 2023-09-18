
# from prettytable import PrettyTable, FRAME, ALL, NONE

from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)

my_screen = Screen()
print(my_screen.canvheight)

timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

my_screen.exitonclick()

# table = PrettyTable()


# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar"])

# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = ("r")
# table.padding_width = 0




# print(table)