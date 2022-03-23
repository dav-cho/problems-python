##
#### Min Cost Climbing Stairs (easy)
########################################

# You are given an integer array cost where cost[i] is the cost of ith step on
# a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 
# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

################################################################################

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
            down_two, down_one = down_one, min(down_one + cost[i - 1], down_two + cost[i - 2])
            
        return down_one


## bottom-up dp (tabulation)
###############################
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        N = len(cost)
        min_cost = [0, 0] + [None] * (N - 1)
        
        for i in range(2, N + 1):
            min_cost[i] = min(min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2])
            
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
        self.assertEqual(Solution().minCostClimbingStairs([10,15,20]), 15)
        self.assertEqual(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]), 6)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Bottom-Up Dynamic Programming (Tabulation)
#############################################################
# Time: O(N) - We iterate N - 1 times, and at each iteration we apply an
#              equation that requires O(1) time.
# Space: O(N) - The array minimumCost is always 1 element longer than the
#               array cost.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        minimum_cost = [0] * (len(cost) + 1)
        
        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i - 1] + cost[i - 1]
            take_two_steps = minimum_cost[i - 2] + cost[i - 2]
            minimum_cost[i] = min(take_one_step, take_two_steps)

        # The final element in minimum_cost refers to the top floor
        return minimum_cost[-1]


## Approach 2: Top-Down Dynamic Programming (Recursion + Memoization)
#########################################################################
# Time: O(N) - minimumCost gets called with each index from 0 to N. Because of
#              our memoization, each call will only take O(1) time.
# Space: O(N) - The extra space used by this algorithm is the recursion call
#               stack. For example, minimumCost(10000) will call
#               minimumCost(9999), which calls minimumCost(9998) etc., all the
#               way down until the base cases at minimumCost(0) and
#               minimumCost(1). In addition, our hash map memo will be of size
#               N at the end, since we populate it with every index from
#               0 to N.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minimum_cost(i):
            # Base case, we are allowed to start at either step 0 or step 1
            if i <= 1:
                return 0

            # Check if we have already calculated minimum_cost(i)
            if i in memo:
                return memo[i]

            # If not, cache the result in our hash map and return it
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        return minimum_cost(len(cost))


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def minimum_cost(i):
            if i <= 1:
                return 0
            
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            return min(down_one, down_two)

        return minimum_cost(len(cost))

## Approach 3: Bottom-Up, Constant Space
############################################
# Time: O(N) - We only iterate N - 1 times, and at each iteration we apply an
#              equation that uses O(1) time.
# Space: O(1) - The only extra space we use is 2 variables, which are
#               independent of input size.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        down_one = down_two = 0
        for i in range(2, len(cost) + 1):
            temp = down_one
            down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
            down_two = temp

        return down_one


