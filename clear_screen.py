# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# clear_screen.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# ===============================================

# Import module

import os  # allows us to clear the screen

# Helper function clears the terminal window.
# It checks which operating system you're on:
# - "nt" means Windows -> use the "cls" command
# - otherwise (Mac/Linux) -> use the "clear" command
# This keeps the menu clean every time it refreshes.

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# --------------------------------------------------

clear_screen()  # clears the screen

print("Hello, World!!")