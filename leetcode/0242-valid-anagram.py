##
#### Valid Anagram (easy)
########################################

# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
 
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?

################################################################################

## first attempt
##############################
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = Counter(s)
        counts_t = Counter(t)

        return counts_s == counts_t


## sorting
##############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return s == t


## hash table
##############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = defaultdict(int)
        
        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1
            
        for count in counts.values():
            if count != 0:
                return False

        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        
        for i in range(len(s)):
            counts[ord(s[i]) - 97] += 1
            counts[ord(t[i]) - 97] -= 1
            
        for count in counts:
            if count != 0:
                return False

        return True


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.isAnagram("anagram", "nagaram"), True)
        self.assertEqual(solution.isAnagram("rat", "car"), False)
        self.assertEqual(solution.isAnagram("a", "ab"), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: (Sorting) [Accepted]
#######################################
# Time: O(nlogn)
# - Assume that nn is the length of ss, sorting costs O(nlogn) and comparing two
#   strings costs O(n). Sorting time dominates and the overall time complexity
#   is O(nlogn).

# Space: O(1)
# - Space depends on the sorting implementation which, usually, costs O(1)
#   auxiliary space if heapsort is used. Note that in Java, toCharArray() makes
#   a copy of the string so it costs O(n) extra space, but we ignore this for
#   complexity analysis because:
#       - It is a language dependent detail.
#       - It depends on how the function is designed. For example, the function
#         parameter types can be changed to char[].

## Java
#public boolean isAnagram(String s, String t) {
#    if (s.length() != t.length()) {
#        return false;
#    }
#    char[] str1 = s.toCharArray();
#    char[] str2 = t.toCharArray();
#    Arrays.sort(str1);
#    Arrays.sort(str2);
#    return Arrays.equals(str1, str2);
#}


## Approach 2: (Hash Table) [Accepted]
##########################################
# Time: O(n) - Time complexity is O(n) because accessing the counter table is a
#              constant time operation.
# Space: O(1) - Although we do use extra space, the space complexity is O(1)
#               because the table's size stays constant no matter how large
#               n is.

## Java
#public boolean isAnagram(String s, String t) {
#    if (s.length() != t.length()) {
#        return false;
#    }
#    int[] counter = new int[26];
#    for (int i = 0; i < s.length(); i++) {
#        counter[s.charAt(i) - 'a']++;
#        counter[t.charAt(i) - 'a']--;
#    }
#    for (int count : counter) {
#        if (count != 0) {
#            return false;
#        }
#    }
#    return true;
#}


#public boolean isAnagram(String s, String t) {
#    if (s.length() != t.length()) {
#        return false;
#    }
#    int[] table = new int[26];
#    for (int i = 0; i < s.length(); i++) {
#        table[s.charAt(i) - 'a']++;
#    }
#    for (int i = 0; i < t.length(); i++) {
#        table[t.charAt(i) - 'a']--;
#        if (table[t.charAt(i) - 'a'] < 0) {
#            return false;
#        }
#    }
#    return true;
#}


## Approach 3: 
##############################
# Time: 
# Space: 


