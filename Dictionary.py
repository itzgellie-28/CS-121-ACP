employees = {
    "Jeraldine": 35000,
    "Bry": 42000,
    "Mae": 39000,
    "Fhey": 45000,
    "Greg": 38000,
}

print("Employee List")
print(employees)

print("\nSpecific employee salary")
print("Jeraldine salary is", employees["Jeraldine"])

print("\nADD EMPLOYEE")
employees["Bry"] = 40000
print(employees)

print("\nUpdate one employee")
employees["Greg"] = 46000
print(employees)

print("\nDelete one employee")
del employees["Fhey"]
print(employees)
