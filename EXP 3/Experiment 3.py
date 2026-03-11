
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
