##
#### Hamming Distance (easy)
########################################

# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

# Example 1:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# Example 2:
# Input: x = 3, y = 1
# Output: 1
 
# Constraints:
# 0 <= x, y <= 231 - 1

################################################################################

## brian kernighan's algorithm
##################################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        
        while xor:
            xor &= xor - 1
            dist += 1
            
        return dist


## bit shift
##############################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        
        while xor:
            if xor & 1:
                dist += 1
                
            xor >>= 1
            
        return dist


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        
        while xor:
            if xor & 1:
                count += 1
                
            xor >>= 1
            
        return count


## flip least significant 1-bit
###################################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        
        while xor != 0:
            xor &= xor - 1
            count += 1
            
        return count


## built-in functions
##############################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


## 3rd attempt
##############################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        xor = x ^ y
        
        while xor > 0:
            xor &= xor - 1
            count += 1
            
        return count


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        xor = x ^ y
        
        while xor != 0:
            xor &= xor - 1
            count += 1
            
        return count


## second attempt
##############################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        mask = 1
        count = 0
        
        for _ in range(32):
            if xor & mask:
                count += 1
                
            mask <<= 1
            
        return count


## first attempt
##############################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


## 
##############################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().hammingDistance(1, 4), 2)
        self.assertEqual(Solution().hammingDistance(3, 1), 1)

if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Built-in BitCounting Functions
#################################################
# Time: O(1)
# - There are two operations in the algorithm. First, we do the XOR operation
#   which takes a constant time.
# - Then, we call the built-in bitCount function. In the worst scenario, the
#   function would take O(k) time where kk is the number of bits for an integer
#   number. Since the Integer type is of fixed size in both Python and Java,
#   the overall time complexity of the algorithm becomes constant, regardless
#   the input numbers.

# Space: O(1) - 
# - A temporary memory of constant size is consumed, to hold the result of XOR
#   operation.
# - We assume that the built-in function also takes a constant space.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


## Approach 2: Bit Shift
##############################
# Time: O(1) - Since the Integer is of fixed size in Python and Java, the
#              algorithm takes a constant time. For an Integer of 32 bit, the
#              algorithm would take at most 32 iterations.
# Space: O(1) - A constant size of memory is used, regardless the input.
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance


## Approach 3: Brian Kernighan's Algorithm
##############################################
# Time: O(1)
# - Similar as the approach of bit shift, since the size (i.e. bit number) of
#   integer number is fixed, we have a constant time complexity.
# - However, this algorithm would require less iterations than the bit shift
#   approach, as we have discussed in the intuition.

# Space: O(1)
# - A constant size of memory is used, regardless the input.

class Solution:
    def hammingDistance(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance


