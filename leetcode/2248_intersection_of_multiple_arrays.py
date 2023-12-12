"""
2248. Intersection of Multiple Arrays (easy)
"""

from typing import List


class Solution1:
    """First attempt."""

    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for i in range(1, len(nums)):
            res &= set(nums[i])
        return sorted(res)


class Solution2:
    """Hash Map.

    Time complexity: O(n * m + m * log(m))
    Space complexity: O(n * m)
    """

    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)
