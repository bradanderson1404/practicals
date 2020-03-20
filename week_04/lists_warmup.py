numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] prints the first index so it would print 3
print(numbers[0])

# numbers[-1] prints the last index so it would print 2
print(numbers[-1])

# numbers[3] prints the fourth index so it prints 1
print(numbers[3])

# numbers[:-1] prints the entire list but stops before the last index
print(numbers[:-1])

# numbers[3:4] prints the list starting at the 4th index and stopping before the 5th. (1)
print(numbers[3:4])

# 5 in numbers would return True
if 5 in numbers:
    print("5 in numbers is True")

# 7 in numbers would return False
if 7 not in numbers:
    print("7 in numbers is False")

# "3" in numbers would return False
if "3" not in numbers:
    print("'3' in numbers is False")

# numbers + [6, 5, 3] would append these values to the end of the list
numbers += [6, 5, 3]
print(numbers)

# 1. Change first element of numbers to the string "ten"
numbers[0] = "ten"
print(numbers)

# 2. change last element of numbers to 1
numbers[-1] = 1
print(numbers)

# 3. get all the elements from numbers except the first two
elements = numbers[2:]
print(elements)

# 4. check if 9 is an element of numbers
if 9 in numbers:
    print("True")
else:
    print("False")
