import math

# String Operations
text = "python programming"

print("=== String Functions ===")
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Title Case: {text.title()}")
print(f"Length: {len(text)}")
print(f"Replace: {text.replace('python', 'Python')}")
print(f"Split: {text.split()}")
print(f"Count 'g': {text.count('g')}")
print(f"Find 'program': {text.find('program')}")
print()

# Math Operations
number = 25.7

print("=== Math Functions ===")
print(f"Original number: {number}")
print(f"Absolute value: {abs(-number)}")
print(f"Round: {round(number)}")
print(f"Round to 1 decimal: {round(number, 1)}")
print(f"Square root: {math.sqrt(49)}")
print(f"Power: {pow(3, 4)}")
print(f"Max: {max(5, 15, 25)}")
print(f"Min: {min(5, 15, 25)}")
print(f"Floor: {math.floor(number)}")
print(f"Ceil: {math.ceil(number)}")
print(f"Factorial: {math.factorial(5)}")
