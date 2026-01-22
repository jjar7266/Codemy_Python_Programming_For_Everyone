# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# string_manipulation.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

name = "my name is Bad MoFo"

# .upper()
# .lower()
# .capitalize()
# .title()
# .swapcase()
# len() - length


# uncomment to print

# print(name.upper())  # prints in all uppercase
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.swapcase())
# print(len(name))  # what's the length of name

print(name[11:])  # index slicing (starts at 0)

print(name.split(" ")[3])  # splits using the space character