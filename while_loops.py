# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# while_loops.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# While Loops

counter = 0

while counter <= 10:
    print(f"The Count Is: {counter}")
    counter += 1