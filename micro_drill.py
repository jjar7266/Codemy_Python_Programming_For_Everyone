# This isn't part of Codemy.com course

"""
🔥 Micro‑Drill: Loop Through a String
Write a for loop that prints each character in the word "Python" on its own line.

Expected output:
P
y
t
h
o
n
"""
# Code written by Jose "Joe" Ruiz, for my personal use

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

word = "Python"

for letter in word:
    print(letter)