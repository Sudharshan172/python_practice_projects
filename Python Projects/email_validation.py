# Basic Email Validation

''' print("Welcome to Email Validator!!")
e = input("Enter an email to validate: ")
if '.' in e and '@' in e:
    print('valid')
else:
    print("not valid")
================================================ '''
# Complete Email Validation
import re
email_regex = r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$"

def is_valid_email(e):
    return re.match(email_regex, e) is not None

e = input("Enter an email for validation: ")

print(f"{e}: {'Valid' if is_valid_email(e) else 'Invalid'}")
