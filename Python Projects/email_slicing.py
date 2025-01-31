import re
email_regex = r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$"

def is_valid_email(email):
    return re.match(email_regex, email) is not None

email = input("Enter your email id: ")

if is_valid_email(email):
    username = email[0:email.index('@')]
    domain = email[email.index('@') + 1:]
    print("Username - ", username)
    print("Domain - ", domain)
else:
    print("Invalid Email!")