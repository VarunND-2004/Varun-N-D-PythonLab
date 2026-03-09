"""
-------------------------------------------------------------------------------
EXPERIMENT NO: 5
NAME OF THE EXPERIMENT: Write a program to demonstrate tuple & related functions
                        in python.
-------------------------------------------------------------------------------

PROBLEM STATEMENT :
Write a program to demonstrate the creation of tuples, exploring their
immutability, performing indexing/slicing, and using built-in functions
like count() and index().

ALGORITHM :
STEP 1 : Start the program.
STEP 2 : Create a tuple containing various data types (string, int, float).
STEP 3 : Demonstrate Accessing Elements:
         > Use positive and negative indexing.
         > Use slicing to extract sub-tuples.
STEP 4 : Demonstrate Immutability:
         > Attempt to change an element and show that it raises a TypeError.
STEP 5 : Demonstrate Tuple Operations:
         > Concatenate two tuples using the + operator.
         > Repeat a tuple using the * operator.
STEP 6 : Use Built-in Functions:
         > Use count() to find occurrences of an element.
         > Use index() to find the position of an element.
         > Use len(), max(), and min() functions.
STEP 7 : Demonstrate Tuple Packing and Unpacking.
STEP 8 : Stop the program.

-------------------------------------------------------------------------------
"""

# --- SOURCE CODE ---

tech_stack = ("Python", "Java", "C++", "Python", "Ruby", "SQL")

print("\n" + "="*45)
print("EXPERIMENT 5: TUPLE OPERATIONS")
print("="*45)
print(f"Original Tuple: {tech_stack}")

print("\n[1] Accessing & Slicing:")
print(f"First element:       {tech_stack[0]}")
print(f"Last 2 elements:     {tech_stack[-2:]}")
print(f"Every 2nd element:   {tech_stack[::2]}")

print("\n[2] Immutability Test:")
try:
    tech_stack[0] = "Julia"
except TypeError as e:
    print(f"Error caught: {e}")
    print("Note: Tuples cannot be modified after creation.")

print("\n[3] Tuple Methods:")
print(f"Count of 'Python':   {tech_stack.count('Python')}")
print(f"Index of 'C++':      {tech_stack.index('C++')}")

more_tech = ("React", "Node.js")
combined = tech_stack + more_tech
print("\n[4] Tuple Operations:")
print(f"Concatenation (+):   {combined}")
print(f"Repetition (x2):     {more_tech * 2}")

print("\n[5] Tuple Unpacking:")
fruits = ("Apple", "Banana", "Cherry")
(red, yellow, pink) = fruits
print(f"Unpacked values: {red}, {yellow}, {pink}")

print("\n" + "="*45)
print("Code Execution Successful")
print("="*45)

"""
-------------------------------------------------------------------------------
OUTPUT :
Original Tuple: ('Python', 'Java', 'C++', 'Python', 'Ruby', 'SQL')

[1] Accessing & Slicing:
First element:       Python
Every 2nd element:   ('Python', 'C++', 'Ruby')

[2] Immutability Test:
Error caught: 'tuple' object does not support item assignment

[3] Tuple Methods:
Count of 'Python':   2

=== Code Execution Successful ===
-------------------------------------------------------------------------------
"""