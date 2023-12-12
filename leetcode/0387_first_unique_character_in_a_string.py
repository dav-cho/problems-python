##
#### 387. First Unique Character in a String (easy)
#######################################################


## first attempt
##############################
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i

        return -1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.firstUniqChar("leetcode"), 0)
        self.assertEqual(solution.firstUniqChar("loveleetcode"), 2)
        self.assertEqual(solution.firstUniqChar("aabb"), -1)


if __name__ == "__main__":
    unittest.main()
