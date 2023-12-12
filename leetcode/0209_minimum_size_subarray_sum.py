"""
209. Minimum Size Subarray Sum (medium)
"""

from typing import List


# two pointers
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = s = 0
        ans = float("inf")

        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                ans = min(ans, i + 1 - l)
                s -= nums[l]
                l += 1

        return int(ans) if ans != float("inf") else 0


# brute force [not accepted]
# time: O(n^2)
# space: O(n)
class BruteForce:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [nums[0]]

        ans = float("inf")

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = prefix[j] - prefix[i] + nums[i]
                if s >= target:
                    ans = min(ans, (j - i + 1))
                    break

        return int(ans) if ans != float("inf") else 0
