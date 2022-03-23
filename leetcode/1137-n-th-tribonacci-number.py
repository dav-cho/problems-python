##
#### N-th Tribonacci Number (easy)
########################################

# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

################################################################################

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


## LeetCode Solutions
#########################

## Approach 1: Space Optimisation : Dynamic Programming
###########################################################
# Time: O(N)
# Space: O(1) - Constant space to keep the last three Fibonacci numbers.
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        
        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z


## Approach 2: Performance Optimisation : Recursion with Memoization
########################################################################
# Time: O(1) - To retrieve preliminary computed Tribonacci number, and 38
#              operations for the preliminary computations.
# Space: O(1) - Constant space to keep an array of 38 Tribonacci numbers.
class Tri:
    def __init__(self):
        def helper(k):
            if k == 0:
                return 0
            
            if nums[k]:
                return nums[k]

            nums[k] = helper(k - 1) + helper(k - 2) + helper(k - 3) 
            return nums[k]
        
        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        helper(n - 1)
                    
class Solution:
    t = Tri()
    def tribonacci(self, n: int) -> int:
        return self.t.nums[n]


## Approach 3: Performance Optimisation : Dynamic Programming
#################################################################
# Time: O(1) - To retrieve preliminary computed Tribonacci number, and 38
#              operations for the preliminary computations.
# Space: O(1) - Constant space to keep an array of 38 Tribonacci numbers.
class Tri:
    def __init__(self):
        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        for i in range(3, n):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]
                    
class Solution:
    t = Tri()
    def tribonacci(self, n: int) -> int:
        return self.t.nums[n]


