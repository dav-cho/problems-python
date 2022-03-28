##
#### 461. Hamming Distance (easy)
########################################


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
        return bin(x ^ y).count("1")


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
        return bin(x ^ y).count("1")


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
