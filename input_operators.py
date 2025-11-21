fname = str(input("Enter first name: "))
lname = str(input("Enter last name: "))
city = str(input("Enter city: "))
year = int(input("Enter birth year: "))
year = str(year)

print(f"My name is {fname} {lname}, I live in {city}, and I was born in {year}")

print("First name (uppercase):", fname.upper())
print("Last name length:", len(lname))
print(year + " is a string now")
print("City (lowercase):", city.lower())
