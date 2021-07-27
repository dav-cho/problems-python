##
#### New Year Chaos (medium)
################################

# It is New Year's Day and people are in line for the Wonderland
# rollercoaster ride. Each person wears a sticker indicating their
# initial position in the queue from  to . Any person can bribe the
# person directly in front of them to swap positions, but they still wear
# their original sticker. One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get
# to a given queue order. Print the number of bribes, or, if
# anyone has bribed more than two people, print Too chaotic.

# Sample Input:
# STDIN       Function
# -----       --------
# 2           t = 2
# 5           n = 5
# 2 1 5 3 4   q = [2, 1, 5, 3, 4]
# 5           n = 5
# 2 5 1 3 4   q = [2, 5, 1, 3, 4]

# Sample Output:
# 3
# Too chaotic

##############################################################################

from typing import Union

# 1-based indexing: i + 1 should equal person's original position
# - if i is less than person, person moved back
# - if i is greater than person, person moved forward
# i = i + 1
# p = original position (or person's sticker)
# if p - i > 2 --> too chaotic
# if p - i > 0 --> person moved back either 1 or 2 positions
# anyone who bribed p cannot get higher than p + 1
# check for how many greater than p in range
# from i + 1 to p + 1
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
