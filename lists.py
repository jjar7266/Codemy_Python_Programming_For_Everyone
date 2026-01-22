# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# lists.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# DATA TYPES
# Lists

my_name = "Tammy"
nums = [1, 2, 3, 4, 5]
first_names = ["John", "Bob", "April", 41, my_name, nums]

print("First item:", first_names[0])

print("41 + 10 =", first_names[3] + 10)

print("Full list:", first_names)

print("Third item inside nested list:", first_names[5][2])

# Changed Item
first_names[0] = "Kurt"

# Append Item
first_names.append("Joe")

# Delete Item
del(first_names[2])

# pop Item
removed = first_names.pop(2)
print("Removed with pop():", removed)
print("List after pop:", first_names)

print("Last item:", first_names[-1])

# Example of list concatenation
combined = first_names + nums
print("Combined list:", combined)

# Example of looping over lists
for item in first_names:
    print("Item:", item)

