# write a function that generates a string that is 27 characters long by choosing random letters from the
# 26 letters in the alphabet plus the space. We’ll write another function that will score each generated
# string by comparing the randomly generated string to the goal.
#
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
# If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s
# progress this third function should print out the best string generated so far and its score every 1000 tries.


import random


def generate_rand(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]

    return res


def score_rand(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame += 1
        return numSame / len(goal)


def main():

    run_count = 0
    goalstring = "methinks it is a weasel"
    newstring = generate_rand(28)
    best = 0
    newscore = score_rand(goalstring, newstring)

    while newscore < 1:
        if newscore > best:
            print(newscore, newstring)
            best = newscore
        newstring = generate_rand(28)
        newscore = score_rand(goalstring, newstring)
        run_count += 1

    if run_count % 1000000 == 1:
        print(run_count) + "cycles completed."

    print("Success")


main()
