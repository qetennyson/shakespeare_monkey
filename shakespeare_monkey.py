# write a function that generates a string that is 27 characters long by choosing random letters from the
# 26 letters in the alphabet plus the space. We’ll write another function that will score each generated
# string by comparing the randomly generated string to the goal.
#
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
# If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s
# progress this third function should print out the best string generated so far and its score every 1000 tries.


import string
import random
import time


def generate_rand():

    res = random.choices(string.ascii_lowercase + " ", k=27)
    # res = list("methinks it is like a weasel")
    return res


def score_rand(test):
    goal = list("methinks it is like a weasel")
    score = len([i for i, j in zip(goal, test) if i == j])
    return score


def run_test():

    while True:
        monkey = generate_rand()
        start_time = time.time()

        if score_rand(monkey) >= 13:
            print("Got thirteen")
            print("--- %s seconds ---" (time.time() - start_time()))
            break
        elif 15 <= score_rand(monkey) <= 19:
            print("Not bad.")
        elif 20 <= score_rand(monkey) <= 24:
            print("Almost There!!")
        elif 25 <= score_rand(monkey) < 27:
            print("HNNNGGGGGHHH!")
        elif score_rand(monkey) == 27:
            print("Success")
            break


run_test()
