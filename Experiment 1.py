"""
-------------------------------------------------------------------------------
EXPERIMENT NO: 1
NAME OF THE EXPERIMENT: Demonstrate Various Data Types and Operators in Python.
-------------------------------------------------------------------------------

PROBLEM STATEMENT :
Write a program to demonstrate various data types and verify mathematical
and bitwise identities using Python operators.

ALGORITHM :
STEP 1 : Start the program.
STEP 2 : Read two integer inputs 'x' and 'y' from the user.
STEP 3 : Verify Algebraic Identities using arithmetic and comparison operators:
         > (x + y)² = x² + 2xy + y²
         > (x - y)² = x² - 2xy + y²
         > (x + y)(x - y) = x² - y²
         > x³ + y³ = (x + y)(x² - xy + y²)
STEP 4 : Verify Bitwise Identities to show the relationship between
         OR, AND, and XOR operations.
STEP 5 : Implement Addition using only bitwise operators.
STEP 6 : Implement Subtraction using multiple variations of bitwise logic.
STEP 7 : Display the boolean results (True/False) for each verification.
STEP 8 : Stop the program.

-------------------------------------------------------------------------------
"""

# --- SOURCE CODE ---

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

print("\n" + "="*40)
print("EXPERIMENT 1: OPERATORS & IDENTITIES")
print("="*40)

print("\nEquation Assignment Operators:")
print(f"(x + y) ** 2 == x**2 + 2*x*y + y**2: {(x + y) ** 2 == x**2 + 2*x*y + y**2}")
print(f"(x - y) ** 2 == x**2 - 2*x*y + y**2: {(x - y) ** 2 == x**2 - 2*x*y + y**2}")
print(f"(x + y) * (x - y) == x**2 - y**2:    {(x + y) * (x - y) == x**2 - y**2}")
print(f"x**3 + y**3 == (x+y)*(x**2-xy+y**2): {x**3 + y**3 == (x + y) * (x**2 - x*y + y**2)}")

print("\nBitwise Operator Demonstration:")
print(f"x | y == (x ^ y) + (x & y):          {x | y == (x ^ y) + (x & y)}")
print(f"x ^ (x & y) == (x | y) ^ y:          {x ^ (x & y) == (x | y) ^ y}")
print(f"y ^ (x & y) == (x | y) ^ x:          {y ^ (x & y) == (x | y) ^ x}")
print(f"(x & y) ^ (x | y) == x ^ y:          {(x & y) ^ (x | y) == x ^ y}")

print("\nAddition using Bitwise Operators:")
print(f"Rule 1 (OR/AND):                     {x + y == (x | y) + (x & y)}")
print(f"Rule 2 (XOR/AND):                    {x + y == (x ^ y) + 2*(x & y)}")

print("\nSubtraction using Bitwise Operators:")
print(f"Method 1: {x - y == (x ^ (x & y)) - ((x | y) ^ x)}")
print(f"Method 2: {x - y == ((x | y) ^ y) - ((x | y) ^ x)}")
print(f"Method 3: {x - y == (x ^ (x & y)) - (y ^ (x & y))}")
print(f"Method 4: {x - y == ((x | y) ^ y) - (y ^ (x & y))}")

print("\n" + "="*40)
print("Code Execution Successful")
print("="*40)

"""
-------------------------------------------------------------------------------
OUTPUT :
Enter the value for x: 10
Enter the value for y: 5

Equation Assignment Operators:
(x + y) ** 2 == x**2 + 2*x*y + y**2: True
(x - y) ** 2 == x**2 - 2*x*y + y**2: True
(x + y) * (x - y) == x**2 - y**2:    True
x**3 + y**3 == (x+y)*(x**2-xy+y**2): True

Bitwise Operator Demonstration:
x | y == (x ^ y) + (x & y):          True
... (Output continues for all identities) ...

=== Code Execution Successful ===
-------------------------------------------------------------------------------
"""