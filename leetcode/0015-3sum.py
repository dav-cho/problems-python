##
#### 15. 3Sum (medium)
########################################


## *best: two-pointer
##############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSumII(i):
            left = i + 1
            right = N - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

        nums.sort()
        N = len(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i - 1] != nums[i]:
                twoSumII(i)

        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def find_triplet(i):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum < 0:
                    lo += 1
                elif curr_sum > 0:
                    hi -= 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo - 1] == nums[lo]:
                        lo += 1

        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                find_triplet(i)

        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSumII(i):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum < 0:
                    lo += 1
                elif curr_sum > 0:
                    hi -= 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo - 1] == nums[lo]:
                        lo += 1

        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSumII(i)

        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSumII(i):
            lo, hi = i + 1, N - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum < 0:
                    lo += 1
                elif curr_sum > 0:
                    hi -= 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo - 1] == nums[lo]:
                        lo += 1

        nums.sort()
        N = len(nums)
        res = []
        for i in range(N):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSumII(i)

        return res


## two-pointer
##############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)

        return res

    def twoSumII(self, nums, i, res):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            curr_sum = nums[i] + nums[lo] + nums[hi]
            if curr_sum < 0:
                lo += 1
            elif curr_sum > 0:
                hi -= 1
            else:
                res.append((nums[i], nums[lo], nums[hi]))
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)

        return res

    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            curr_sum = nums[i] + nums[lo] + nums[hi]
            if curr_sum < 0:
                lo += 1
            elif curr_sum > 0:
                hi -= 1
            else:
                res.append((nums[i], nums[lo], nums[hi]))
                lo += 1
                hi -= 1
                while lo < hi and nums[lo - 1] == nums[lo]:
                    lo += 1


## no-sort
##############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        dups = set()
        seen = {}
        for i, x in enumerate(nums):
            if x not in dups:
                dups.add(x)
                for j, y in enumerate(nums[i + 1 :]):
                    comp = -x - y
                    if comp in seen and seen[comp] == i:
                        res.add(tuple(sorted((x, y, comp))))
                    seen[y] = i

        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        dups = set()
        seen = {}
        for i, x in enumerate(nums):
            if x not in dups:
                dups.add(x)
                for j, y in enumerate(nums[i + 1 :]):
                    comp = -x - y
                    if comp in seen and seen[comp] == i:
                        res.add(tuple(sorted([x, y, comp])))
                    seen[y] = i

        return res


## hashset
##############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)

        return res

    def twoSum(self, nums, i, res):
        seen = set()
        j = i + 1
        while j < len(nums):
            comp = -nums[i] - nums[j]
            if comp in seen:
                res.append((nums[i], nums[j], comp))
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(
            Solution().threeSum([-1, 0, 1, 2, -1, -4]), [(-1, -1, 2), (-1, 0, 1)]
        )
        self.assertCountEqual(Solution().threeSum([]), [])
        self.assertCountEqual(Solution().threeSum([0]), [])


if __name__ == "__main__":
    unittest.main()
