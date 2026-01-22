# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# tuples.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# DATA Types
# Tuples

tuple_1 = ("John", "Joe", "April")

tuple_2 = ("Tammy", )

tuple_3 = tuple_1 + tuple_2

tuple_4 = tuple_1[0:2]

print("Combined tuple:", tuple_3)

print("Original tuple:", tuple_1)

print("Slice of tuple_1:", tuple_4)

# Tuples are immutable:

# tuple_1[0] = "Kurt"  # This will raise a TypeError

# ============================================================

# Example: Convert between list and tuple

as_list = list(tuple_1)
as_list.append("NewName")
print("Modified list:", as_list)

back_to_tuple = tuple(as_list)
print("Back to tuple:", back_to_tuple)

# =============================================================

# tuple unpacking

a, b, c, = tuple_1
print(a, b, c)

# ===============================================================

# single-item tuple pitfall

not_a_tuple = ("Tammy")
print(type(not_a_tuple))  # str

yes_a_tuple = ("Tammy",)
print(type(yes_a_tuple))  # tuple






