##
#### 154. Find Minimum in Rotated Sorted Array II (hard)
############################################################


## modified binary search
##############################
# case 1: nums[mid] < nums[right] -> target is to left of mid
# case 2: nums[mid] > nums[right] -> target is to right of mid
# case 3: nums[mid] == nums[right] -> decrement right by one


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[left]


##
##############################
class Solution:
    def findMin(self, nums: list[int]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findMin([1, 3, 5]), 1)
        self.assertEqual(Solution().findMin([2, 2, 2, 0, 1]), 0)


if __name__ == "__main__":
    unittest.main()
