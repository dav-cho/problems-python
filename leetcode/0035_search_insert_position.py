##
#### 35. Search Insert Position (easy)
##########################################


## attempt 1 (not O(log(n)))
##############################
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)


## binary search
##############################
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        return left


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 0), 0)
        self.assertEqual(solution.searchInsert([1], 0), 0)

        self.assertEqual(solution.searchInsert([1, 3], 2), 1)
        self.assertEqual(solution.searchInsert([1, 3], 3), 1)
        self.assertEqual(solution.searchInsert([1, 3, 5], 5), 2)
        self.assertEqual(solution.searchInsert([1, 2, 3, 4, 5, 10], 2), 1)


if __name__ == "__main__":
    unittest.main()
