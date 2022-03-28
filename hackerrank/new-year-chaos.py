##
#### New Year Chaos (medium)
################################


from typing import Union


def minimumBribes(q: list[int]) -> Union[int, str]:
    bribes = 0

    for i, p in enumerate(q):
        i += 1
        if p - i > 2:
            return print("Too chaotic")
        # elif p - i > 0:
        for j in range(max(p - 2, 0), i):
            if q[j] > p:
                bribes += 1

    return print(bribes)


#        1  2  3  4  5
test1 = [2, 1, 5, 3, 4]  # 3
test2 = [2, 5, 1, 3, 4]  # Too chaotic
test3 = [5, 1, 2, 3, 7, 8, 6, 4]  # Too chaotic
#        1  2  3  4  5  6  7  8
test4 = [1, 2, 5, 3, 7, 8, 6, 4]  # 7
test5 = [1, 2, 5, 3, 4, 7, 8, 6]  # 4


def test(*args):
    test_number = 0

    def run():
        for test in args:
            nonlocal test_number
            test_number += 1
            print(f"~ test {test_number}:")
            print(test)
            minimumBribes(test)

    return run


test(test1, test2, test3, test4, test5)()
