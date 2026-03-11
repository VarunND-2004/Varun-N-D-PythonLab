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

=== Code Execution Successful ===
-------------------------------------------------------------------------------

"""
