##
#### 162. Find Peak Element (medium)
########################################


## binary search - iterative
##############################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return right


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


## binary search - recursive
##############################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        def search(left, right):
            if left == right:
                return left

            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return search(left, mid)

            return search(mid + 1, right)

        return search(0, len(nums) - 1)


## linear search
##############################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1


##
##############################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findPeakElement([1, 2, 3, 1]), 2)
        self.assertIn(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]), [1, 5])


if __name__ == "__main__":
    unittest.main()
