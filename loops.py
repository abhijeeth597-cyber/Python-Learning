"""Loops are assembly lines that repeat actions. A for loop processes items one by one (like checking each apple in a basket). 
A while loop keeps going until told to stop (like stirring soup until it boils)."""
"""Syntax Rules: .For Loop:for item in sequence: iterates through collections
.While Loop: while condition: continues until condition is False
.Break: exits the loop immediately
.Continue: skips to the next iteration
.pass: placeholder for future code(does nothing)
.else clause : runs after loop completes normally (no break)"""


#Example 1 : for loop with range and enumerate
# simple range loop
for i in range (3):
 print (f"Count: {i}")
 #output: Count: 0, Count: 1, Count: 2
 # Enumerate for index + value
 fruits = ["apple", "banana", "cherry"]
 for index, fruit in enumerate(fruits):
   print(f"{index}: {fruit}")
   #output: 0:apple, 1:banana, 2:cherry
#One liner: range()generates numbers, enumerate() gives index+value pairs, zip() pairs items from multiple lists
#Example 2 : while loop with break and continue
attempts = 0
password = "secret123"
while attempts < 3:
  guess = input("Enter password: ")
  attempts += 1
  if guess == password:
        print("Access granted!")
        break
  elif attempts == 3:
        print("Too many attempts. Access denied.")
        continue
  else:
        print("Incorrect password. Account locked.")

#Example 3 : List comprehension (loop shorthand)
#Traditional loop to create a list of squares
squares = []
for x in range(10):
    squares.append(x**2)
#List comprehension version
squares = [x**2 for x in range(10)]
print (squares)
#with condition
even_squares = [ x for x in range(10) if x % 2 == 0]
print(even_squares)
# Exercise : Print a tringle pattern of stars
for i in range (1,6):
    print("*" * i)
    
