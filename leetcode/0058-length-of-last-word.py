##
#### 58. Length of Last Word (easy)
########################################


## one-pass
##############################
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                res += 1
            elif res:
                return res

        return res


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)
        res = 0

        while i > 0:
            i -= 1
            if s[i] != " ":
                res += 1
            elif res > 0:
                return res

        return res


## built-in methods
##############################
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if not s or s.isspace() else len(s.split()[-1])


## first attempt
##############################
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                return len(s[i])


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().lengthOfLastWord("Hello World"), 5)
        self.assertEqual(Solution().lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(Solution().lengthOfLastWord("luffy is still joyboy"), 6)


if __name__ == "__main__":
    unittest.main()
