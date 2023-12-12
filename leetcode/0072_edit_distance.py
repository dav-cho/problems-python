##
#### 72. Edit Distance (hard)
########################################


##
##############################
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.minDistance("horse", "ros"), 3)
        self.assertEqual(solution.minDistance("intention", "execution"), 5)


if __name__ == "__main__":
    unittest.main()
