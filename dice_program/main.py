import random
import sys


def roll_d4():
    result = random.randint(1, 4)
    return result


def roll_d6():
    result = random.randint(1, 6)
    return result


def roll_d8():
    result = random.randint(1, 8)
    return result


def roll_d10():
    result = random.randint(1, 10)
    return result


def roll_d12():
    result = random.randint(1, 12)
    return result


def roll_d20():
    result = random.randint(1, 20)
    return result


def roll_d100():
    result = random.randint(1, 100)
    return result


print('Multi-Sided Dice Roller!')
while True:
    while True:
        print('Which dice to roll? d(4), d(6), d(8), d(10), d(12), d(20), d(100) > ', end='')
        dice = input()
        roll = 0
        if dice == 'q':
            sys.exit()
        elif not dice == '':
            if int(dice) == 4:
                roll = roll_d4()
                break
            elif int(dice) == 6:
                roll = roll_d6()
                break
            elif int(dice) == 8:
                roll = roll_d8()
                break
            elif int(dice) == 10:
                roll = roll_d10()
                break
            elif int(dice) == 12:
                roll = roll_d12()
                break
            elif int(dice) == 20:
                roll = roll_d20()
                break
            elif int(dice) == 100:
                roll = roll_d100()
                break
        else:
            print("Please type one of the following: 4, 6, 8, 10, 12, 20, 100")
    print("Rolling a D" + str(dice) + ": " + str(roll))




# I guess I really am writing a while True while True in this. I feel like it looks f****d, but whatever. It runs, and it loops
# This took a while, but it's the first Python program I wrote from my own ideas. *_*