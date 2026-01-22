# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# intro_data_types.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# DATA TYPES
# ===========================

# Strings 

# Numbers - Floats - Ints

# Booleans

# Lists - are mutable - they can be changed

# Tuples - are immutable - they can't be changed

# Dictionaries - can be indexed by using key: value pair

first_name = "Jose"  # string

age        = 55      # int
GPA        = 3.90    # float

lie = True  # Boolean (True or False)

first_names = ["Tom", "Dick", "Harry", "Sue", "Peggy"]  # [list] 

last_names  = ("Ferry", "Allen", "Sanchez", "Ruiz")     # (Tuple)

dict = {
    "Tom": "Ferry",
    "Dick": "Allen",
    "Harry": "Sanchez",
    "Sue": "Ruiz"
}

fav_pizza = {
    "Tom": "Pepperoni",
    "Tim": "Cheese",
    "Joe": "Deluxe",
    "Sue": "Veggie"
}

# Examples 
clear_screen()

print(first_names[3])  # prints out "Sue"

print(first_names)

print(fav_pizza["Joe"])




