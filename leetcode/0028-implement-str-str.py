##
#### Implement strStr() (easy)
##################################

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.

# Clarification:
# - What should we return when needle is an empty string? This is a great
#   question to ask during an interview.
# - For the purpose of this problem, we will return 0 when needle is an empty
#   string. This is consistent to C's strstr() and Java's indexOf().

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0
 
# Constraints:
# 0 <= haystack.length, needle.length <= 5 * 104
# haystack and needle consist of only lower-case English characters.

################################################################################

## 
##############################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        return haystack.index(needle) if needle in haystack else -1

    
## 
##############################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if haystack == needle:
            return 0

        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if needle == haystack[i:i + n]:
                return i
            
        return -1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


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


