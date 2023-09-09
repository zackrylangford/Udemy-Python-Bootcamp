# programming_dictionary = {
#         "Bug": "An error in a program that prevents the program from running as expected.",
#         "Function": "A piece of code that you can easily call over and over again.",
# }

# # Retrieving items from dictionary.
# print(programming_dictionary["Bug"])

# # Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# # Create an empty dictionary.
# empty_dictionary = {}

# empty_dictionary["Key"] = "Value"

# print(empty_dictionary)

# # Wipe an existing dictionary.

# programming_dictionary = {}
# print(programming_dictionary)

# # Edit an item in a dictionary.

# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# # Loop through a dictionary.

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# # Nesting

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# # Nesting a List in a Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# # Nesting Dictionary in a Dictionary

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# # Nesting Dictionary in a List



travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    entry = {"country": country, "visits": visits, "cities": cities}
    travel_log.append(entry)







#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
