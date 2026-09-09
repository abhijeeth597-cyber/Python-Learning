"""Functions are reusable recipe of cards. Instead of rewriting the same code yu give it and call it whatever you needed.
Parameters are the ingredients you pass to the function, and the return value is the final dish it gives back."""

"""Syntax Rules:  .Define function: def function_name(parameters): followed by indented block
.Return value: use return keyword to send back a result
.Default parameters: def func(param=default_value): allows optional arguments
eg. def greet(name="Guest"):
    return f"Hello, {name}!"
.Variable arguments: *args for non-keyword(tuple), **kwargs for keyword arguments(dictionaries)
.Scope: Variables inside functions are local unless declared global.
.Lambda: lambda x : x*2 is an anonymous function for simple operations.
.Docstrings: Triple quotes '''Docstring''' for function documentation.  
"""
# Example 1 : Basic function with paramters and return value
# calculate the area of a circle
import math
def calculate_area(radius):
    return math.pi*radius**2
print(calculate_area(5))
# Example 2 : basic functions with parameters and default values
def calculate_total()
   