##
#### Longest Palindromic Substring
########################################

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"
 
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

################################################################################


## expand around center
##############################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left + 1:right]
        
        res = ''
        for i in range(len(s)):
            a = expand_around_center(i, i)
            b = expand_around_center(i, i + 1)
            if len(a) > len(b) and len(a) > len(res):
                res = a
            elif len(b) > len(a) and len(b) > len(res):
                res = b
        
        return res


## 
##############################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


## 
##############################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


## 
##############################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


## 
##############################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


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


## LeetCode Solutions
#########################

## Approach 1: Longest Common Substring
###########################################
# Time: 
# Space: 


## Approach 2: Brute Force
##############################
# Time: 
# Space: 


## Approach 3: Dynamic Programming
##############################
# Time: 
# Space: 


## Approach 4: Expand Around Center
##############################
# Time: 
# Space: 


## Approach 5: Manacher's Algorithm
##############################
# Time: 
# Space: 


