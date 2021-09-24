##
#### Valid Palindrome (easy)
########################################

# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
#  
# 
# Example 1:
# 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# 
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
# Constraints:
# 
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

################################################################################

## first attempt - best
##############################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True


## two pointer
##############################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True


## reverse
##############################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list(filter(lambda char: char.isalnum(), s.lower()))
                
        return chars == chars[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
                
        return chars == chars[::-1]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(solution.isPalindrome("race a car"), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Compare with Reverse
#######################################
# Time: O(n) - Where n is length of the string.
# - We need to iterate thrice through the string:
#       1. When we filter out non-alphanumeric characters, and convert the
#          remaining characters to lower-case.
#       2. When we reverse the string.
#       3. When we compare the original and the reversed strings.
# - Each iteration runs linear in time (since each character operation completes
#   in constant time). Thus, the effective run-time complexity is linear.

# Space: O(n) - Where n is the length of the string.
# - We need O(n) additional space to stored the filtered string and the
#   reversed string.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list


## Approach 2: Two Pointers
##############################
# Time: O(n) - Where n is the length of the string. We traverse over each
#              character at most once, until the two pointers meet in the
#              middle, or when we break and return early.
# Space: O(1) - No extra space required, at all.
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


