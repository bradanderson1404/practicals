def main():

    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("Password Saved:", end=' ')
    for i in range(len(password)):
        print("*", end='')


def get_password():
    password = input("Enter Password: ")
    while len(password) < 5:
        print("Password cannot be shorter than 5 characters.")
        password = input("Re-enter password: ")
    return password


main()
