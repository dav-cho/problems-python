##
#### Reverse String (easy)
##############################

# Write a function that reverses a string.
# The input string is given as an array of characters s.


# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# Follow up: Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.

#################################################################################

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
        self.assertEqual(solution.reverseString(["h","e","l","l","o"]), ["o","l","l","e","h"])
        self.assertEqual(solution.reverseString(["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursion, In-Place, O(N) Space
##################################################
# Time: O(N) - Time to perform N/2 swaps.
# Space: O(N) - To keep the recursion stack.
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


## Approach 2: Two Pointers, Iteration, O(1) Space
######################################################
# Time: O(N) - To swap N/2 elements.
# Space: O(1) - It's a constant space solution.
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


