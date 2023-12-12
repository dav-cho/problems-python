##
#### 153. Find Minimum in Rotated Sorted Array (medium)
###########################################################


## binary search iterative
##############################
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1


## binary search recursive
##############################
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[-1] > nums[0]:
            return nums[0]

        def search(left, right):
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[left]:
                return search(mid + 1, right)

            return search(left, mid - 1)

        return search(0, len(nums) - 1)


## first attempt (Wrong Answer)
##############################
class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] >= nums[lo]:
                    lo = mid + 1
                else:
                    hi = mid

        return lo


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(Solution().findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(Solution().findMin([11, 13, 15, 17]), 11)


if __name__ == "__main__":
    unittest.main()
