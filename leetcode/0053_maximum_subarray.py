##
#### 53. Maximum Subarray (easy)
########################################


## dynamic programming / kidane's algorithm
###############################################
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = res = nums[0]

        for num in nums[1:]:
            curr = max(num, curr + num)
            res = max(res, curr)

        return res


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = float("-inf")
        curr = 0

        for num in nums:
            curr = max(num, curr + num)
            res = max(res, curr)

        return res


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = float("-inf")
        curr = 0

        for num in nums:
            if curr < 0:
                curr = 0

            curr += num
            res = max(res, curr)

        return res


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = res = float("-inf")

        for num in nums:
            curr = max(num, curr + num)
            res = max(res, curr)

        return res


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])

        return max(nums)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            res = max(res, nums[i])

        return res


## divide and conquer
##############################
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def helper(left, right):
            if left > right:
                return float("-inf")

            mid = (left + right) // 2
            curr = max_left = max_right = 0

            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                max_left = max(max_left, curr)

            curr = 0

            for i in range(mid + 1, right + 1):
                curr += nums[i]
                max_right = max(max_right, curr)

            res = nums[mid] + max_left + max_right

            left_res = helper(left, mid - 1)
            right_res = helper(mid + 1, right)

            return max(res, left_res, right_res)

        return helper(0, len(nums) - 1)


## optimized brute force (TLE)
##################################
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = float("-inf")

        for i in range(len(nums)):
            curr = 0

            for j in range(i, len(nums)):
                curr += nums[j]
                res = max(res, curr)

        return res


## first attempt
##############################
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0

        for i in range(1, N):
            for j in range(N - i):
                res = max(res, sum(nums[i : i + j]))

        return res


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        N = len(nums)
        left, right = 0, 1
        res = sum(nums[left:right])

        while right < N:
            while right < N and nums[right] < 0:
                right += 1

            res = max(res, sum(nums[left : right + 1]))

            while right < N and left < right:
                left += 1
                res = max(res, res - nums[left])

            right += 1

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(solution.maxSubArray([1]), 1)
        self.assertEqual(solution.maxSubArray([5, 4, -1, 7, 8]), 23)


if __name__ == "__main__":
    unittest.main()
