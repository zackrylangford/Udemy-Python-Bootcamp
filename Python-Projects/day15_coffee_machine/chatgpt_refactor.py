from menu import MENU, resources, resource_units

coffee_machine_on = True


def check_resources(order):
    ingredients = MENU[order]["ingredients"]
    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def make_coffee(order):
    print(f"Dispensing {order} now, please enjoy responsibly!")
    ingredients = MENU[order]["ingredients"]
    for item, amount in ingredients.items():
        resources[item] -= amount


def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")


def process_coins():
    print("Please insert coins.")
    quarters = get_integer("How many quarters?: ")
    dimes = get_integer("How many dimes?: ")
    nickles = get_integer("How many nickles?: ")
    pennies = get_integer("How many pennies?: ")

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def check_transaction(paid, order_cost):
    change_needed = paid - order_cost
    if change_needed >= 0:
        print(f"Change returned: ${change_needed:.2f}")
        resources['money'] += order_cost
        return True
    else:
        print("Sorry, that is not enough, money refunded.")
        return False


def report(is_admin_report):
    for name, amount in resources.items():
        if is_admin_report or name != "money":
            print(f"{name.capitalize()}: {amount}{resource_units[name]}")


while coffee_machine_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_order == "off":
        print("Shutting down")
        coffee_machine_on = False
    elif user_order == "report":
        report(True)
    elif user_order in MENU:
        if check_resources(user_order):
            money_paid = process_coins()
            if check_transaction(money_paid, MENU[user_order]["cost"]):
                make_coffee(user_order)
        else:
            report(False)
    else:
        print("Please select a valid option")
