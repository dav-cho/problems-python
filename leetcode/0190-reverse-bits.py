##
#### Reverse Bits (easy)
########################################

# Reverse bits of a given 32 bits unsigned integer.

# Note:
# - Note that in some languages, such as Java, there is no unsigned integer
#   type. In this case, both input and output will be given as a signed integer
#   type. They should not affect your implementation, as the integer's internal
#   binary representation is the same, whether it is signed or unsigned.
# - In Java, the compiler represents the signed integers using 2's complement
#   notation. Therefore, in Example 2 above, the input represents the signed
#   integer -3 and the output represents the signed integer -1073741825.
 
# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100
#              represents the unsigned integer 43261596, so return 964176192
#              which its binary representation is
#              00111001011110000010100101000000.

# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101
#              represents the unsigned integer 4294967293, so return 3221225471
#              which its binary representation is
#              10111111111111111111111111111111.
 
# Constraints:
# The input must be a binary string of length 32
 
# Follow up: If this function is called many times, how would you optimize it?

################################################################################


## *best/easiest (bit by bit)
#################################
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
            
        return res


## bit by bit
##############################
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31
        
        while n:
            res += (n & 1) << power
            power -= 1
            n >>= 1
        
        return res


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
            
        return res


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(31, -1, -1):
            res += (n & 1) << i
            n >>= 1
            
        return res


## byte by byte with memoization
####################################
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 24
        cache = {}
        
        while n:
            res += self.reverse_byte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
            
        return res
    
    def reverse_byte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
        
        return cache[byte]


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 24
        cache = {}
        
        while n:
            res += self.reverse_byte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
            
        return res
    
    def reverse_byte(self, byte, cache):
        if byte not in cache:
            res = 0
            curr = byte
            
            for i in range(8):
                res = (res << 1) + (curr & 1)
                curr >>= 1
                
            cache[byte] = res
        
        return cache[byte]


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 24
        cache = {}
        
        while n:
            res += self.reverse_byte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
            
        return res
    
    def reverse_byte(self, byte, cache):
        if byte not in cache:
            res = 0
            curr = byte
            
            for i in range(7, -1, -1):
                res += (curr & 1) << i
                curr >>= 1
                
            cache[byte] = res
        
        return cache[byte]


class Solution:
    def reverseBits(self, n: int) -> int:
        def reverse_byte(byte):
            if byte not in cache:
                res = 0
                curr = byte
                
                for i in range(7, -1, -1):
                    res += (curr & 1) << i
                    curr >>= 1
                    
                cache[byte] = res
                
            return cache[byte]
            
        cache = {}
        res = 0
        
        for i in range(24, -1, -8):
            res += reverse_byte(n & 0xff) << i
            n >>= 8
            
        return res


class Solution:
    def reverseBits(self, n: int) -> int:
        def reverse_byte(byte):
            if byte not in cache:
                res = 0
                curr = byte
                
                for i in range(7, -1, -1):
                    res += (curr & 1) << i
                    curr >>= 1
                    
                cache[byte] = res
                
            return cache[byte]
            
        cache = {}
        res = 0
        
        for _ in range(4):
            res = (res << 8) + reverse_byte(n & 0xff)
            n >>= 8
            
        return res


## mask and shift
##############################
class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)

        return n


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().reverseBits(0b00000010100101000001111010011100), 964176192)
        self.assertEqual(Solution().reverseBits(0b11111111111111111111111111111101), 3221225471)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Bit by Bit
##############################
# Time: O(1) - Though we have a loop in the algorithm, the number of iteration
#              is fixed regardless the input, since the integer is of fixed-size
#              (32-bits) in our problem.
# Space: O(1) - Since the consumption of memory is constant regardless the
#               input.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


## Approach 2: Byte by Byte with Memoization
################################################
# Time: O(1) - Though we have a loop in the algorithm, the number of iteration
#              is fixed regardless the input, since the integer is of fixed-size
#              (32-bits) in our problem.
# Space: O(1) - Again, though we used a cache keep the results of reversed
#               bytes, the total number of items in the cache is bounded to
#               2^8 = 2562.

## Python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023 
        return cache[byte]

## Python3 - with decorator
import functools

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 24
        while n:
            ret += self.reverseByte(n & 0xff) << power
            n = n >> 8
            power -= 8
        return ret

    # memoization with decorator
    @functools.lru_cache(maxsize=256)
    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023


## Approach 3: Mask and Shift
#################################
# Time: O(1) - No loop is used in the algorithm.
# Space: O(1) - Actually, we did not even create any new variable in the
#               function.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


