##
#### 268. Missing Number (easy)
########################################


## best*
##############################

## gauss' formula
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        expected = N * (N + 1) // 2
        actual = sum(nums)

        return expected - actual


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(set(nums))


## bit manipulation
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)

        for i, num in enumerate(nums):
            res ^= i ^ num

        return res


## hash set
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        seen = set(nums)

        for num in range(len(nums) + 1):
            if num not in seen:
                return num


## bit manipulation
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)

        for i, num in enumerate(nums):
            res ^= i ^ num

        return res


## sorting
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            if i != num:
                return i

        return nums[-1] + 1


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()

        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0

        for i in range(1, len(nums)):
            expected = nums[i - 1] + 1

            if nums[i] != expected:
                return expected


## gauss' formula
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        expected = N * (N + 1) // 2
        actual = sum(nums)

        return expected - actual


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        expected_sum = N * (N + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)

        return (N * (N + 1) // 2) - sum(nums)


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        expected = len(nums) * (len(nums) + 1) // 2
        actual = sum(nums)

        return expected - actual


## first attempt
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        mx = max(nums)
        seen = set(nums)

        for num in range(mx):
            if num not in seen:
                return num

        return mx + 1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
        self.assertEqual(Solution().missingNumber([0]), 1)


if __name__ == "__main__":
    unittest.main()
