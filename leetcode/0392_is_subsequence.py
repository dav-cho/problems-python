"""
392. Is Subsequence (easy)
"""

import unittest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_idx: int, right_idx: int):
            if left_idx == LEFT_BOUND:
                return True
            if right_idx == RIGHT_BOUND:
                return False

            if s[left_idx] == t[right_idx]:
                left_idx += 1
            right_idx += 1

            return rec_isSubsequence(left_idx, right_idx)

        return rec_isSubsequence(0, 0)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)

        def inner(i, j):
            if i == s_len:
                return True
            if j == t_len:
                return False

            if s[i] == t[j]:
                i += 1
            j += 1

            return inner(i, j)

        return inner(0, 0)


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for s, t, expected in [
            ("abc", "ahbgdc", True),
            ("axc", "ahbgdc", False),
        ]:
            self.assertEqual(Solution().isSubsequence(s, t), expected)


if __name__ == "__main__":
    unittest.main()
