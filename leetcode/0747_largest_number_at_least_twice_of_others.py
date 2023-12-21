"""
747. Largest Number At Least Twice of Others (easy)
"""

from typing import List


class OnePass:
    def dominantIndex(self, nums: List[int]) -> int:
        first = second = float("-inf")
        idx = 0
        for i, num in enumerate(nums):
            if num > first:
                first, second = num, first
                idx = i
            elif num > second:
                second = num
        if first >= second * 2:
            return idx
        return -1


class TwoPass:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        for num in nums:
            if num == largest:
                continue
            if num * 2 > largest:
                return -1
        return nums.index(largest)


class FirstAttempt:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        for num in nums:
            if num == largest:
                continue
            if num * 2 > largest:
                return -1
        return nums.index(largest)
