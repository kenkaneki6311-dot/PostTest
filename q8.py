f = open("employee.txt", "w")
f.write("Employees\t\t Salary")
f.close()
print("File created!")

with open("employee.txt", "w") as f:
    f.write("Arnav Verma\t\t90000")
    f.write("\nApoorva\t\t80000")
    f.write("\nArpit\t\t70000")
    f.write("\nyash\t\t950000")
    f.write("\nAayush\t\t60000")
    f.close()
print("Data Added!")