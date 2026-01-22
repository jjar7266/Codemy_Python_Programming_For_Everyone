# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# dictionaries.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

# Import module

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

# DATA Types
# Dictionaries - Key/Value pairs

fav_pizza = {
    "John": "Pepperoni",
    "Joe": "Mushroom",
    "April": "Veggie",
}

# Delete Item
# del(fav_pizza["John"])

# Change an Item
fav_pizza["John"] = "Green Peppers"

# Add an Item
fav_pizza.update({"Steve": "Onion"})

print("Full dictionary: ", fav_pizza)
print("Steves's favorite:", fav_pizza["Steve"])

# =====================================================

# Demonstrate safe access with .get()

print("Does Bob exist?", fav_pizza.get("Bob", "Not found"))

# ======================================================

# Example: Loop through a dictionary

for name, pizza in fav_pizza.items():
    print(name, "Likes", pizza)

# ========================================================

# Demonstrate adding multiple items at once

fav_pizza.update({
    "Tammy": "Cheese",
    "Kurt": "Sausage"
})

# =======================================================

# Del is fine, but .pop() is more flexible

removed = fav_pizza.pop("April", "Not found")
print("Removed:", removed)

# =======================================================

# Dictionary length

print("Total entries:", len(fav_pizza))

