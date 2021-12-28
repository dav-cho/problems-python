##
#### Level 3: Problem 1
########################################

# Find the Access Codes
# =====================

# In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need
# access to it. But the only door leading to the LAMBCHOP chamber is secured
# with a unique lock system whose number of passcodes changes daily. Commander
# Lambda gets a report every day that includes the locks' access codes, but
# only the Commander knows how to figure out which of several lists contains
# the access codes. You need to find a way to determine which list contains
# the access codes once you're ready to go in. 

# Fortunately, now that you're Commander Lambda's personal assistant, Lambda
# has confided to you that all the access codes are "lucky triples" in order
# to make it easier to find them in the lists. A "lucky triple" is a tuple
# (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that
# information, you can figure out which list contains the number of access
# codes that matches the number of locks on the door when you're ready to go
# in (for example, if there's 5 passcodes, you'd need to find a list with 5
# "lucky triple" access codes).

# Write a function solution(l) that takes a list of positive integers l and
# counts the number of "lucky triples" of (li, lj, lk) where the list indices
# meet the requirement i < j < k.  The length of l is between 2 and 2000
# inclusive.  The elements of l are between 1 and 999999 inclusive.  The
# solution fits within a signed 32-bit integer. Some of the lists are purposely
# generated without any access codes to throw off spies, so if no triples are
# found, return 0. 

# For example, [1, 2, 3, 4, 5, 6] has the triples:
# [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution([1, 1, 1])
# Output: 1

# Input:
# Solution.solution([1, 2, 3, 4, 5, 6])
# Output: 3

# -- Python cases --
# Input:
# solution.solution([1, 2, 3, 4, 5, 6])
# Output: 3

# Input:
# solution.solution([1, 1, 1])
# Output: 1

################################################################################


## Submitted Solution
##############################
def solution(l):
    N = len(l)
    pairs = [0] * N
    count = 0
    for y in range(N):
        for x in range(y):
            if l[y] % l[x] == 0:
                pairs[y] += 1
                count += pairs[x]

    return count


# [1, 2, 3, 4, 5, 6]
# [0, 1, 1, 2, 1, 3]
# count = 3

# [1, 1, 1]
# [0, 1, 2]
# count = 1


## 
##############################
def solution(l):
    pass


## first attempt
##############################

# (x, y, z) such that z % y = 0 and y % x = 0
# find (l[i], l[j], l[k]) where i < j < k
# 2 <= len(l) <= 2000
# if no tuples found, return 0

def solution(l):
    n = len(l)
    res = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                zy = l[k] % l[j] == 0
                yx = l[j] % l[i] == 0
                if zy and yx:
                    res.append((i, j, k))

    return len(res)


## https://stackoverflow.com/questions/39846735/google-foobar-challenge-3-find-the-access-codes
##############################
def solution(l):
    c = [0] * len(l)
    count = 0
    for i in range(0, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                c[i] += 1
                count += c[j]

    return count


## from https://www.youtube.com/watch?v=TW1Sdmx28JA
##############################
def solution(l):
    n = len(l)
    pairs = [0] * n
    count = 0

    # find first pair (x, y)
    # y is between first and last element in list
    for y in range(1, n - 1):
        for x in range(y):
            if l[y] % l[x] == 0:
                pairs[y] += 1

    # find second pair (y, z) and increment count
    # z in the range of 3rd elem to last elem
    for z in range(2, n):
        for y in range(1, z):
            if l[z] % l[y] == 0:
                count += pairs[y]

    return count


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(solution([1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()


