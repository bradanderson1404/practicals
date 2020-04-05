user_details = {}

email = input("Enter your email: ")
while email != "" and "@" in email:
    name_portion, domain = email.split("@")
    if "." in name_portion:
        name = name_portion.split(".")
        full_name = " ".join(name)
        prompt = input("Is your name {}? Y/N".format(name))
        while prompt.upper() == "N":
            full_name = input("Enter your name: ")
        user_details[email] = full_name
    else:
        name = name_portion
        prompt = input("Is your name {}? Y/N".format(name))
        while prompt.upper() == "N":
            full_name = input("Enter your name: ")
        user_details[email] = name

