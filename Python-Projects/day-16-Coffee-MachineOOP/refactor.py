import menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
zacks_machine = CoffeeMaker()
zacks_menu = menu.Menu()
zacks_money = MoneyMachine()

while is_on:
    options = zacks_menu.get_items()
    order = input(f"What would you like to order?{options}")
    if order == "off":
        is_on = False
        print("Coffee machine shutting down")
    elif order == "report":
        zacks_machine.report()
        zacks_money.report()
    else:
        user_order = zacks_menu.find_drink(order)
        if zacks_machine.is_resource_sufficient(user_order):
            order_cost = user_order.cost
            print(f"A {order} costs: ${order_cost:.2f}")
            if zacks_money.make_payment(order_cost):
                zacks_machine.make_coffee(user_order)
