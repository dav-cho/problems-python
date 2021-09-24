##
#### Reverse Integer (easy)
###############################

# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Example 4:
# Input: x = 0
# Output: 0

# Constraints:
# -231 <= x <= 231 - 1

################################################################################

## using divmod - best
##############################
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31
        sign = [1, -1][x < 0]
        x = abs(x)
        rev = 0
        
        while x > 0:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev >= MAX_INT - 1:
                return 0
            
        return rev * sign


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31
        sign = [1, -1][x < 0]
        x = abs(x)
        rev = 0
        
        while x > 0:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if not -MAX_INT <= rev < MAX_INT:
                return 0
            
        return rev * sign


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 / 10
        sign = [1, -1][x < 0]
        x = abs(x)
            
        rev = 0
        while x != 0:
            if rev > MAX_INT:
                return 0
            x, pop = divmod(x, 10)
            rev = rev * 10 + pop
        
        return sign * rev


## convert to string (not allowed by problem description)
#############################################################
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev = int(str(abs(x))[::-1])
        if not -(2 ** 31) < rev < (2 ** 31) - 1:
            return 0
        
        return rev * sign


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rev = int('-' + str(x)[1:][::-1])
        else:
            rev = int(str(x)[::-1])
            
        if not -(2 ** 31) <= rev <= 2 ** 31:
            return 0
        
        return rev


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(120), 21)
        self.assertEqual(solution.reverse(0), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Pop and Push Digits & Check before Overflow
##############################################################
# Time: O(log(x)) - There are roughly log base(10)(x) digits in x.
# Space: O(1)

## C++
#class Solution {
#public:
#    int reverse(int x) {
#        int rev = 0;
#        while (x != 0) {
#            int pop = x % 10;
#            x /= 10;
#            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
#            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
#            rev = rev * 10 + pop;
#        }
#        return rev;
#    }
#};

## Java
#class Solution {
#    public int reverse(int x) {
#        int rev = 0;
#        while (x != 0) {
#            int pop = x % 10;
#            x /= 10;
#            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
#            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
#            rev = rev * 10 + pop;
#        }
#        return rev;
#    }
#}


