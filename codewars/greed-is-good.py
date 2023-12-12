##
#### Greed is Good (6kyu)
#############################
from collections import Counter


def score(dice):
    scores = Counter(dice)

    total = 0
    for side in scores:
        quotient, remainder = divmod(scores[side], 3)
        total += quotient * side * 100

        if side == 1:
            total += quotient * 900 + remainder * 100
        if side == 5:
            total += remainder * 50

    return total


## Tests
############
test1 = [2, 3, 4, 6, 2] # 0
test2 = [4, 4, 4, 3, 3] # 400
test3 = [2, 4, 4, 5, 4] # 450
test4 = [1, 1, 1, 3, 3] # 1000

tests = (
    test1,
    test2,
    test3,
    test4,
)


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            result = score(test)

            #print('dice:', test)
            #print('result:', result)
            print(result)

    return run()


test(*tests)

