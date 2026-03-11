"""
-------------------------------------------------------------------------------
EXPERIMENT NO: 6
NAME OF THE EXPERIMENT: Write a program to demonstrate Dictionary & related
                        functions in python
-------------------------------------------------------------------------------

PROBLEM STATEMENT :
Write a program to create a dictionary, perform basic operations like
accessing, adding, updating, and deleting key-value pairs, and demonstrate
the use of built-in dictionary methods.

ALGORITHM :
STEP 1 : Start the program.
STEP 2 : Create a dictionary 'student' with keys: Name, Roll_No, Course, and Marks.
STEP 3 : Access values using keys and the get() method.
STEP 4 : Update an existing value (e.g., update Marks).
STEP 5 : Add a new key-value pair (e.g., add 'Grade').
STEP 6 : Demonstrate Deletion:
         > Use pop() to remove a specific key.
         > Use del to remove an item.
STEP 7 : Use Built-in Methods:
         > keys() to get all keys.
         > values() to get all values.
         > items() to get key-value pairs.
STEP 8 : Iterate through the dictionary using a loop.
STEP 9 : Clear the dictionary and stop the program.

-------------------------------------------------------------------------------
"""

# --- SOURCE CODE ---

student = {
    "Name": "Rahul",
    "Roll_No": 101,
    "Course": "Data Science",
    "Marks": 85
}

print("\n" + "="*45)
print("EXPERIMENT 6: DICTIONARY OPERATIONS")
print("="*45)
print(f"Initial Dictionary: {student}")

print("\n[1] Accessing Data:")
print(f"Student Name:      {student['Name']}")
print(f"Course (using get): {student.get('Course')}")

print("\n[2] Modifying Dictionary:")
student["Marks"] = 92                # Updating existing key
student["Grade"] = "A"               # Adding new key-value pair
print(f"After Update & Add: {student}")

print("\n[3] Dictionary Methods:")
print(f"All Keys:   {list(student.keys())}")
print(f"All Values: {list(student.values())}")
print(f"All Items:  {list(student.items())}")

print("\n[4] Removing Data:")
removed_val = student.pop("Roll_No")
print(f"After pop('Roll_No'): {student}")
print(f"Popped Value: {removed_val}")

print("\n[5] Iterating through Dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

student.clear()
print(f"\nAfter clear(): {student} (Empty)")

print("\n" + "="*45)
print("Code Execution Successful")
print("="*45)

"""
-------------------------------------------------------------------------------
OUTPUT :
Initial Dictionary: {'Name': 'Rahul', 'Roll_No': 101, 'Course': 'Data Science', 'Marks': 85}

[1] Accessing Data:
Student Name:      Rahul

[2] Modifying Dictionary:
After Update & Add: {'Name': 'Rahul', 'Roll_No': 101, 'Course': 'Data Science', 'Marks': 92, 'Grade': 'A'}

[5] Iterating through Dictionary:
Name: Rahul
Course: Data Science
Marks: 92
Grade: A

=== Code Execution Successful ===
-------------------------------------------------------------------------------
"""