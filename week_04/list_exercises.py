numbers = []
for i in range(5):
    number = int(input("Enter Number: "))
    numbers.append(number)
print("The first number is " + str(numbers[0]))
print("The last number is " + str(numbers[-1]))
print("The smallest number is " + str(min(numbers)))
print("The biggest number is " + str(max(numbers)))
print("The average of all numbers is " + str(sum(numbers) / len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_input = input("Enter your username: ")
if user_input in usernames:
    print("Access Granted")
else:
    print("Access Denied!")
