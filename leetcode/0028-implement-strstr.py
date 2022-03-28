##
#### 28. Implement strStr() (easy)
########################################


## first attempt
##############################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        N = len(haystack)
        M = len(needle)

        for i in range(N - M + 1):
            if haystack[i : i + M] == needle:
                return i

        return -1


##
##############################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass


##
##############################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.strStr("hello", "ll"), 2)
        self.assertEqual(solution.strStr("aaaaa", "bba"), -1)
        self.assertEqual(solution.strStr("", ""), 0)


if __name__ == "__main__":
    unittest.main()
