##
#### 204. Count Prims (medium)
########################################


import math


## best* - using array
##############################
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        nums = [1] * n

        for i in range(2, int(math.sqrt(n)) + 1):
            if nums[i]:
                for multiple in range(i * i, n, i):
                    nums[multiple] = 0

        return nums.count(1) - 2


## sieve
##############################
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        nums = set()

        for i in range(2, int(math.sqrt(n)) + 1):
            if i not in nums:
                for multiple in range(i * i, n, i):
                    nums.add(multiple)

        return n - 2 - len(nums)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        nums = {}

        for i in range(2, int(math.sqrt(n)) + 1):
            if i not in nums:
                for multiple in range(i * i, n, i):
                    nums[multiple] = None  # any arbitrary value

        return n - 2 - len(nums)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        nums = {}

        for i in range(2, int(math.sqrt(n)) + 1):
            if i not in nums:
                for multiple in range(i * i, n, i):
                    nums[multiple] = 1

        return n - 2 - len(nums)


## not optimized [TLE]
##############################
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        nums = [None, None] + list(range(2, n))

        for i in range(2, int(math.sqrt(n)) + 1):
            for multiple in range(i * i, n, i):
                nums[multiple] = None

        nums = list(filter(lambda x: x, nums))

        return len(nums)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().countPrimes(10), 4)
        self.assertEqual(Solution().countPrimes(0), 0)
        self.assertEqual(Solution().countPrimes(1), 0)


if __name__ == "__main__":
    unittest.main()
