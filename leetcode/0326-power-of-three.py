##
#### Power of Three (easy)
########################################

# Given an integer n, return true if it is a power of three. Otherwise, return
# false.

# An integer n is a power of three, if there exists an integer x such that
# n == 3x.

# Example 1:
# Input: n = 27
# Output: true

# Example 2:
# Input: n = 0
# Output: false

# Example 3:
# Input: n = 9
# Output: true

# Example 4:
# Input: n = 45
# Output: false
 
# Constraints:
# -231 <= n <= 231 - 1
 
# Follow up: Could you solve it without loops/recursion?

################################################################################

## loop
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3:
                return False
            
            n //= 3
            
        return n == 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        
        while not n % 3:
            n /= 3
            
        return n == 1


## recursive
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n % 3:
            return False
        
        return self.isPowerOfThree(n // 3)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n % 3 != 0:
            return False
        
        return self.isPowerOfThree(n // 3)


## integer limitations
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pass


## math
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pass


## base conversion
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().isPowerOfThree(27), True)
        self.assertEqual(Solution().isPowerOfThree(0), False)
        self.assertEqual(Solution().isPowerOfThree(9), True)
        self.assertEqual(Solution().isPowerOfThree(45), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Loop Iteration
#################################
# Time: O(logn) - In our case that is O(logn). The number of divisions is given
#                 by that logarithm.
# Space: O(1) - We are not using any additional memory.

## Java
#public class Solution {
#    public boolean isPowerOfThree(int n) {
#        if (n < 1) {
#            return false;
#        }
#
#        while (n % 3 == 0) {
#            n /= 3;
#        }
#
#        return n == 1;
#    }
#}


## Approach 2: Base Conversion
##################################
# Time: O(log_3(n))
# - Assumptions:
#   - Integer.toString() - Base conversion is generally implemented as a
#     repeated division. The complexity of should be similar to our
#     Approach 1: O(log_3(n)).
#   - String.matches() - Method iterates over the entire string. The number of
#     digits in the base 3 representation of n is O(log_3(n)).

# Space: O(log_3(n))
# - We are using two additional variables,
#   - The string of the base 3 representation of the number (size log_3(n))
#   - The string of the regular expression (constant size)

## Java
#public class Solution {
#    public boolean isPowerOfThree(int n) {
#        return Integer.toString(n, 3).matches("^10*$");
#    }
#}


## Approach 3: Mathematics
##############################
# Time: Unknown - The expensive operation here is Math.log, which upper bounds
#                 the time complexity of our algorithm. The implementation is
#                 dependent on the language we are using and the compiler.
# Space: O(1) -  We are not using any additional memory. The epsilon variable
#                can be inlined.

## Java
#public class Solution {
#    public boolean isPowerOfThree(int n) {
#        return (Math.log10(n) / Math.log10(3)) % 1 == 0;
#    }
#}

# Common pitfalls
# - This solution is problematic because we start using doubles, which means we
#   are subject to precision errors. This means, we should never use == when
#   comparing doubles. That is because the result of
#   Math.log10(n) / Math.log10(3) could be 5.0000001 or 4.9999999. This effect
#   can be observed by using the function Math.log() instead of Math.log10().
# - In order to fix that, we need to compare the result against an epsilon.

# return (Math.log(n) / Math.log(3) + epsilon) % 1 <= 2 * epsilon;

## Approach 4: Integer Limitations
######################################
# Time: O(1) - We are only doing one operations.
# Space: O(1) - We are not using any additional memory.

## Java
#public class Solution {
#    public boolean isPowerOfThree(int n) {
#        return n > 0 && 1162261467 % n == 0;
#    }
#}
