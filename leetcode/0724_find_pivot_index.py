"""
724. Find Pivot Index (easy)
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == right - left - num:
                return i
            left += num
        return -1


class FirstAttempt:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for i in range(len(nums)):
            right -= nums[i]
            if i > 0:
                left += nums[i - 1]
            if left == right:
                return i
        return -1
