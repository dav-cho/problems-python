##
#### 704. Binary Search (easy)
########################################


## binary search
##############################
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1


## first attempt
##############################
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def helper(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] < target:
                return helper(mid + 1, right)
            elif nums[mid] > target:
                return helper(left, mid - 1)
            else:
                return mid

            return -1

        return helper(0, len(nums) - 1)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        stack = [(left, right)]

        while stack:
            left, right = stack.pop()
            mid = (left + right) // 2

            if left > right:
                continue
            if nums[mid] < target:
                stack.append((mid + 1, right))
            elif nums[mid] > target:
                stack.append((left, mid - 1))
            else:
                return mid

        return -1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(Solution().search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()
