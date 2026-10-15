#1. Print all even numbers from 1 to 100
def even_numbers():
    print("Even numbers from 1 to 100 are:")
    for i in range(2,101):
        if i%2 == 0:
            print(i)
even_numbers()

#2. Sum of digits of a number (example input: 1234 → output: 10)
def sum_of_digits():
    num = int(input("Enter a number: "))
    total=0
    while num > 0:
        total = total + num % 10
        num  = num// 10
    print("Sum of digits is:", total)
sum_of_digits()

#3.Reverse a Number
def reverse_num():
    num = int(input("Enter a number: "))
    rev = 0 
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    print("Reverse of the number is:", rev)
reverse_num()

#4. Check if a number is palindrome or not
def is_palindrome():
    num = int(input("Enter a number: "))
    original_num = num
    rev = 0 
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    if original_num == rev:
        print(original_num, "is a palindrome.")
    else:
        print(original_num, "is not a palindrome.")
is_palindrome()
 #5. Count Digit 3
def count_digit_three():
    count = 0
    for i in range(1, 101):
        count += str(i).count('3')
    print("Digit 3 appears", count, "times from 1 to 100.")
count_digit_three()