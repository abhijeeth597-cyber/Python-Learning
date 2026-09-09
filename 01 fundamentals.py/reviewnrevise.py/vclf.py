###V= variables; '''Variables are containers for storing data values
#C= Conditionals '''Conditionals are used to perform different actions based on different conditions.    
#L= Loops '''Loops are assembly lines that repeat actions. A for loop processes items one by one (like checking each apple in a basket).
#F = Functions'''Functions are reusable blocks of code that perform a specific task. They help break down complex problems into smaller, manageable pieces.###

#Exercises: 1.) Multiplication table generator
# 1. Multiplication Table
def multiplication_table (n, upto = 10):
    for i in range (1, upto+1):
        print(f"{n} * {i} = {n * i}")
multiplication_table(4)
num = int(input ("Enter a number to generate its multiplication table: "))
multiplication_table(num)   

#Exercise : 2.) Even/odd checker
def even_odd_checker(num):
    if num%2 == 0 :
        print("even")
    else:
        print("odd")
even_odd_checker(10)
number = int(input("Enter a number to check if it's even or odd: "))
even_odd_checker(number)
 
#Exercise : 3.) Factorial calculator
def factorial(num):
    if num <0 :
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range (1, num + 1):
        result *= i
    return result
print(factorial(5))

#Exercise : 4.) Fibonacci sequence generator
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
