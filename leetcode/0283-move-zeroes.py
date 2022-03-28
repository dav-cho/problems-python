##
#### 283. Move Zeroes (easy)
################################


## *best
##############################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1


## operation sub-optimal, space sub-optimal
###############################################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zeroes = nums.count(0)
        res = []

        for num in nums:
            if num != 0:
                res.append(num)

        while zeroes:
            res.append(0)
            zeroes -= 1

        for i in range(len(nums)):
            nums[i] = res[i]

        return nums


## space optimal
##############################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1

        for i in range(k, len(nums)):
            nums[i] = 0

        return nums


## optimal
##############################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1

        return nums


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1

        return nums


## first attempt
##############################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1

        for i in range(k, len(nums)):
            nums[i] = 0

        return nums


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(solution.moveZeroes([0]), [0])


if __name__ == "__main__":
    unittest.main()
