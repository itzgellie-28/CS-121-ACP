import re

emails = ["user@example.com", "invalid-email", "hello@domain.org"]

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

for email in emails:
    if re.match(pattern, email):
        print(f"{email} is a valid email")
    else:
        print(f"{email} is NOT a valid email")
