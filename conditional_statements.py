# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# conditional_statements.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# DATA TYPES
# Conditional Statements - Logic! (If/Else/Elif)

# If (Something):
#    Do Something
# Else:
#    Do Something Else

num = 10

if num > 10:
    print("Your number is greater than 10")

elif num == 10:
    print("Your number EQUALS TEN!!")

else:
    print("Your number is not greater than 10")

"""
TEACHING NOTES:
---------------
This script demonstrates Python's conditional logic flow.

1. Python evaluates conditions from top to bottom.
2. Only the first True condition runs.
3. 'elif' allows multiple checks without nesting.
4. 'else' is the fallback when no conditions match.
5. Conditions use comparison operators:
   >, <, >=, <=, ==, !=

This pattern is the foundation for decision-making in Python.
"""


