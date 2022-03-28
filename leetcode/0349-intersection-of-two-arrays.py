##
#### 349. Intersection of Two Arrays (easy)
###############################################


## binary search
##############################
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        nums2.sort()
        res = set()

        for num in nums1:
            if self.search(nums2, num):
                res.add(num)

        return list(res)

    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


## two sets
##############################
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [x for x in set1 if x in set2]


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) > len(set2):
            return self.intersection(nums2, nums1)

        return [x for x in set1 if x in set2]


## built in intersection
##############################
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)


## first attempt
##############################
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = []

        for num in set1:
            if num in set2:
                res.append(num)

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(Solution().intersection([1, 2, 2, 1], [2, 2]), [2])
        self.assertCountEqual(
            Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]), [9, 4]
        )


if __name__ == "__main__":
    unittest.main()
