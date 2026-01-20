# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# variables.py

# Code written by Jose "Joe" Ruiz

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# variables

first_name = "Jose"
state      = "Florida"
city       = "Coral Springs"
zip_code   = "33065"
age        = 56

# Print Hello World

clear_screen()
print("Hello, World!")

print(first_name)
print(city)

