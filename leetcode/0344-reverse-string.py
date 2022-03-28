##
#### 344. Reverse String (easy)
###################################


## two pointer - best
##############################
class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]


## first attempt
##############################
class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]


## recursive - O(n) space
##############################
class Solution:
    def reverseString(self, s: list[str]) -> None:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.reverseString(["h", "e", "l", "l", "o"]), ["o", "l", "l", "e", "h"]
        )
        self.assertEqual(
            solution.reverseString(["H", "a", "n", "n", "a", "h"]),
            ["h", "a", "n", "n", "a", "H"],
        )


if __name__ == "__main__":
    unittest.main()
