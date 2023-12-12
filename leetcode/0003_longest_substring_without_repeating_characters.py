"""
3. Longest Substring Without Repeating Characters (medium)
"""

import unittest
from collections import defaultdict


## Sliding Window Optimized (On)
########################################################################################


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        idx_map = {}
        i = 0

        for j, char in enumerate(s):
            if char in idx_map:
                i = max(i, idx_map[char])

            res = max(res, j - i + 1)
            idx_map[char] = j + 1

        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        mp = {}
        res = 0

        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            res = max(res, j - i + 1)
            mp[s[j]] = j + 1

        return res


## Sliding Window (O2n)
########################################################################################


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        j = 0
        seen = set()
        while j < len(s):
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                j += 1

            res = max(res, j - i)

        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        j = 0
        seen = set()

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
            else:
                seen.remove(s[i])
                i += 1

            res = max(res, j - i)

        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = defaultdict(int)
        res = 0

        while right < len(s):
            seen[s[right]] += 1

            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1

            right += 1
            res = max(res, right - left)

        return res


## brute force (TLE)
########################################################################################


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                if s[i] in chars:
                    return False

                chars.add(s[i])

            return True

        N = len(s)
        res = 0

        for i in range(N):
            for j in range(i, N):
                if check(i, j):
                    res = max(res, j - i + 1)

        return res


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring(""), 0)


if __name__ == "__main__":
    unittest.main()
