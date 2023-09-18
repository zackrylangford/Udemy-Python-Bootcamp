# Day 12 Python Udemy 100 days of code

## Scope

### Local Scope

```python

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) # NameError: name 'potion_strength' is not defined

```

Understanding local scope

* Local scope is created when a function is called, and immediately destroyed when the function is finished.
* A variable created in a function is only accessible in that function.
* A function can access variables defined in the global scope.
* A function's local scope cannot access variables in any other local scope.

### Global Scope

```python

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)

```

Understanding global scope

* Global scope is created when a program starts, and immediately destroyed when the program ends.
* A variable created in the global scope is accessible to all functions.
* A function's local scope cannot access variables in any other local scope.
* A function's local scope can access global variables.
* Code in the global scope cannot use any local variables.


### Modifying Global Scope

```python

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

```

### Does Python have Block Scope?

```python

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

```

Python does not have block scope. Variables created inside a block of code can be accessed outside the block of code.

If you create a variable inside a block of code, that variable is accessible within the block of code (local scope), outside the block of code (global scope), and in any block of code nested within the block of code (nested scope).

### Naming Global Constants

```python

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

```

Use all capital letters to name a global constant so that you know it should not be changed.