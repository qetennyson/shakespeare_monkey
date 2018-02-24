# write a function that generates a string that is 27 characters long by choosing random letters from the
# 26 letters in the alphabet plus the space. We’ll write another function that will score each generated
# string by comparing the randomly generated string to the goal.
#
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
# If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s
# progress this third function should print out the best string generated so far and its score every 1000 tries.


import string
import random


def generate_rand():

    res = random.choices(string.ascii_lowercase + " ", k=27)
    return res


def score_rand(test):
    goal = list("methinks it is like a weasel")
    score = len([i for i, j in zip(goal, test) if i == j])
    return score


def run_test():
    test_num = 0
    while True:
        monkey = generate_rand()
        if score_rand(monkey) < 27:
            test_num += 1
        else:
            print("Success")
            break

        print(str(test_num) + "000 iterations completed")


run_test()