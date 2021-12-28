##
#### Valid Perfect Square (easy)
########################################

# Given a positive integer num, write a function which returns True if num is
# a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

# Example 1:
# Input: num = 16
# Output: true

# Example 2:
# Input: num = 14
# Output: false
 
# Constraints:
# 1 <= num <= 2^31 - 1

################################################################################


## newton's method
##############################
# x = (x + num/x) / 2
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        x = num >> 1
        
        while x * x > num:
            x = (x + num // x) >> 1
            
        return x * x == num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        x = num // 2
        
        while x * x > num:
            x = (x + num // x) // 2
            
        return x * x == num


## binary search
##############################
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num >> 1
        
        while left <= right:
            mid = (left + right) >> 1
            
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return False


## first attempt
##############################
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def get_sqrt(x):
            if x < 2:
                return x
            
            left = get_sqrt(x >> 2) << 1
            right = left + 1
            
            return left if right * right > x else right
        
        res = get_sqrt(num)
        
        return res * res == num


## 
##############################
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().isPerfectSquare(16), True)
        self.assertEqual(Solution().isPerfectSquare(14), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Binary Search
################################
# Time: O(logN)
# - Let's compute time complexity with the help of master theorem
#   T(N) = aT(N/b) + Θ(N**d). The equation represents dividing the problem up
#   into aa subproblems of size Θ(N**d) time. Here at step there is only one
#   subproblem a = 1, its size is a half of the initial problem b = 2, and all
#   this happens in a constant time d = 0. That means that log_b(a) = d and
#   hence we're dealing with case 2 that results in
#   O(n**(log_b) * log**(d+1) * N) = O(logN) time complexity.

# Space: O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False


## Approach 2: Newton's Method
##################################
# Time: O(logN) - Because guess sequence converges quadratically.
# Space: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num


