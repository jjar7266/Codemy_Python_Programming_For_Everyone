# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# hello2.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

import namer_module
import os


result = namer_module.namer("John")
print(result)

# Example 1 - Basic import and call
"""
import namer_module

print(namer_module.namer("Alice"))
"""
# Example 2 - Assigning the return value

"""
import namer_module

greeting = namer_module.namer("Bob)
print(greeting)
"""

# Example 3 - Using clear_screen + module import

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()
print(namer_module.namer("Charlie"))

# SUMMARY
# - Created a custom module: namer_module.py
# - Defined a function that RETURNS a string (not prints)
# - Imported the module into hello2.py using: import namer_module
# - Called the function with: namer_module.namer("Name")
# - Used clear_screen() for a clean terminal output
# - Added a __main__ test block inside the module for direct execution
# - Practiced multiple import patterns and return-value handling




