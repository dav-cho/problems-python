##
#### House Robber (medium)
########################################

# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

################################################################################


## best - from discuss solutions
####################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = curr = 0
        
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
            
        return curr


## top-down to bottom-up
############################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        def dp(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])

            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])

            return memo[i]

        memo = {}
        return dp(len(nums) - 1)


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)

        if N == 0:
            return nums[0]

        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[N - 1]


## optimized dynamic programming - bottom up
################################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        prev = 0
        curr = nums[0]
        
        for i in range(N - 2, -1, -1):
            prev, curr = curr, max(curr, prev + nums[i])
            
        return curr


class Solution:
    def rob(self, nums: list[int]) -> int:
        next_next_house = 0
        next_house = nums[0]
        
        for i in range(1, len(nums)):
            curr = max(next_house, next_next_house + nums[i])
            next_next_house = next_house
            next_house = curr
            
        return next_house


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        next_next_house = 0
        next_house = nums[0]
        
        for i in range(1, N):
            next_next_house, next_house = next_house, max(next_house, next_next_house + nums[i])
            
        return next_house


## optimized dynamic programming - top down
###############################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        prev = 0
        curr = nums[N - 1]
        
        for i in range(N - 2, -1, -1):
            prev, curr = curr, max(curr, prev + nums[i])
            
        return curr


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        next_next_house = 0
        next_house = nums[N - 1]
        
        for i in range(N - 2, -1, -1):
            next_next_house, next_house = next_house, max(next_house, next_next_house + nums[i])
            
        return next_house


## dp bottom-up iterative (tabulation)
##########################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {}
        memo[N] = 0
        memo[N - 1] = nums[N - 1]
        
        for i in range(N - 2, -1, -1):
            memo[i] = max(memo[i + 1], memo[i + 2] + nums[i])
            
        return memo[0]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = [None] * (N - 1) + [nums[N - 1], 0]
        
        for i in range(N - 2, -1, -1):
            memo[i] = max(memo[i + 1], memo[i + 2] + nums[i])
            
        return memo[0]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {N: 0, N - 1: nums[N - 1]}
        
        for i in range(N - 2, -1, -1):
            memo[i] = max(memo[i + 1], memo[i + 2] + nums[i])
            
        return memo[0]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {0: 0, 1: nums[0]}
        
        for i in range(2, N + 1):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i - 1])
            
        return memo[N]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = { 0: 0, 1: nums[0] }
        
        for i in range(1, N):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])
            
        return memo[N]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {}
        memo[0] = 0
        memo[1] = nums[0]
        
        for i in range(1, N):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])
            
        return memo[N]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = { 0: 0, 1: nums[0] }
        
        for i in range(1, N):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])
            
        return memo[N]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = [0, nums[0]] + [None] * (N - 1)
        
        for i in range(2, N + 1):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i - 1])
            
        return memo[-1]


## dp top-down recursive (memoization)
##########################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        @lru_cache(None)
        def dp(i):
            if i >= len(nums):
                return 0
            
            return max(dp(i + 1), dp(i + 2) + nums[i])
        
        return dp(0)


class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        
        def helper(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(helper(i + 1), helper(i + 2) + nums[i])
            
            return memo[i]
        
        return helper(0)


class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        
        def helper(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(helper(i - 1), helper(i - 2) + nums[i])
            
            return memo[i]
        
        return helper(len(nums) - 1)


## Discuss Solutions
##############################
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = curr = 0
        
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
            
        return curr


class Solution:
    def rob(self, nums: list[int]) -> int:
        a = b = 0
        
        for i in range(len(nums)):
            if i % 2:
                a = max(a + nums[i], b)
            else:
                b = max(a, b + nums[i])
                
        return max(a, b)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.rob([1,2,3,1]), 4)
        self.assertEqual(solution.rob([2,7,9,3,1]), 12)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursion with Memoization
##############################
# Time: O(N) - Since we process at most N recursive calls, thanks to caching,
#              and during each of these calls, we make an O(1) computation which
#              is simply making two other recursive calls, finding their
#              maximum, and populating the cache based on that.
# Space: O(N) - Which is occupied by the cache and also by the recursion stack.
class Solution:
    
    def __init__(self):
        self.memo = {}
    
    def rob(self, nums: List[int]) -> int:
        
        self.memo = {}
        
        return self.robFrom(0, nums)
    
    def robFrom(self, i, nums):
        
        
        # No more houses left to examine.
        if i >= len(nums):
            return 0
        
        # Return cached value.
        if i in self.memo:
            return self.memo[i]
        
        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        
        # Cache for future use.
        self.memo[i] = ans
        return ans


## Approach 2: Dynamic Programming
######################################
# Time: O(N)
# - Since we have a loop from N − 2 ⋯ 0 and we simply use the pre-calculated
#   values of our dynamic programming table for calculating the current value
#   in the table which is a constant time operation.

# Space: O(N)
# - Which is used by the table. So what is the real advantage of this solution
#   over the previous solution? In this case, we don't have a recursion stack.
#   When the number of houses is large, a recursion stack can become a serious
#   limitation, because the recursion stack size will be huge and the compiler
#   will eventually run into stack-overflow problems (no pun intended!).

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        
        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
            
        return maxRobbedAmount[0]    


## Approach 3: Optimized Dynamic Programming
##############################
# Time: O(N) - Since we have a loop from N−2⋯0 and we use the precalculated
#              values of our dynamic programming table to calculate the current
#              value in the table which is a constant time operation.
# Space: O(1) - Since we are not using a table to store our values. Simply using
#               two variables will suffice for our calculations.

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        N = len(nums)
        
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
            
        return rob_next


