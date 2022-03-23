##
#### Word Break (medium)
########################################

# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in
# the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 
# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

################################################################################


## 
##############################
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        pass


## 
##############################
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        pass


## 
##############################
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        pass


## 
##############################
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().wordBreak("leetcode", ["leet","code"]), true)
        self.assertEqual(Solution().wordBreak("applepenapple", ["apple","pen"]), true)
        self.assertEqual(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]), false)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(2^n) - Given a string of length n, there are n+1 ways to split it
#                into two parts. At each step, we have a choice: to split or
#                not to split. In the worse case, when all choices are to be
#                checked, that results in O(2^n).
# Space: O(n) - The depth of the recursion tree can go upto n.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakRecur(s: str, word_dict: Set[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False

        return wordBreakRecur(s, set(wordDict), 0)


## Approach 2: Recursion with memoization
#############################################
# Time: O(n^3) - Size of recursion tree can go up to n^2.
# Space: O(n) - The depth of recursion tree can go up to n.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def wordBreakMemo(s: str, word_dict: FrozenSet[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                    return True
            return False

        return wordBreakMemo(s, frozenset(wordDict), 0)


## Approach 3: Using Breadth-First-Search
#############################################
# Time: O(n^3) - For every starting index, the search can continue till the end
#                of the given string.
# Space: O(n) - Queue of at most n size is needed.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False


## Approach 4: Using Dynamic Programming
############################################
# Time: O(n^3) - There are two nested loops, and substring computation at each
#                iteration. Overall that results in O(n^3) time complexity.
# Space: O(n) - Length of p array is n+1.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]


