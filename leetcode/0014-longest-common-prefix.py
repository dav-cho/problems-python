##
#### Longest Common Prefix (easy)
########################################

# Write a function to find the longest common prefix string amongst an array
# of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

################################################################################

## horizontal scanning
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        
        res = strs[0]
        
        for i in range(1, len(strs)):
            while strs[i].find(res) != 0:
                res = res[:-1]
                
                if not res:
                    return ''
                
        return res


## vertical scanning
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or len(strs) == 0:
            return ''
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                
        return strs[0]


## divide and conquer
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or len(strs) == 0:
            return ''
        
        def cp(left, right):
            min_len = len(min((left, right), key=len))
            
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
                
            return left[:min_len]
        
        def lcp(left, right):
            if left == right:
                return strs[left]
            
            mid = (left + right) // 2
            lcp_left = lcp(left, mid)
            lcp_right = lcp(mid + 1, right)
            
            return cp(lcp_left, lcp_right)
        
        return lcp(0, len(strs) - 1)


## binary search
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or len(strs) == 0:
            return ''
        
        def is_common_prefix(length):
            for i in range(1, len(strs)):
                if not strs[i].startswith(strs[0][:length]):
                    return False
                
            return True
        
        min_len = len(min(strs, key=len))
        left = 1
        right = min_len
        
        while left <= right:
            mid = (left + right) // 2
            
            if is_common_prefix(mid):
                left = mid + 1
            else:
                right = mid - 1
                
        return strs[0][:(left + right) // 2]


## first attempt
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return res
                
            res += char
            
        return res


## 
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pass


## 
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["flower","flow","flight"]), "fl")
        self.assertEqual(solution.longestCommonPrefix(["dog","racecar","car"]), "")


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Horizontal Scanning
######################################
# Time: O(S) - where S is the sum of all characters in all strings.
# - In the worst case all n strings are the same. The algorithm compares the
#   string S1 with the other strings [S_2 …S_n]. There are S character
#   comparisons, where S is the sum of all characters in the input array.

# Space: O(1) - We only used constant extra space.

## Java
# public String longestCommonPrefix(String[] strs) {
#    if (strs.length == 0) return "";
#    String prefix = strs[0];
#    for (int i = 1; i < strs.length; i++)
#        while (strs[i].indexOf(prefix) != 0) {
#            prefix = prefix.substring(0, prefix.length() - 1);
#            if (prefix.isEmpty()) return "";
#        }        
#    return prefix;
#}


## Approach 2: Vertical Scanning
####################################
# Time: O(S) - Where S is the sum of all characters in all strings. In the worst
#              case there will be nn equal strings with length m and the
#              algorithm performs S=m⋅n character comparisons. Even though the
#              worst case is still the same as Approach 1, in the best case
#              there are at most n n⋅minLen comparisons where minLen is the
#              length of the shortest string in the array.
# Space: O(1) - We only use constant extra space.

## Java
#public String longestCommonPrefix(String[] strs) {
#    if (strs == null || strs.length == 0) return "";
#    for (int i = 0; i < strs[0].length() ; i++){
#        char c = strs[0].charAt(i);
#        for (int j = 1; j < strs.length; j ++) {
#            if (i == strs[j].length() || strs[j].charAt(i) != c)
#                return strs[0].substring(0, i);             
#        }
#    }
#    return strs[0];
#}


## Approach 3: 
##############################
# Time: 
# Space: 


## Approach 4: 
##############################
# Time: 
# Space: 


## Approach 5: 
##############################
# Time: 
# Space: 


