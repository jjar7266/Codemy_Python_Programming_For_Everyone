# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# FizzBuzz.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

"""
Print out all the numbers between 1 - 100.
If a number is divisible by 3 print out Fizz,
If it's divisible by 5 print out Buzz, 
if it's divisible by 3 and 5 print out FizzBuzz !!,
otherwise just print out the number.
"""

# FizzBuzz !!

# 1. Loop through numbers
# 2. Check if divisible by both
# 3. Check if divisible by 3
# 4. Check if divisible by 5
# 5. Otherwise print the number

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()
"""

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} = FizzBuzz !!")
    elif num % 3 == 0:
        print(f"{num} = Fizz")
    elif num % 5 == 0:
        print(f"{num} = Buzz")
    else:
        print(num)
"""

# Instructors Solution

count = 1
while (count <= 100):
    if (count % 3 == 0) and (count % 5 == 0):
        print(f"{count}. FIZZBUZZ !!!")
    elif (count % 3 == 0):
        print(f"{count}. FIZZ !!!")
    elif (count % 5 == 0):
        print(f"{count}. BUZZ !!!")
    else:
        print(f"{count}.")
    
    count += 1

# Extra Credit

# Try with less lines of code
# Keep separate counters for each



