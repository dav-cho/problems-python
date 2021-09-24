##
#### Longest Substring Without Repeating Characters (medium)
################################################################

# Given a string s, find the length of the longest substring without repeating
# characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.

# Example 4:
# Input: s = ""
# Output: 0
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

################################################################################

## sliding window
##############################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            res = max(res, right - left)
            
        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            
        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0
        
        while right < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1
                res = max(res, right - left)
            else:
                seen.remove(s[left])
                left += 1
                
            
        return res


from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = defaultdict(int)
        res = 0
        
        while right < len(s):
            seen[s[right]] += 1

            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
                
            right += 1
            res = max(res, right - left)
            
        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = defaultdict(int)
        res = 0
        
        while right < len(s):
            seen[s[right]] += 1
            
            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
                
            res = max(res, right - left + 1)
            right += 1
            
        return res


## first attempt
##############################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                res = max(res, len(s[left:right + 1]))
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            
        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        seen = set()
        res = 0
        
        while right < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                res = max(res, len(s[left:right + 1]))
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            
        return res


## brute force (TLE)
##############################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                if s[i] in chars:
                    return False
                
                chars.add(s[i])
                
            return True
        
        N = len(s)
        res = 0
        
        for i in range(N):
            for j in range(i, N):
                if check(i, j):
                    res = max(res, j - i + 1)
                    
        return res


## 
##############################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        pass


## 
##############################
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring(""), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(n 3)
# - To verify if characters within index range [i,j) are all unique, we need to
#   scan all of them. Thus, it costs O(j−i) time.
# - For a given i, the sum of time costed by each j∈[i+1,n] is
#       ∑(n / i+1)O(j−i).
# - Thus, the sum of all the time consumption is:
#       O(∑(n-1/i=0)(∑(n/j=i+1)(j−i)))=O(∑(n-1/i=0)((1+n−i)(n−i))/2)=O(n^3)

# Space: O(min(n,m))
# - We need O(k) space for checking a substring has no duplicate characters,
#   where k is the size of the Set. The size of the Set is upper bounded by the
#   size of the string n and the size of the charset/alphabet m.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res


## Approach 2: Sliding Window
#################################
# Time: O(2n) = O(n) - In the worst case each character will be visited twice by
#                      i and j.
# Space: O(min(m,n)) - Same as the previous approach. We need O(k) space for the
#                      sliding window, where kk is the size of the Set. The size
#                      of the Set is upper bounded by the size of the string n
#                      and the size of the charset/alphabet m.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


