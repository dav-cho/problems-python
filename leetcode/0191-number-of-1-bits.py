##
#### Number of 1 Bits (easy)
########################################

# Write a function that takes an unsigned integer and returns the number of '1'
# bits it has (also known as the Hamming weight).

# Note:
# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 
# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a
# total of three '1' bits.

# Example 2:
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a
# total of one '1' bit.

# Example 3:
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a
# total of thirty one '1' bits.
 
# Constraints:
# The input must be a binary string of length 32.
 
# Follow up: If this function is called many times, how would you optimize it?

################################################################################

## bit manipulation - flip least significant 1-bit
######################################################
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n != 0:
            n &= n - 1
            count += 1
            
        return count


## loop and bit mask
##############################
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            count += n & 1
            n >>= 1
            
        return count


## first attempt
##############################
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().hammingWeight(0b00000000000000000000000000001011), 3)
        self.assertEqual(Solution().hammingWeight(0b00000000000000000000000010000000), 1)
        self.assertEqual(Solution().hammingWeight(0b11111111111111111111111111111101), 31)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: (Loop and Flip) [Accepted]
#############################################
# Time: O(1) - The run time depends on the number of bits in n. Because n in
#              this piece of code is a 32-bit integer, the time complexity
#              is O(1).
# Space: O(1) - Additional space is allocated.

## Java
#public int hammingWeight(int n) {
#    int bits = 0;
#    int mask = 1;
#    for (int i = 0; i < 32; i++) {
#        if ((n & mask) != 0) {
#            bits++;
#        }
#        mask <<= 1;
#    }
#    return bits;
#}


## Approach 2: (Bit Manipulation Trick) [Accepted]
######################################################
# Time: O(1) - The run time depends on the number of 11-bits in n. In the worst
#              case, all bits in n are 1-bits. In case of a 32-bit integer, the
#              run time is O(1).
# Space: O(1) - No additional space is allocated.

## Java
#public int hammingWeight(int n) {
#    int sum = 0;
#    while (n != 0) {
#        sum++;
#        n &= (n - 1);
#    }
#    return sum;
#}


## Approach 3: 
##############################
# Time: 
# Space: 


