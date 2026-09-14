#1. Print all even numbers from 1 to 100


from itertools import count


def even_numbers():
    print("Even numbers from 1 to 100:")
    for i in range(1, 101):

        if i % 2 == 0:

            print(i)

even_numbers()

#2.Sum of digits of a number (example input: 1234 → output: 10)
def sum_of_digits():
    num = int(input("Enter a number: "))
    total = 0
    while num>0:
        total = total + num % 10
        num = num//10
    print("Sum of digits:", total)

sum_of_digits()

#3.Reverse a number (example input: 1234 → output: 4321)
def reverse_number():
    num = int(input("Enter a number: "))
    reversed_num = 0
    while num > 0 :
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    print("Reversed number:", reversed_num)

reverse_number()

#4. Check if a number is palindrome (121 → True, 123 → False)
def is_palindrome():
    num = int(input("Enter a number: "))
    original_num = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10 
    if original_num == reversed_num:
        print(f"{original_num} is a palindrome.")
    else:
        print(f"{original_num} is not a palindrome.")

is_palindrome()

#5.Count how many times digit 3 appears in numbers 1 to 100
def count_digit_three():
    count = 0
    for i in range(1, 101):
        count += str(i).count('3')
    print("Digit 3 appears", count, "times from 1 to 100.")
    
count_digit_three()

#6.  Reverse a string without using [::-1]
def reverse_string():
    string = input("Enter a string:")
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    print("Reversed string:", reversed_str)
reverse_string()

#7.  Count vowels in a string
def vowel_count(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = "hello world"

print("Number of vowels in the string:", vowel_count(s))  