# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# boolean.py

# Instructor briefly went over this topic not really any code.

# I will put some thought into this:

# Code written by Jose "Joe" Ruiz, for my personal use

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# ========================================================

# What are Booleans?

# Booleans are either True or False

# Examples

is_logged_in = True
has_pizza = False

print(is_logged_in)
print(has_pizza)

# Boolean expressions

print(5 > 3)     # True
print(10 == 2)   # False
print("Joe" != "John")  # True

# Booleans in conditions

age = 20
can_vote = age >= 18

if can_vote:
    print("You can vode!")
else:
    print("Not old enough.")

# Combining conditions

is_admin = True
is_active = False

print(is_admin and is_active)  # False
print(is_admin or is_active)   # True
print(not is_admin)            # False

# Python treats many values as True/False automatically

print(bool(0))          # False
print(bool(10))         # True
print(bool(""))         # False
print(bool("Joe"))      # True
print(bool([1, 2, 3]))  # True

# ===============================================

# A practical example

username = "Joe"
password = "1234"

is_correct_user = username == "Joe"
is_correct_pass = password == "1234"

if is_correct_user and is_correct_pass:
    print("Login successful")
else:
    print("Access denied")


