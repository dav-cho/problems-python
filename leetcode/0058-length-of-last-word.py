##
#### Lenght of Last Word (easy)
########################################

# Given a string s consisting of some words separated by some number of spaces,
# return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 
# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

################################################################################

## one-pass
##############################
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
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
            if s[i] != ' ':
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
            if s[i] != ' ':
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


## LeetCode Solutions
#########################

## Approach 1: 
##############################
# Time: 
# Space: 


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


