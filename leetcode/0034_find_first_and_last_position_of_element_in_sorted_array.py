##
#### 34. Find First and Last Position of Element in Sorted Array (medium)
#############################################################################


## binary search
##############################
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    if is_first:
                        if mid == left or nums[mid - 1] < target:
                            return mid

                        right = mid - 1
                    else:
                        if mid == right or nums[mid + 1] > target:
                            return mid

                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        lower_bound = find_bound(True)

        if lower_bound == -1:
            return [-1, -1]

        upper_bound = find_bound(False)

        return [lower_bound, upper_bound]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    if is_first:
                        if mid == left or nums[mid - 1] < target:
                            return mid

                        right = mid - 1
                    else:
                        if mid == right or nums[mid + 1] > target:
                            return mid

                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        lower_bound = find_bound(True)

        if lower_bound == -1:
            return [-1, -1]

        upper_bound = find_bound(False)

        return [lower_bound, upper_bound]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lower_bound = self.find_bound(nums, target, True)

        if lower_bound == -1:
            return [-1, -1]

        upper_bound = self.find_bound(nums, target, False)

        return [lower_bound, upper_bound]

    def find_bound(self, nums, target, is_first):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if is_first:
                    if mid == left or nums[mid - 1] < target:
                        return mid

                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid

                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


## Discuss Solutions
##############################
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        def search(left, right):
            if nums[left] == target == nums[right]:
                return [left, right]

            if nums[left] <= target <= nums[right]:
                mid = (left + right) // 2
                L, R = search(left, mid), search(mid + 1, right)

                return max(L, R) if -1 in L + R else [L[0], R[1]]

            return [-1, -1]

        return search(0, len(nums) - 1)


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        def search(left, right):
            if nums[left] == target == nums[right]:
                return [left, right]

            if nums[left] <= target <= nums[right]:
                mid = (left + right) // 2
                left, right = search(left, mid), search(mid + 1, right)

                return max(left, right) if -1 in left + right else [left[0], right[1]]

            return [-1, -1]

        return search(0, len(nums) - 1)


##
##############################
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(Solution().searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
        self.assertEqual(Solution().searchRange([], 0), [-1, -1])


if __name__ == "__main__":
    unittest.main()
