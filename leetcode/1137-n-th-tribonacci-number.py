##
#### 1137. N-th Tribonacci Number (easy)
############################################


from functools import lru_cache


## dp bottom-up (space optimized)
#####################################
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        a = 0
        b = c = 1

        for _ in range(n - 2):
            a, b, c = b, c, a + b + c

        return c


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1]

        for i in range(3, n + 1):
            memo[i % 3] = sum(memo)

        return memo[n % 3]


## dp bottom-up
##############################
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

        return memo[n]


## dp top-down (recursion + memoization)
############################################
class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def dp(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1

            return dp(i - 1) + dp(i - 2) + dp(i - 3)

        return dp(n)


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def helper(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = helper(i - 1) + helper(i - 2) + helper(i - 3)

            return memo[i]

        return helper(n)


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        memo = [0] * (n + 1)
        memo[1] = memo[2] = 1

        def helper(i):
            if i == 0:
                return 0
            if memo[i]:
                return memo[i]

            memo[i] = helper(i - 1) + helper(i - 2) + helper(i - 3)

            return memo[i]

        return helper(n)


## first attempt
##############################
class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        if n < 2:
            return 1

        a = 0
        b = c = 1

        for _ in range(n - 2):
            a, b, c = b, c, a + b + c

        return c


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1] + [None] * (n - 2)

        for i in range(3, n + 1):
            memo[i] = memo[i - 3] + memo[i - 2] + memo[i - 1]

        return memo[n]


##
##############################
class Solution:
    def tribonacci(self, n: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().tribonacci(4), 4)
        self.assertEqual(Solution().tribonacci(25), 1389537)


if __name__ == "__main__":
    unittest.main()
