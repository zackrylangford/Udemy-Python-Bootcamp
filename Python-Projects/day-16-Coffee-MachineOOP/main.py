from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
zacks_machine = CoffeeMaker()
zacks_menu = Menu()
valid_order = ["espresso", "latte", "cappucino"]

while is_on:
    order = input("What would you like to order? (espresso/latte/cappucino)")
    if order == "off":
        is_on = False
        print("Coffee machine shutting down")
    if order == "report":
        zacks_machine.report()
    elif order in valid_order:
        user_order = zacks_menu.find_drink(order)
        if zacks_machine.is_resource_sufficient(user_order):
            print("Yes")

    else:
        print("not a valid order")



