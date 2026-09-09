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
from turtle import filling
def calculate_area(radius):
    return math.pi*radius**2
print(calculate_area(5))
# Example 2 : basic functions with parameters and default values
def calculate_total(price,discount):
 tax_rate = 0.05
 subtotal = price + (price * tax_rate)
 total = subtotal - (subtotal * discount)
 return total
print(calculate_total(100,0.10))
#example 2 : args and kwargs (flexible parameters
#args = multiple values(tuple)
#kwargs = keyword/named arguments (dictionaries)
def make_sandwich(bread,*fillings,**extras):
   print("bread",bread)
   print("fillings",fillings)
   print("extras",extras)
   print(f"Bread: {bread}")
   print("Filling:",",".join(fillings))
   for key,value in extras.items():
         print(f"{key}: {value}")
make_sandwich("whole wheat","ham","cheese",sauce="mayo",toasted=True)

#example 3: Lambda and higher order functions
#Lambda function for simple operations
square = lambda x : x**2
print(square(5))
#using with built in functions like map and filter
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2,numbers))
evens = list(filter(lambda x : x%2 ==0,numbers))
print(f'Squared= {squared}')
print(f'evens = {evens}')