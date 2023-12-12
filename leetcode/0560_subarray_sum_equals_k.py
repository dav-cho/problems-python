"""
560. Subarray Sum Equals K (medium)
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Hash map.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
