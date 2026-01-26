# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# for_loops.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# For Loops

"""
names = ["John", "Bob", "April"]

for name in names:
    print(name)
"""

fav_pizza = {"John": "Pepperoni",
             "Bob": "Mushroom",
             "April": "Veggie"
            }

for key, value in fav_pizza.items():
    print(f"{key}'s favorite pizza is {value}.")

# ==================================================

# Examples

for name in fav_pizza:
    print(name)

# Loop over values only

for pizza in fav_pizza.values():
    print(pizza)






