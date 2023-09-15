# Coffee machine

# Initial resource values


resources = [
    {"water": 300, "type": "ml"},
    {"milk": 200, 'type': "ml"},
    {"coffee": 100, "type": "g"},
    {"money": 0, "type": "$"},
]

user_order = input("What would you like? (espresso/latte/cappuccino): ")

if user_order == "off":
    print("Shutting down")
elif user_order == "report":
    for resource in resources:
        for name, amount in resource.items():
            if name != "type":
                print(f"{name.capitalize()}: {amount}{resource['type']}")
else:
    print("Please select a valid option")

