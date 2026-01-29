# Codemy.com

# Course: Python Programming For Everyone

# Instructor: John Elder

# namer_module.py

# Code written by Jose "Joe" Ruiz, for my personal use

# Modified instructors code to be more Pythonic and readable

def namer(first_name):
    
    return f"Hello there {first_name}, you are very good looking!"

# Example - Using a test block inside the module


#def namer(first_name):
#   return f'Hello there {first_name}, you are very good looking!'

if __name__ == "__main__":
    # This only runs when executing THIS file directly

    print(namer("Test"))
    
