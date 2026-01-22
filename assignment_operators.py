# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# assignment_operators.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# Assignment Operators

# = , with math
# +=, -=, *=, **=, %=

age = 46

#age += 1  # commented out for now (great tool to use for a counter in loops)

age -= 1  # you can change the assignment operator

print(age)

# =================================================

# Demonstrating assignment operators

x = 10

x += 5   # 15
x -= 3   # 12
x *= 2   # 24
x **= 2  # 576
x %= 10  # 6

print("Final value of x:", x)

# ===================================================

age = 45  # Before
print("Starting age:", age)

age -= 1  # After
print("After -= 1:", age)

# ===================================================

# Example of a loop counter:

counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1

# ===================================================

# Quick Reference:

# a += b  ->  a = a + b
# a -= b  ->  a = a - b
# a *= b  ->  a = a * b
# a /= b  ->  a = a / b
# a ** b  ->  a = a ** b
# a %= b  ->  a = a % b

# ====================================================

# assignment operators also work with strings

# Example

name = "Tommy"
name += " Jones"

print(name)








