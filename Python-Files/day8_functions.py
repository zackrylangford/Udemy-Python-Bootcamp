def greet(name):
    print(f"Hello, {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")


greet("zack")


def greet_with_name(name):
    print(f"Hello, {name}")


greet_with_name("Zack")



def greet_with_multiple(n1, n2):
    print(f"Hello, {n1}. Hello, {n2}")

greet_with_multiple("zack", "dave")

def location(name, location):
    print(f"Hello, {name}. What is the weather like in {location}?")


location("Zack", "Marshall")


# With Keyword arguments

def greet_with_kw(a, b, c):
    print(f"Hello, {a}. How is {b}? What about {c}?")

greet_with_kw(b="Marshall", a="Zack", c="Dave")

