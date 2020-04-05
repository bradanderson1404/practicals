user_details = {}

email = input("Enter your email: ")
while email != "" and "@" in email:
    name_portion, domain = email.split("@")
    if "." in name_portion:
        name = name_portion.split(".")
        full_name = " ".join(name)
        prompt = input("Is your name {}? Y/N".format(full_name))
        if prompt.upper() == "N":
            full_name = input("Enter your name: ")
        user_details[email] = full_name
    else:
        full_name = name_portion
        prompt = input("Is your name {}? Y/N".format(full_name))
        if prompt.upper() == "N":
            full_name = input("Enter your name: ")
        user_details[email] = full_name
    email = input("Enter your email: ")

for key in user_details:
    print("{} - ({})".format(user_details[key], key))
