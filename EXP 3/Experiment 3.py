"""
-------------------------------------------------------------------------------
EXPERIMENT NO: 3
NAME OF THE EXPERIMENT: Write a program to implement various string operations.
-------------------------------------------------------------------------------

PROBLEM STATEMENT :
Write a program to demonstrate fundamental string operations including
concatenation, slicing, indexing, and various built-in string methods in Python.

ALGORITHM :
STEP 1 : Start the program.
STEP 2 : Read a main string and a substring from the user.
STEP 3 : Demonstrate Basic Operations:
         > Concatenation (+)
         > Repetition (*)
         > Length calculation (len())
STEP 4 : Demonstrate Slicing and Indexing:
         > Access first and last characters.
         > Slice the string from a specific range.
         > Reverse the string using slicing [::-1].
STEP 5 : Demonstrate Built-in String Methods:
         > Case conversions (upper, lower, title, swapcase).
         > Search and Replace (find, replace, count).
         > Content checking (isalpha, isdigit, isspace).
STEP 6 : Demonstrate Splitting and Joining operations.
STEP 7 : Display the results of each operation clearly.
STEP 8 : Stop the program.

-------------------------------------------------------------------------------
"""

# --- SOURCE CODE ---

print("\n" + "="*45)
print("EXPERIMENT 3: STRING OPERATIONS")
print("="*45)

text = input("Enter a main string: ")
sub = input("Enter a substring to search for: ")

print("\n[1] Basic Operations:")
print(f"Original String:  '{text}'")
print(f"Length of String: {len(text)}")
print(f"Concatenation:    {text + ' is Fun!'}")
print(f"Repetition (x2):  {text * 2}")

print("\n[2] Slicing and Indexing:")
print(f"First Character:  {text[0]}")
print(f"Last Character:   {text[-1]}")
print(f"Slice (0 to 5):   {text[0:6]}")
print(f"Reversed String:  {text[::-1]}")

print("\n[3] String Methods (Transformation):")
print(f"Uppercase:        {text.upper()}")
print(f"Lowercase:        {text.lower()}")
print(f"Title Case:       {text.title()}")
print(f"Swap Case:        {text.swapcase()}")

print("\n[4] Search and Replace:")
print(f"Count of '{sub}': {text.count(sub)}")
print(f"Find '{sub}' index: {text.find(sub)}")
print(f"Replace '{sub}' with 'Java': {text.replace(sub, 'Java')}")

print("\n[5] Boolean Checks:")
print(f"Is Alphabetic?    {text.isalpha()}")
print(f"Is Digit?         {text.isdigit()}")
print(f"Starts with 'P'?  {text.startswith('P')}")

print("\n[6] Split and Join:")
words = text.split()
print(f"Split into List:  {words}")
print(f"Joined with '-':  {'-'.join(words)}")

print("\n" + "="*45)
print("Code Execution Successful")
print("="*45)

"""
-------------------------------------------------------------------------------
OUTPUT :
Enter a main string: Hello Python
Enter a substring to search for: l

[1] Basic Operations:
Length of String: 12
Concatenation:    Hello Python is Fun!

[2] Slicing and Indexing:
First Character:  H
Reversed String:  nohtyP olleH

[3] String Methods:
Uppercase:        HELLO PYTHON

=== Code Execution Successful ===
-------------------------------------------------------------------------------
"""