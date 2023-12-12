##
#### 70. Climbing Stairs (easy)
###################################


## dynamic programming
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0, 1, 2] + [None] * (n - 2)

        for i in range(3, n + 1):
            memo[i] = memo[i - 2] + memo[i - 1]

        return memo[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1, 2] + [None] * (n - 2)

        for i in range(2, n):
            memo[i] = memo[i - 2] + memo[i - 1]

        return memo[n - 1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        memo = [None] * (n + 1)
        memo[1], memo[2] = 1, 2

        for i in range(3, n + 1):
            memo[i] = memo[i - 2] + memo[i - 1]

        return memo[n]


## recursion w/ memoization
##############################

from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]
            elif i > n:
                return 0
            elif i == n:
                return 1

            memo[i] = helper(i + 1) + helper(i + 2)

            return memo[i]

        return helper(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1

            memo[i] = helper(i + 1) + helper(i + 2)

            return memo[i]

        return helper(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * (n + 2)

        def helper(i):
            if memo[i]:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1

            memo[i] = helper(i + 1) + helper(i + 2)

            return memo[i]

        return helper(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict()

        def helper(i, n):
            if i in memo:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1

            memo[i] = helper(i + 1, n) + helper(i + 2, n)

            return memo[i]

        return helper(0, n)


## fibonacci number
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        a, b = 1, 2

        for i in range(3, n + 1):
            c = a + b
            a, b = b, c

        return b


## brute force (TLE)
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i):
            if i > n:
                return 0
            if i == n:
                return 1

            return helper(i + 1) + helper(i + 2)

        return helper(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i, n):
            if i > n:
                return 0
            if i == n:
                return 1

            return helper(i + 1, n) + helper(i + 2, n)

        return helper(0, n)


## fibonacci formula
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        pass


## binets method
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        pass


## Tests
############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(2), 2)
        self.assertEqual(solution.climbStairs(3), 3)

        self.assertEqual(solution.climbStairs(4), 5)
        self.assertEqual(solution.climbStairs(10), 89)
        self.assertEqual(solution.climbStairs(20), 10946)


if __name__ == "__main__":
    unittest.main()
