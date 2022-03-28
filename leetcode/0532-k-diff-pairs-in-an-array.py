##
#### 532. K-diff Pairs in an Array (medium)
###############################################


from collections import Counter


## hash map
##############################
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        counts = Counter(nums)
        res = 0
        for num in counts:
            if k > 0 and num + k in counts:
                res += 1
            elif k == 0 and counts[num] > 1:
                res += 1

        return res


## two-pointers
##############################
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, 1
        res = 0
        while left < n and right < n:
            diff = nums[right] - nums[left]
            if left == right or diff < k:
                right += 1
            elif diff > k:
                left += 1
            else:
                left += 1
                res += 1
                while left < n and nums[left] == nums[left - 1]:
                    left += 1

        return res


## brute force (TLE)
##############################
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        s_nums = sorted(nums)
        n = len(s_nums)
        res = 0
        for i in range(n):
            if i > 0 and s_nums[i] == s_nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and s_nums[j] == s_nums[j - 1]:
                    continue

                if abs(s_nums[j] - s_nums[i] == k):
                    res += 1

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findPairs([3, 1, 4, 1, 5], 2), 2)
        self.assertEqual(Solution().findPairs([1, 2, 3, 4, 5], 1), 4)
        self.assertEqual(Solution().findPairs([1, 3, 1, 5, 4], 0), 1)


if __name__ == "__main__":
    unittest.main()
