import random


def main():
    score = float(input("Enter score: "))
    print(determine_result(score))
    random_score = random.randrange(0, 100)
    print(random_score, determine_result(random_score))


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"




main()
