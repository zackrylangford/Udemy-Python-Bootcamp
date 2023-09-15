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


def process_coins():
    """Process the coins inserted by the user"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def check_transaction(total, order):
    pass

def update_resources():
    pass


def report():
    for name, amount in resources.items():
        print(f"{name.capitalize()}: {amount}{resource_units[name]}")



while coffee_machine_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        print("Shutting down")
        coffee_machine_on = False
    elif user_order == "report":
        report()
    elif user_order in MENU:
        print(f"You ordered: {user_order}")
        if check_resources(user_order) == False:
            report()
        else:
            money_paid = (process_coins())
            print(money_paid)
    else:
        print("Please select a valid option")


