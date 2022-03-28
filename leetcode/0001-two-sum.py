##
#### 1. Two Sum (easy)
##########################


## brute force
##############################
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


## two-pass hash
##############################
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            seen[num] = i

        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen and seen[comp] != i:
                return [i, seen[comp]]


## one-pass hash
##############################
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]

            seen[num] = i


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(solution.twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
