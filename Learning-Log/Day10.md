# Functions with Outputs

```python
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""


print(format_name("angela", "YU"))
```

## Multiple return values

```python
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

```

## Docstrings

```python
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

```

Docstrings allow us to add a description to the function. It is good practice to add docstrings to our functions. That way it will show up in a hover in VS Code when you hover over the function name.

## Printing vs Returning

```python
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
    
```

Why return instead of print? Because we want to use the function in other places. If we print, we can't use the function in other places.