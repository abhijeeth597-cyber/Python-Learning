""" Conditionals are used to perform different actions based on different conditions. 
In Python, we use if, elif, and else statements to create conditional statements.
Python evaluates conditions to True or False, then executes the corresponding code block. 
The beauty? You can chain multiple decisions with elif (else-if)."""


"""Syntax  Rules:
• if statement: if condition: followed by indented block
• elif: Check additional conditions if previous ones fail
• else: Catch-all for when no conditions match
Comparison operators: ==, !=, <, >, <=, >=
Logical operators: and, or, not
Truthy/Falsy: Empty values (0, "", [], {}, None) are False; others are True
• Ternary operator: value = x if condition else y """
#Example 1: Basic if\elif\else statement
name = "Abhijeeth"
score = 82

if score >= 90 :
    grade = "A"
elif score >= 80 :
    grade = "B"
elif score >=70 :
    grade = "C"
elif score >= 60 :
    grade = "D"
else :
    grade = "F"
   
print(f"{name} you scored {score} and your grade is {grade}")

#Example 2 : Complex conditions with and / or
age = 25
income = 25000
has_job = True
if age>=21 and income >= 25000:
    print("You are eligible for the loan.")
elif age>=21 or has_job:
    print(" Conditional approval: You need to provide additional documents.")
else:
    print("Sorry, you do not meet the eligibility criteria for the loan/Loan Disapproved.")
    
     # Quick practice: Write a function that returns Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for multiples of both.
def fizzbuzz(n):
        if n % 15 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return n
        print(fizzbuzz(15))  # Output: FizzBuzz
