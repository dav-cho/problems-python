"""
2090. K Radius Subarray Averages (medium)
"""

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k < 0:
            return nums

        n = len(nums)
        avgs = [-1] * n
        width = k * 2 + 1

        if width > n:
            return avgs

        curr_sum = sum(nums[:width])
        avgs[k] = curr_sum // width

        for i in range(width, n):
            curr_sum += nums[i] - nums[i - width]
            avgs[i - k] = curr_sum // width

        return avgs


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        avgs = [-1] * n

        if (width := k * 2 + 1) > n:
            return avgs

        curr_sum = sum(nums[:width])
        avgs[k] = curr_sum // width

        for i in range(width, n):
            curr_sum += nums[i] - nums[i - width]
            avgs[i - k] = curr_sum // width

        return avgs


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        avgs = [-1] * n

        if (width := k * 2 + 1) > n:
            return avgs

        curr_sum = sum(nums[:width])
        avgs[k] = curr_sum // width

        for i in range(n - width):
            curr_sum += nums[i + width] - nums[i]
            avgs[i + k + 1] = curr_sum // width

        return avgs
