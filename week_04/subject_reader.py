"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    class_lists = get_data()
    display_subject_details(class_lists)


def display_subject_details(class_lists):
    """Format and display the subject details."""
    for i in range(0, len(class_lists)):
        print("{} is taught by {:12} and has {:>3} students".format(class_lists[i][0], class_lists[i][1],
                                                                    class_lists[i][2]))


def get_data():
    """Read data from file and return class information in a list of lists"""
    class_lists = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        class_lists.append(parts)
    input_file.close()
    return class_lists


main()
