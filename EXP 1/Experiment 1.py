
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

=== Code Execution Successful ===
-------------------------------------------------------------------------------

"""
