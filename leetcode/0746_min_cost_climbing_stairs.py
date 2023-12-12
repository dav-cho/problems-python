##
#### 746. Min Cost Climbing Stairs (easy)
#############################################


from functools import cache, lru_cache


## bottom-up dp (constant space)
####################################
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a = b = 0

        for i in range(1, len(cost)):
            a, b = b, min(b + cost[i], a + cost[i - 1])

        return b


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a = b = 0

        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])

        return b


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev = curr = 0

        for i in range(2, len(cost) + 1):
            prev, curr = curr, min(curr + cost[i - 1], prev + cost[i - 2])

        return curr


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        one = two = 0

        for i in range(2, len(cost) + 1):
            two, one = one, min(one + cost[i - 1], two + cost[i - 2])

        return one


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        down_one = down_two = 0

        for i in range(2, len(cost) + 1):
            down_two, down_one = down_one, min(
                down_one + cost[i - 1], down_two + cost[i - 2]
            )

        return down_one


## bottom-up dp (tabulation)
###############################
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        N = len(cost)
        min_cost = [0, 0] + [None] * (N - 1)

        for i in range(2, N + 1):
            min_cost[i] = min(
                min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2]
            )

        return min_cost[N]


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        N = len(cost)
        min_cost = [0] * (N + 1)

        for i in range(2, N + 1):
            take_one_step = min_cost[i - 1] + cost[i - 1]
            take_two_steps = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(take_one_step, take_two_steps)

        return min_cost[N]


## top-down dp (recursion + memoization)
############################################
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        @lru_cache(None)
        def dp(i):
            if i >= n - 1:
                return 0

            return min(dp(i + 1) + cost[i], dp(i + 2) + cost[i + 1])

        return dp(0)


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @lru_cache(None)
        def dp(i):
            if i < 2:
                return 0

            return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        return dp(len(cost))


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}

        def helper(i):
            if i < 2:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = min(helper(i - 1) + cost[i - 1], helper(i - 2) + cost[i - 2])

            return memo[i]

        return helper(len(cost))


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @cache
        def min_cost(i):
            if i <= 1:
                return 0

            down_one = cost[i - 1] + min_cost(i - 1)
            down_two = cost[i - 2] + min_cost(i - 2)

            return min(down_one, down_two)

        return min_cost(len(cost))


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}

        def min_cost(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]

            down_one = cost[i - 1] + min_cost(i - 1)
            down_two = cost[i - 2] + min_cost(i - 2)
            memo[i] = min(down_one, down_two)

            return memo[i]

        return min_cost(len(cost))


##
##############################
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(
            Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6
        )


if __name__ == "__main__":
    unittest.main()
