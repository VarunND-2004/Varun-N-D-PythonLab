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

=== Code Execution Successful ===
-------------------------------------------------------------------------------

"""
