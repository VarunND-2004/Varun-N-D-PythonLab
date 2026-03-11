tech_stack = ["Python", "Java", "C++", "Python", "Ruby", "SQL"]

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

=== Code Execution Successful ===
-------------------------------------------------------------------------------

"""
