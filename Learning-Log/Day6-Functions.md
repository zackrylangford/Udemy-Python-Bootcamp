# Day 6 

## Functions

Today we are talking about functions. Functions are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you've defined in a function, you call the name of the function responsible for it. If you need to perform that task multiple times throughout your program, you don't need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function. You'll find that using functions makes your programs easier to write, read, test, and fix.

## Python built-in functions

Useful link to the [Python built-in functions](https://docs.python.org/3/library/functions.html)


## Creating our own functions

### Defining a function

Here's a simple function named greet_user() that prints a greeting:

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
```
To call a function you write the name of the function, followed by any necessary information in parentheses, as shown here:

```python
greet_user()
```

Three steps to defining functions: 

1. Use the keyword def to inform Python that you're defining a function.
2. Follow the function name with a set of parentheses and a colon.
3. Add an indented block of code below the function definition.

### Benefits of using functions

- Organizing your code
- Avoiding repetition
- Making your code easier to understand
- Testing individual parts of your program
- Extending your program's capabilities by calling it from other programs


### First challenge - reeborgs world

[Reeborgs world](https://reeborg.ca/index_en.html) is a website where you can learn how to code in Python. It's a fun way to learn the basics of Python.

We played around with functions to move the robot around the world.

Remember that I should always look for ways to shorten the code and make it cleaner. Use loops, functions, etc. to not repeat yourself. DRY - Don't repeat yourself.

### Indentation

Indentation is extremely important in Python. It is used to determine the scope of the function. 

#### Tabs vs spaces

The Python style guide recommends using 4 spaces per indentation level.

#### IndentationError

If you get an IndentationError, check that you are using the same number of spaces for indentation throughout your code.

### While loops

We then discussed and went through while loops

while loops will continue to execute a block of code while some condition remains True.

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

so: 

while something_is_true:
    do something

You can check conditions by using negation phrasing as well. So: 

while not something_is_true:
    do something


* for loops are better if you know how many times you want to loop through something

* while loops are better if you don't know how many times you want to loop through something

### infinite loops

An infinite loop occurs when a loop never ends. If there's no way for the condition to become False, the loop will never stop running. You can stop an infinite loop by pressing CTRL-C, or by closing the window displaying the output.
