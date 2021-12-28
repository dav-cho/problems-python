##
#### Sqrt(x) (easy)
########################################

# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.

# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 
# Constraints:
# 0 <= x <= 231 - 1

################################################################################

from math import e, log


## recursion + bit shifts
##############################
# sqrt(x) = 2 * sqrt(x // 4)
# x << y = x * (2**y)
# x >> y = x // (2**y)

# sqrt(x) = sqrt(x >> 2) << 1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        
        return left if right * right > x else right


## binary search
##############################
# 0 < sqrt(x) < x/2

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 0, x >> 1
        
        while left <= right:
            mid = (left + right) >> 1
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 2
        right = x // 2
        
        while left <= right:
            num = (left + right) // 2
            
            if num * num == x:
                return num
            elif num * num < x:
                left = num + 1
            else:
                right = num - 1
                
        return right


## pocket calculator algorithm
##################################
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = int(e ** (0.5 * log(x)))
        right = left + 1
        
        return left if right * right > x else right


## discuss solutions
##############################

## integer newton
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        
        while r * r > x:
            r = (r + x // r) // 2
            
        return r


class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        
        while r * r > x:
            r = (r + x // r) >> 1
            
        return r


## 
##############################
class Solution:
    def mySqrt(self, x: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().mySqrt(4), 2)
        self.assertEqual(Solution().mySqrt(8), 2)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Pocket Calculator Algorithm
##############################################
# Time: O(1)
# Space: O(1)
from math import e, log
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right


## Approach 2: Binary Search
##############################
# Time: O(logN)
# - Let's compute time complexity with the help of master theorem
#   T(N) = aT(N/b) + Θ(N^d). The equation represents dividing the problem up
#   into a subproblems of size N/b in Θ(N^d) time. Here at step there is only
#   one subproblem a = 1, its size is a half of the initial problem b = 2, and
#   all this happens in a constant time d = 0. That means that log_ba=d and
#   hence we're dealing with case 2 that results in
#   O(n^(log_b(a))log(d+1)N) = O(logN) time complexity.

# Space: O(1)

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right


## Approach 3: Recursion + Bit Shifts
#########################################
# Time: O(logN)
# - Let's compute time complexity with the help of master theorem
#   T(N) = aT(N/b) + Θ(N^d). The equation represents dividing the problem up
#   into a subproblems of size N/b in Θ(N^d) time. Here at step there is only
#   one subproblem a = 1, its size is a half of the initial problem b = 2, and
#   all this happens in a constant time d = 0. That means that log_ba=d and
#   hence we're dealing with case 2 that results in
#   O(n^(log_b(a))log(d+1)N) = O(logN) time complexity.

# Space: O(logN)
# - To keep the recursion stack.
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right * right > x else right


