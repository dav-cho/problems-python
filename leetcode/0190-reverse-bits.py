##
#### 190. Reverse Bits (easy)
########################################


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
            res += self.reverse_byte(n & 0xFF, cache) << power
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
            res += self.reverse_byte(n & 0xFF, cache) << power
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
            res += self.reverse_byte(n & 0xFF, cache) << power
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
            res += reverse_byte(n & 0xFF) << i
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
            res = (res << 8) + reverse_byte(n & 0xFF)
            n >>= 8

        return res


## mask and shift
##############################
class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)

        return n


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().reverseBits(0b00000010100101000001111010011100), 964176192
        )
        self.assertEqual(
            Solution().reverseBits(0b11111111111111111111111111111101), 3221225471
        )


if __name__ == "__main__":
    unittest.main()
