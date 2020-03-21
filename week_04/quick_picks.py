import random

QUICK_PICK_COUNT = 6
QUICK_PICK_MIN = 1
QUICK_PICK_MAX = 45


def main():
    pick_total = int(input("How many quick picks would you like? "))
    for i in range(pick_total):
        picks = get_picks()
        display_picks(picks)


def display_picks(picks):
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(picks[0], picks[1], picks[2], picks[3],
                                                       picks[4], picks[5]))


def get_picks():
    """Gather random integers and return them in a list"""
    picks = []
    for j in range(QUICK_PICK_COUNT):
        pick = random.randrange(QUICK_PICK_MIN, QUICK_PICK_MAX + 1)
        if pick not in picks:
            picks.append(pick)
        else:
            while pick in picks:
                pick = random.randrange(QUICK_PICK_MIN, QUICK_PICK_MAX + 1)
            picks.append(pick)
    picks.sort()
    return picks


main()
