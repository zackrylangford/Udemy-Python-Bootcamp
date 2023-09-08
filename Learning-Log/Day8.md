## Functions

Today we worked on functions. We learned how to define functions, pass information to them, and return information from them. We also learned about positional and keyword arguments, and how to use default values to make functions more flexible.

### Defining a function

We defined a function by using the def keyword followed by the name of the function and a set of parentheses. We then indented the code that we wanted to be part of the function. We then called the function by using the name of the function followed by a set of parentheses.

### Parameters

We defined parameters by putting them in the parentheses when we defined the function. We then passed arguments to the function when we called it.

Example:

```python
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
```


### Arguments

We passed arguments to the function by putting them in the parentheses when we called the function. We then used the arguments in the function.

Example for where arguments are passed to the function:
```python

# The argument is passed to the function here in the parantheses
greet_user('jesse')
```

### Positional Arguments

You need to make sure that the arguments are in the same order as the parameters when you pass them to the function. This is called a positional argument.

You can use keyword arguments to make sure that the arguments are in the correct order.

example:

```python
# Use keyword arguments to make sure the arguments are in the correct order
greet_user(username='jesse')
```


### Function with multiple parameters

We defined a function with multiple parameters by putting them in the parentheses when we defined the function. We then passed arguments to the function when we called it.

Example:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

describe_pet('dog', 'willie')
```
