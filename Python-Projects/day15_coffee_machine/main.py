# Coffee machine
from menu import MENU, resources, resource_units
# Initial resource values

coffee_machine_on = True


def check_resources(order):
    """Check if there are enough resources to make the order"""
    ingredients = MENU[order]["ingredients"]

    for item, amount in ingredients.items():
        if item in resources:
            if amount > resources[item]:
                print(f"Sorry there is not enough {item}")
                return False
    return "Enough resources"

def make_coffee(order):
    print(f"Dispensing {order} now, please enjoy responsibly!")
    ingredients = MENU[order]["ingredients"]
    for item, amount in ingredients.items():
        if item in resources:
            resources[item] -= amount
            # print(f"{item.capitalize()} remaining: {resources[item]}{resource_units[item]}")

def get_integer(prompt):
    """Get an integer input from the user, with error checking."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def process_coins():
    """Process the coins inserted by the user"""
    print("Please insert coins.")
    quarters = get_integer("How many quarters?: ")
    dimes = get_integer("How many dimes?: ")
    nickles = get_integer("How many nickles?: ")
    pennies = get_integer("How many pennies?: ")

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def check_transaction(paid, order):
    change_needed = paid - order
    if change_needed >= 0:
        print(f"Change returned: ${change_needed:.2f}")
        resources['money'] += order
        return True
    else:
        print("Sorry, that is not enough, money refunded.")
        return False



def report(type):
    if type == "report":
        for name, amount in resources.items():
            print(f"{name.capitalize()}: {amount}{resource_units[name]}")
    else:
        for name, amount in resources.items():
            if name != "money":
                print(f"{name.capitalize()}: {amount}{resource_units[name]}")




while coffee_machine_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        print("Shutting down")
        coffee_machine_on = False
    elif user_order == "report":
        report("report")
    elif user_order in MENU:
        print(f"You ordered: {user_order}")
        if check_resources(user_order) == False:
            report("ingredients")
        else:
            money_paid = (process_coins())
            beverage_cost = MENU[user_order]["cost"]
            if check_transaction(money_paid, beverage_cost):
                print("Making drink now")
                make_coffee(user_order)
    else:
        print("Please select a valid option")


