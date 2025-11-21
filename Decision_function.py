age = int(input("Enter Age: "))

if age <= 0 or age > 60:
    print("Invalid age")
else:
    print("Valid age")
    if age >= 18:
        print("Adult")
    elif age >= 13:
        print("Teenager")
    else:
        print("Child")
