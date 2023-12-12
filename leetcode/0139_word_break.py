##
#### 139. Word Break (medium)
########################################


##
##############################
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().wordBreak("leetcode", ["leet", "code"]), true)
        self.assertEqual(Solution().wordBreak("applepenapple", ["apple", "pen"]), true)
        self.assertEqual(
            Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]),
            false,
        )


if __name__ == "__main__":
    unittest.main()
