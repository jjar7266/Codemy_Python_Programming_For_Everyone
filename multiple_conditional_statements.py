# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# multiple_conditional_statements.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# DATA TYPES
# Multiple Conditional Statements - and/or

num = 3

if (num > 10) and (num < 100):  # and (they both have to be True)
                           # or (only one has to be True)

    print("Your number is greater that 10 but less than 100")

else:
    print("Nope!")

# Real Logic Version

if 10 < num < 100:
    print("Your number is greater than 10 but less than 100")
else:
    print("Nope!")

    
