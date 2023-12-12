##
#### 191. Number of 1 Bits (easy)
########################################


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
        return bin(n)[2:].count("1")


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().hammingWeight(0b00000000000000000000000000001011), 3
        )
        self.assertEqual(
            Solution().hammingWeight(0b00000000000000000000000010000000), 1
        )
        self.assertEqual(
            Solution().hammingWeight(0b11111111111111111111111111111101), 31
        )


if __name__ == "__main__":
    unittest.main()
