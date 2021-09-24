##
#### First Unique Character in a String (easy)
##################################################

# Given a string s, return the first non-repeating character
# in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

####################################################################

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


## LeetCode Solutions
#########################

## Approach 1: Linear Time Solution
#######################################
# Time: O(N) - Since we go through the string of length N two times.
# Space: O(1) - Because English alphabet contains 26 letters.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1


