"""
1426. Counting Elements (easy)
"""

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        """Hash Set.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        nums = set(arr)
        count = 0

        for num in arr:
            if num + 1 in nums:
                count += 1

        return count
