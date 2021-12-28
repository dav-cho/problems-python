##
#### Search in a Sorted Array of Unknown Size (medium)
##########################################################

# This is an interactive problem.

# You have a sorted array of unique elements and an unknown size. You do not
# have an access to the array but you can use the ArrayReader interface to
# access it. You can call ArrayReader.get(i) that:

# - returns the value at the ith index (0-indexed) of the secret array (i.e.,
#   secret[i]), or
# - returns 231 - 1 if the i is out of the boundary of the array.

# You are also given an integer target.
 
# Return the index k of the hidden array where secret[k] == target or return -1
# otherwise.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: secret = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in secret and its index is 4.

# Example 2:
# Input: secret = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in secret so return -1.
 
# Constraints:
# 1 <= secret.length <= 104
# -104 <= secret[i], target <= 104
# secret is sorted in a strictly increasing order.

## This is ArrayReader's API interface.
## You should not implement it, or speculate about its implementation

##class ArrayReader:
##    def get(self, index: int) -> int:

################################################################################


## binary search
##############################
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        
        left, right = 0, 1
        
        while reader.get(right) < target:
            left = right
            right <<= 1
            
        while left <= right:
            mid = (left + right) >> 1
            num = reader.get(mid)
            
            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        
        left, right = 0, 1
        
        while reader.get(right) < target:
            left = right
            right <<= 1
            
        while left <= right:
            mid = (left + right) // 2
            num = reader.get(mid)
            
            if num == target:
                return mid
            
            if num < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 1
        
        while reader.get(right) < target:
            left = right
            right <<= 1
            
        while left <= right:
            mid = (left + right) >> 1
            num = reader.get(mid)
            
            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


## 
##############################
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().search([-1,0,3,5,9,12], 9), 4)
        self.assertEqual(Solution().search([-1,0,3,5,9,12], 2), -1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Binary Search
##############################
# Time: O(logT) - Where T is an index of target value.
# - There are two operations here: to define search boundaries and to perform
#   binary search.
# - Let's first find the number of steps k to setup the boundaries. On the
#   first step, the boundaries are 2^0 .. 2^{0 + 1}2 0 ..2 0+1 , on the second
#   step 2^1 .. 2^{1 + 1}2 1 ..2 1+1 , etc. When everything is done, the
#   boundaries are 2^k .. 2^{k + 1}2 k ..2 k+1 and 2^k < T ≤ 2^k+1 . That means
#   one needs k=logT steps to setup the boundaries, that means O(logT) time
#   complexity.
# - Now let's discuss the complexity of the binary search. There are
#   2^{k + 1} - 2^k = 2^k2 k+1 −2 k =2 k elements in the boundaries, i.e.
#   2^logT =T elements. As discussed, binary search has logarithmic complexity,
#   that results in O(logT) time complexity.

# Space: O(1) - Since it's a constant space solution.

class Solution:
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0
        
        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1
        
        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)
            
            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1
        
        # there is no target element
        return -1


