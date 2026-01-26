# This isn't part of Codemy.com course

"""
🔥 Mini‑Challenge: Countdown Timer
Write a script that:
1. 	Starts with a number the user enters
2. 	Uses a while loop to count down to zero
3. 	Prints each number as it counts
4. 	Ends by printing "Blast off" when the loop finishes

Example behavior (if user enters 5):
"""
# Code written by Jose "Joe" Ruiz, for my personal use

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

counter = int(input("Enter a number: "))

while counter >= 0:
    print(counter)
    counter -= 1
    
print("\nBlast Off!")

        