"""
976. Largest Perimeter Triangle (easy)
"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i : i + 3]
            if a < b + c:
                return a + b + c
        return 0


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            a, b, c = nums[i : i + 3]
            if a + b > c:
                return a + b + c
        return 0
