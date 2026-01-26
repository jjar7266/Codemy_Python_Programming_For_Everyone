# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# functions.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# Create the function
def namer(first_name):
    print(f"Hello there {first_name} !")

# Call the function
namer("John")

def adder(num_1, num_2):
    print(num_1 + num_2)

adder(4, 1)