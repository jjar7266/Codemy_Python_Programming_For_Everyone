# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# FizzBuzz_Extra.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

"""
Print out all the numbers between 1 - 100.
If a number is divisible by 3 print out Fizz,
If it's divisible by 5 print out Buzz, 
if it's divisible by 3 and 5 print out FizzBuzz !!,
otherwise just print out the number.
"""

# FizzBuzz !!

# 1. Loop through numbers
# 2. Check if divisible by both
# 3. Check if divisible by 3
# 4. Check if divisible by 5

# Extra Credit

# Try with less lines of code
# Keep separate counters for each

FizzBuzz = 0
Fizz = 0
Buzz = 0

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        FizzBuzz += 1
    elif num % 3 == 0:
        Fizz += 1
    elif num % 5 == 0:
        Buzz += 1

print(f"FizzBuzz: {FizzBuzz}")
print(f"Fizz: {Fizz}")
print(f"Buzz: {Buzz}")


# Instructors Solution
"""
count = 1
while (count <= 100):
    if (count % 3 == 0) and (count % 5 == 0):
        print(f"{count}. FIZZBUZZ !!!")
    elif (count % 3 == 0):
        print(f"{count}. FIZZ !!!")
    elif (count % 5 == 0):
        print(f"{count}. BUZZ !!!")
    else:
        print(f"{count}.")
    
    count += 1
"""

# Example of a Pro Pythonic Version

# 🔥 Ultra‑Clean FizzBuzz With Counters
"""
fizz = buzz = fizzbuzz = 0

for n in range(1, 101):
    if n % 15 == 0:
        fizzbuzz += 1
    elif n % 3 == 0:
        fizz += 1
    elif n % 5 == 0:
        buzz += 1

print(f"FizzBuzz: {fizzbuzz}")
print(f"Fizz: {fizz}")
print(f"Buzz: {buzz}")
"""

# Python‑developer‑approved version of FizzBuzz
# using a dictionary of counters

# 🔥 FizzBuzz With a Counter Dictionary (Clean & Professional)
"""
counts = {"fizz": 0, "buzz": 0, "fizzbuzz": 0}

for n in range(1, 101):
    if n % 15 == 0:
        counts["fizzbuzz"] += 1
    elif n % 3 == 0:
        counts["fizz"] += 1
    elif n % 5 == 0:
        counts["buzz"] += 1

print(counts)
"""

# ⭐ The Ultra‑polished Version

"""
counts = dict(fizz=0, buzz=0, fizzbuzz=0)

for n in range(1, 101):
    if n % 15 == 0:
        counts["fizzbuzz"] += 1
    elif n % 3 == 0:
        counts["fizz"] += 1
    elif n % 5 == 0:
        counts["buzz"] += 1

for key, value in counts.items():
    print(f"{key.capitalize()}: {value}")
"""