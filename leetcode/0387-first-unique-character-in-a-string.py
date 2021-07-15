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

## Approach 1: Linear Time Solution
#######################################
# time: O(n)
# space: O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        pass


# string slices using pointer
def firstUniqChar(s: str) -> int:
    for i, char in enumerate(s):
        front = s[:i]
        back = s[i + 1 :]

        if char not in front and char not in back:
            return i

    return -1


# hash map using Counter
def firstUniqChar(s: str) -> int:
    counts = Counter(s)

    for char in counts:
        if counts[char] == 1:
            return s.index(char)

    return -1


## Tests
############
def test(arr):
    solution = Solution()
    count = 1

    def run():
        for test in arr:
            result = solution.firstUniqChar(test)
            nonlocal count
            print(f"~ test {count}")
            print(f"{test} --> {result}")

    return run()


tests = ["leetcode", "loveleetcode", "aabb"]
#            0             2           -1

test(tests)


## LeetCode Solutions
#########################


import collections

## Approach 1: Linear Time Solution
#######################################
# time: O(n) - we go through the string of length n, two times
# space: O(1) - english alphabet contains 26 letters - constant space
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
