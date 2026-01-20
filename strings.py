# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# strings.py

# Code written by Jose "Joe" Ruiz

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# you can use double quotes or single quotes.
# Single quotes outside, double quotes inside. or vice versa

# or use the escape character back slash,
# used to ignore the character following after

yell = 'My Mom yelled: "CLEAN YOUR ROOM!"'  # look at the quotation marks

yelled = "My Mom yelled: \"CLEAN YOUR ROOM!\""  # escape character used

yell_new_line = "My Mom yelled: \n'CLEAN YOUR ROOM'"  # \n is a new line character

mom = "Laura"

f_string_ex = f"My mom {mom} yelled: 'CLEAN YOUR ROOM'"  # f-string used

clear_screen()
print(yell)
print(yelled)
print(yell_new_line)
print(f_string_ex)

