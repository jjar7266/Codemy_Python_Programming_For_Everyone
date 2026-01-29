# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# classes.py - Intro to Classes

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

# Classes

class Square:
    
    def __init__(self, side_length):
        # Define Square side length
        self.side_length = side_length

    # Get the area of our square
    def area(self):
        return(self.side_length * self.side_length)
    
    # Get the perimeter
    def perimeter(self):
        return(self.side_length * 4)
    
    # Creating a litte report
    def report(self):
        print(f'Side Length: {self.side_length}\n')
        print(f'Area: {self.area()}\n')
        print(f'Perimeter: {self.perimeter()}')
        
# Instantiate our class

my_square = Square(10)
my_square.report()

# ==========================================================

# Extra Examples

# Example 1 - Create multiple squares

s1 = Square(5)
s2 = Square(12)

print(s1.area())
print(s2.perimeter())

# Example 2 - Using return values directly

sq = Square(7)
area_value = sq.area()
perimeter_value = sq.perimeter()

print(f"Area: {area_value}, Perimeter: {perimeter_value}")

# Example 3 - Adding a __str__ method (optional enhancement)

"""
class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        
    def area(self):
        return self.side_length ** 2
        
    def perimeter(self):
        return self.side_length * 4
        
    def __str__(self):
        return f"Square(side_length={self.side_length})"

sq = Square(9)
print(sq)  # Uses __str__
"""

# Example 4 - Changing attributes after creation

sq = Square(10)
print(sq.area())

sq.side_length = 20
print(sq.area())  # Updated value

# SUMMARY
# - Created a Square class with:
#       __init__() to store side_length
#       area() to compute area
#       perimeter() to compute perimeter
#       report() to print a formatted summary
#
# - Learned how to instantiate a class:
#       my_square = Square(10)
#
# - Practiced calling methods on objects:
#       my_square.area()
#       my_square.perimeter()
#
# - Explored return values vs printing inside methods
#
# - Added extra examples:
#       multiple objects
#       storing return values
#       optional __str__ method
#       modifying attributes after creation
#
# - This lesson introduces the core OOP pattern:
#       Classes define data + behavior
#       Objects are instances of those classes