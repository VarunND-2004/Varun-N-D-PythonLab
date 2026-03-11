"""
-------------------------------------------------------------------------------
EXPERIMENT NO: 4
NAME OF THE EXPERIMENT: Write a program to demonstrate list & related functions
                        in python.
-------------------------------------------------------------------------------

PROBLEM STATEMENT :
Write a program to demonstrate the creation of lists using technical keywords,
performing indexing, slicing, and modifying the list using append, insert,
and remove functions.

ALGORITHM :
STEP 1 : Start the program.
STEP 2 : Define a list named 'keywords' containing various API and system terms.
STEP 3 : Use indexing to display the first, last, and last 3 keywords.
STEP 4 : Use slicing to display the first 5 keywords and middle keywords (index 5-10).
STEP 5 : Update the first element of the list to a full definition.
STEP 6 : Demonstrate list growth using append() and insert() at a specific index.
STEP 7 : Demonstrate element removal using the remove() function.
STEP 8 : Check for the existence of a keyword using an 'if' condition.
STEP 9 : Iterate through the entire list using a 'for' loop.
STEP 10: Demonstrate step-slicing to show every 2nd keyword.
STEP 11: Stop the program.

-------------------------------------------------------------------------------
"""

# --- SOURCE CODE ---

keywords = [
    "API", "Application programming Interface", "software interface",
    "Api Specification", "Implementation", "expose", "computer system",
    "user interface", "computer programs", "service", "programmer",
    "subroutines", "method", "request", "endpoints", "API calls",
    "interoperability", "internal details", "web APIs", "Internet",
    "Programming language", "software libraries", "operating system",
    "computing hardware", "standard"
]

print("First Keyword:", keywords[0])
print("Last Keyword:", keywords[-1])
print("First 5 Keywords:", keywords[:5])
print("Middle Keywords:", keywords[5:10])
print("Last 3 Keywords:", keywords[-3:])

keywords[0] = "API (Application programming interface)"
print("\nUpdated first Keyword:", keywords[0])

keywords.append("Integration")
print("After Append:", keywords[-1])

keywords.insert(2, "software development")
print("After insert at index 2:", keywords[2])

keywords.remove("standard")
print("After removing 'standard':", keywords)

print(f"\nTotal Keywords: {len(keywords)}")

if "Internet" in keywords:
    print("Internet is in the list")

print("\nAll Keywords:")
for word in keywords:
    print(word)

print("\nEvery 2nd Keyword (::2):")
print(keywords[::2])

"""
-------------------------------------------------------------------------------
OUTPUT :
First Keyword: API
Last Keyword: standard
First 5 Keywords: ['API', 'Application programming Interface', ...]
Updated first Keyword: API (Application programming interface)
After Append: Integration
After insert at index 2: software development
Total Keywords: 26
Internet is in the list

=== Code Execution Successful ===
-------------------------------------------------------------------------------
"""