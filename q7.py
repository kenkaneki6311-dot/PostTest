students = {"Arnav", "Ankit","Apoorva", "Arpit", "Arnav", "Ankit"}

print(f"Remove Duplicate:", students)

students.add("Anshuman")
students.add("Aryan")

print("Final Students:", students)

students_mark = {
    "Arnav": 85,
    "Ankit": 95,
    "Apoorva": 80,
    "Arpit" : 78,
    "Anshuman" : 65,
    "Aryan" : 95
}

for name, mark in students_mark.items():
    if mark >= 75:
        print(f"{name}: Passed")
    else:
        print(f"{name}: Failed!")