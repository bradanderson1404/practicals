user_details = {}

email = input("Enter your email: ")

name_portion, domain = email.split("@")
if "." in name_portion:
    firstname, surname = name_portion.split(".")
    prompt = input("Is your name {} {}? Y/N".format(firstname, surname))
    full_name = " ".join(firstname, surname)
    while prompt.upper() == "N":
        full_name = input("Enter your name: ")
    user_details[email] = full_name
else:
    firstname = name_portion
    prompt = input("Is your name {}? Y/N".format(firstname))
    while prompt.upper() == "N":
        full_name = input("Enter your name: ")
    user_details[email] = firstname
