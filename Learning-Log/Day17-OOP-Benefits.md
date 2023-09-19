# Day 17 of 100 Days of Python on Udemy with Angela Yu

## Topics Covered:

- Object Oriented Programming (OOP) and the benefits of OOP

## Project:

Quiz Game


### Using PascalCase for Classes

```python
# Make sure to capitalize the first letter of each word in the class name 
class MyClass:
    pass

```

### Parameters in Classes for Initialization
You can set arguments and allow for parameters that can be set when the class is initialized. 


```python
# Parameters in Classes for Initialization
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela")
user_2 = User("002", "jack")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
```