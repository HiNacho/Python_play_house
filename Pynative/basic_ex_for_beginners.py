# Question 1
# calculate the multiplication and sum of two numbers
"""
Given two integer numbers, write a Python program to return
their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""

def multiply():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2

# print(multiply())


def mult():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    product = a * b
    return product if  product <= 1000 else a + b

# print(mult())

# Question 2
" Print the Sum of a Current Number and a Previous number"
"""
Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
"""


def ranger():
   # n = int(input("Enter any number: "))
    for i in range(n):
        current_number = i + 1
        prev_number = 1
        print(f"Current number: {current_number} previous number: {prev_number} sum: {current_number + prev_number}")
# ranger()

def print_num(n):
    for current in range(n):
        prev = 0
        print(f"current number: {current} previous number : {prev} sum {current + prev}")
        prev = current
# n = int(input("Enter any number: "))
# print_num(n)

# Question 3
"Print characters present at an even index number"
"""
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
"""
def strip_word(word):
    new_word = word[::2]
    return new_word
# word = input("Enter a word: ")
# print(strip_word(word))

# Question 4
"Remove first n characters from a string"
"""
Write a Python code to remove characters from a string from 0 to n and return a new string.
"""
def word_trim(word, num_chars):
    trimmed_word = word[num_chars::]
    return trimmed_word
# word = input("Enter a word: ")
# um_chars = int(input("Enter number of characters: "))
# print(word_trim(word, num_chars))

# Question 5
"Check if the first and last numbers of a list are the same"
"""
Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
"""

list_1 = [10,20,30,10]
if list_1[0] == list_1[-1]:
    print(True)
else:
    print(False)
# Process finished with exit code 0


# Day 2
# Question 6
"""
Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5
"""

list1 = [10,15,3,7,8,5]

new_list = list(filter(lambda x: x % 5 == 0, list1))
# print(new_list)

# question 7
"""
Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string
"""

str_x = "Emma is a good developer. Emma is a writer"

count_str = str_x.count("Emma")
# print(f"there are {count_str} occurrences of Emma in the given string")

# question 8
# Print the following pattern

for i in range(1,5):
    for j in range(i):
        print(i, end = " ")
    print("")


for i in range(1,5):
    for j in range(i,5):
        print(i, end = " ")
    print("")

# Question 9
# Print multiplication table from 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end = " ")
    print(" ")