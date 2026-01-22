# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# floats_ints.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# DATA TYPES

# Numbers: Floats and Ints

num_1 = 10       # int
num_2 = 3.00     # float

num_3 = 5        # int
num_4 = 7.45845  # float

# Examples

print(num_1 / num_2)

print(int(num_2))

print(int(num_1 / num_2))

print(float(num_3))

print(round(num_4, 2))

