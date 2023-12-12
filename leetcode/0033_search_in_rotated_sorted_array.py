##
#### 33. Search in Rotated Sorted Array (medium)
####################################################


## one-pass binary search
##############################
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[lo]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # mid = left + (right - left) // 2
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


## binary search
##############################
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_rotate_idx(lo, hi):
            if nums[lo] < nums[hi]:
                return 0

            while lo <= hi:
                mid = (lo + hi) // 2

                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[lo]:
                        hi = mid - 1
                    else:
                        lo = mid + 1

        def search(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2

                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1

            return -1

        N = len(nums)

        if N == 1:
            return 0 if nums[0] == target else -1

        k = find_rotate_idx(0, N - 1)

        if nums[k] == target:
            return k
        if k == 0:
            return search(0, N - 1)
        if nums[0] > target:
            return search(k, N - 1)

        return search(0, k)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_rotate_idx(lo, hi):
            if nums[lo] < nums[hi]:
                return 0

            while lo <= hi:
                mid = (lo + hi) // 2

                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[lo]:
                        hi = mid - 1
                    else:
                        lo = mid + 1

        def search(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2

                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1

            return -1

        N = len(nums)

        if N == 1:
            return 0 if nums[0] == target else -1

        k = find_rotate_idx(0, N - 1)

        if nums[k] == target:
            return k
        if k == 0:
            return search(0, N - 1)
        if nums[0] <= target:
            return search(0, k)

        return search(k, N - 1)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_rotate_idx(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1

        def search(left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

            return -1

        N = len(nums)

        if N == 1:
            return 0 if nums[0] == target else -1

        k = find_rotate_idx(0, N - 1)

        if nums[k] == target:
            return k
        if k == 0:
            return search(0, N - 1)
        if nums[0] > target:
            return search(k, N - 1)

        return search(0, k)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(Solution().search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(Solution().search([1], 0), -1)


if __name__ == "__main__":
    unittest.main()
