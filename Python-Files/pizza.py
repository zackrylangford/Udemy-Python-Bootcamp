pizza_size = input("What size pizza would you like? (S, M, L)")
additional_pep = input("Would you like extra pepperoni?")
extra_cheese = input("Would you like extra cheese?")

bill = 0

if pizza_size == "S":
    bill+=15
elif pizza_size == "M":
    bill+=20
elif pizza_size == "L":
    bill+=25

if additional_pep == "Y":
    if pizza_size == "S":
        bill+=2
    else:
        bill+=3
if extra_cheese == "Y":
    bill+=1

print(f"Your final bill is ${bill}")
