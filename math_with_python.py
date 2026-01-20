# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# math_with_python.py

# Code written by Jose "Joe" Ruiz

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

#    +   (addition)        -> Adds two numbers together.
#    -   (subtraction)     -> Subtracts the right number from the left.
#    *   (multiplication)  -> Multiplies two numbers.
#    /   (division)        -> Divides the left number by the right and returns a float.
#    **  (exponentiation)  -> Raises a number to the power of another.
#    %   (modulus)         -> Returns the remainder after division.
#    //  (floor division)  -> Divides and rounds down to the nearest whole number.

# Examples

# 3 + 2    -> 5
# 5 - 1    -> 4
# 4 * 3    -> 12
# 8 / 2    -> 4.0
# 2 ** 3   -> 8
# 10 % 3   -> 1
# 10 // 3  -> 3

# ORDER OF OPERATIONS (PEMDAS)

"""
1. Parentheses ()
    - Parentheses always run first.
    - They force Python to evaluate something
    - before everything else.
    - Example:
    - (2 + 3) * 4  -> 20
    - Without parentheses:
    - 2 + 3 * 4  -> 14

2. Exponents **
    - Anything involving powers happens next.
    - Example:
    - 2 + 3 ** 2  ->  2 + 9 -> 11 

3. Multiplication, Division, Floor Division, Modulus
    - These all share the same priority level:
    - *   multiplication
    - /   division
    - //  floor division
    - %   modulus(remainder)

Python evaluates them left to right.
    - Example:
    - 10 / 2 * 3  -> (10 / 2) * 3  -> 5 * 3  -> 15

4. Addition and Subtraction
    - These are the last operations evaluated, also left to right.
    - Example:
    - 10 - 2 + 5  -> (10 - 2) + 5  -> 8 + 5  -> 13
"""
# ========================================================

# Full Priority List (Top -> Bottom)

# 1. Parentheses ()
# 2. Exponents   **
# 3. Multiplication  *
# 4. Division        /
# 5. Floor Division  //
# 6. Modulus         %
# 7. Addition        +
# 8. Subtraction     -

# (3 - 6 all share the same level and go left-to-right.)

# Python doesn't "guess" what you meant - it follows these rules strictly.
# If you want a different order, you must use parentheses.

# =========================================================

print(3 + 2)   
print(3 - 2)   
print(5 * 5)   
print(10 / 2)  
print(2 ** 3)  

num1 = 3
num2 = 5
num3 = num1 + num2
print(num3)

print(3 + 1 * 4)  # multiplication is first, then the addition

