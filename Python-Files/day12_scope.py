# ################### Scope ####################

# enemies = 1

# def increase_enemies(total):
#   total += 5
#   print(total)
#   print(f"enemies inside function: {enemies}")
#   return total

# enemies = increase_enemies(enemies)
# print(f"enemies outside function: {enemies}")

# Modifying Global Scope

import random

game_level = 8

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    else: 
        new_enemy = random.choice(enemies)

    print(new_enemy)

create_enemy()
