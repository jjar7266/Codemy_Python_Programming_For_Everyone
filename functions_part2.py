# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# functions_part2.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# Create the function
def namer(first_name):
    count = 0
    for _ in first_name:
        count += 1

    return(count)

# Call the function
letter_count = namer("April")

print(f"There are {letter_count} letters in that name")


