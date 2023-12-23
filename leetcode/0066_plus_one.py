"""
66. Plus One (easy)
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(carry + digits[i], 10)
        return [carry, *digits] if carry else digits
