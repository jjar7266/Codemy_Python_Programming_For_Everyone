# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# comparison_operators.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# DATA TYPES
# Comparison Operators
# == , !=, <, >, <=, >=


print("9 == 10:", 9 == 10)

print("9 != 10:", 9 != 10)

print("12 < 10:", 12 < 10)

print("12 > 10:", 12 > 10)

print("12 >= 10:", 12 >= 10)

print("9 >= 10:", 9 >= 10)

print('"John" == "john":', "John" == "john")

print("[1, 2, 3] == [1, 2, 3, 3]:", [1, 2, 3] == [1, 2, 3, 3])

# ================================================================

result = 5 < 10
print("Result is:", result, "and its type is:", type(result))

print("John".lower() == "john".lower())  # True

# ================================================================

print([1, 2, 3] == [1, 2, 3])     # True
print([1, 2, 3] < [1, 2, 4])      # True
print([1, 2, 3] > [1, 2, 2])      # True

# ===============================================================

print(5 < 10 < 20)   # True
print(5 < 10 > 3)    # True
