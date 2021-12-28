##
#### Find Smallest Letter Greater Than Target (easy)
########################################################

# Given a characters array letters that is sorted in non-decreasing order and
# a character target, return the smallest character in the array that is larger
# than target.

# Note that the letters wrap around.

# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 
# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"

# Example 3:
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
 
# Constraints:
# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.

################################################################################

from bisect import bisect


## binary search
##############################
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        idx = bisect(letters, target)
        
        return letters[idx % len(letters)]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        idx = bisect.bisect(letters, target)
        
        return letters[idx] if idx < len(letters) else letters[0]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        res = 0
        
        while left <= right:
            mid = (left + right) >> 1
            
            if letters[mid] > target:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return letters[res]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        res = 0
        
        while left <= right:
            mid = (left + right) >> 1
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
                
        return letters[res]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        
        while left < right:
            mid = (left + right) >> 1
            
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        return letters[left]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        
        while left < right:
            mid = (left + right) >> 1
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
                
        return letters[left]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) >> 1
            
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return letters[left % len(letters)]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        if letters[left] > target or letters[right] < target:
            return letters[left]
        
        while left <= right:
            mid = (left + right) >> 1
            
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return letters[left % len(letters)]


## linear scan
##############################
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char
            
        return letters[0]


## hash table
##############################
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        seen = set(letters)
        
        for i in range(1, 26):
            char = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            
            if char in seen:
                return char


## 
##############################
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().nextGreatestLetter(["c","f","j"], "a"), "c")
        self.assertEqual(Solution().nextGreatestLetter(["c","f","j"], "c"), "f")
        self.assertEqual(Solution().nextGreatestLetter(["c","f","j"], "d"), "f")


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Record Letters Seen [Accepted]
#################################################
# Time: O(N) - Where N is the length of letters. We scan every element of the
#              array.
# Space: O(1) - The maximum size of seen.
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        seen = set(letters)
        for i in xrange(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand


## Approach 2: Linear Scan [Accepted]
#########################################
# Time: O(N) - Where N is the length of letters. We scan every element of the
#              array.
# Space: O(1) - As we maintain only pointers.
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]


## Approach 3: Binary Search [Accepted]
###########################################
# Time: O(logN) - Where N is the length of letters. We peek only at logN
#                 elements in the array.
# Space: O(1) - As we maintain only pointers.
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]


