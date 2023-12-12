"""
344. Reverse String (easy)
"""

from typing import List
import unittest


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for s, expected in [
            (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
            (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        ]:
            self.assertEqual(Solution().reverseString(s), expected)


if __name__ == "__main__":
    unittest.main()
