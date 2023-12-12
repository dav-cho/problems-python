"""
283. Move Zeroes (easy)
"""

from typing import List


# time: O(1)
# space: O(n)
class Optimal:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
