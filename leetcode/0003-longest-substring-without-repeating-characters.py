##
#### 3. Longest Substring Without Repeating Characters (medium)
###################################################################


## sliding window
##############################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            res = max(res, right - left)

        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1

        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0

        while right < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1
                res = max(res, right - left)
            else:
                seen.remove(s[left])
                left += 1

        return res


from collections import defaultdict


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

            res = max(res, right - left + 1)
            right += 1

        return res


## first attempt
##############################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                res = max(res, len(s[left : right + 1]))
                right += 1
            else:
                seen.remove(s[left])
                left += 1

        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0

        while right < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                res = max(res, len(s[left : right + 1]))
                right += 1
            else:
                seen.remove(s[left])
                left += 1

        return res


## brute force (TLE)
##############################
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
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring(""), 0)


if __name__ == "__main__":
    unittest.main()
