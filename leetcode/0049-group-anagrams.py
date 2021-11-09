##
#### Group Anagrams (medium)
########################################

# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
 
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

################################################################################

from collections import defaultdict


## letter count
##############################
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word)
            
        return res.values()


## sorting
##############################
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for word in strs:
            res[tuple(sorted(word))].append(word)
        
        return res.values()


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])
        self.assertCountEqual(Solution().groupAnagrams([""]), [[""]])
        self.assertCountEqual(Solution().groupAnagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Categorize by Sorted String
##############################################
# Time: O(NKlogK) - Where N is the length of strs, and K is the maximum length
#                   of a string in strs. The outer loop has complexity O(N) as
#                   we iterate through each string. Then, we sort each string
#                   in O(KlogK) time.
# Space: O(NK) - The total information content stored in ans.
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


## Approach 2: Categorize by Count
######################################
# Time:  O(NK) - Where N is the length of strs, and K is the maximum length of
#                a string in strs. Counting each string is linear in the size
#                of the string, and we count every string.
# Space: O(NK) - The total information content stored in ans.
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


