##
#### 5. Longest Palindromic Substring
#########################################


## expand around center
##############################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1 : right]

        res = ""
        for i in range(len(s)):
            a = expand_around_center(i, i)
            b = expand_around_center(i, i + 1)
            curr = a if len(a) > len(b) else b
            if len(curr) > len(res):
                res = curr

        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1 : right]

        res = ""
        for i in range(len(s)):
            a = expand_around_center(i, i)
            b = expand_around_center(i, i + 1)
            if len(a) > len(b) and len(a) > len(res):
                res = a
            elif len(b) > len(a) and len(b) > len(res):
                res = b

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().longestPalindrome("babad"), "bab")
        self.assertEqual(Solution().longestPalindrome("cbbd"), "bb")
        self.assertEqual(Solution().longestPalindrome("a"), "a")
        self.assertEqual(Solution().longestPalindrome("ac"), "a")


if __name__ == "__main__":
    unittest.main()
