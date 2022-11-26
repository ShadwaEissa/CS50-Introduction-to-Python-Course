from validator_collection import validators, checkers, errors

Email = input("What's your email address? ")
is_email_address = checkers.is_email(Email)
if is_email_address:
    print("Valid")
else:
    print("Invalid")