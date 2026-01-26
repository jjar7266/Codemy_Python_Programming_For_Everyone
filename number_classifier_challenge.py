# This isn't part of Codemy.com course

"""
🔥 Mini‑Challenge: “Number Classifier”
Write a script that:
1. 	Asks the user for a number
2. 	Converts it to an integer
3. 	Uses if / elif / else to classify the number into one of these categories:
• 	Negative
• 	Zero
• 	Positive but less than 10
• 	10 exactly
• 	Greater than 10
Your output should be a single, clean print statement for each case.
"""
# Code written by Jose "Joe" Ruiz, for my personal use

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

num = int(input("Enter a number: "))

if num < 0:
    print(f"{num} is a Negative numbber")
elif num == 0:
    print(f"{num} is a Zero")
elif 0 < num < 10:
    print(f"{num} is Positive but less than 10")
elif num == 10:
    print(f"{num} is exactly 10!!")
else:
    print(f"{num} is greater than 10")

