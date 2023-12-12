"""
159. Longest Substring with At Most Two Distinct Characters (medium)
"""

from collections import defaultdict
import unittest


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = left = right = 0
        chars = defaultdict(int)
        while right < len(s):
            chars[s[right]] += 1
            right += 1
            if len(chars) > 2:
                chars[s[left]] -= 1
                if not chars[s[left]]:
                    del chars[s[left]]
                left += 1
            ans = max(ans, right - left)
        return ans


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for s, expected in [
            ("eceba", 3),
            ("ccaabbb", 5),
        ]:
            self.assertEqual(
                Solution().lengthOfLongestSubstringTwoDistinct(s), expected
            )


if __name__ == "__main__":
    unittest.main()
