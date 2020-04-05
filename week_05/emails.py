user_details = {}

email = input("Enter your email: ")

name_portion, domain = email.split("@")
if "." in name_portion:
    firstname, surname = name_portion.split(".")
else:
    firstname = name_portion
