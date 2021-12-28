##
#### Find K Closest Elements (medium)
########################################

# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending
# order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
 
# Constraints:
# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

################################################################################

from bisect import bisect_left


## binary search to find left bound
#######################################
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
                
        return arr[left:left + k]


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
                
        return arr[left:left + k]


## binary search + sliding window
#####################################
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        if len(arr) == k:
            return arr
        
        left = bisect_left(arr, x) - 1
        right = left + 1
        
        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
                
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
                
        return arr[left + 1:right]


## sort w/ custom comparator
##############################
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        sorted_arr = sorted(arr, key=lambda num: abs(x - num))
        res = [sorted_arr[i] for i in range(k)]
        
        return sorted(res)


## 
##############################
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findClosestElements([1,2,3,4,5], 4, 3), [1,2,3,4])
        self.assertEqual(Solution().findClosestElements([1,2,3,4,5], 4, -1), [1,2,3,4])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Sort With Custom Comparator
##############################################
# Given N as length of arr.

# Time: O(N⋅log(N)+k⋅log(k))
# - To build sortedArr, we need to sort every element in the array by a new
#   criteria: x - num. This costs O(N⋅log(N)). Then, we have to sort sortedArr
#   again to get the output in ascending order. This costs O(k⋅log(k)) time
#   since sortedArr.length is only k.

# Space: O(N)
# - Before we slice sortedArr to contain only k elements, it contains every
#   element from arr, which requires O(N) extra space. Note that we can use
#   less space if we sort the input in place.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort using custom comparator
        sorted_arr = sorted(arr, key = lambda num: abs(x - num))

        # Only take k elements
        result = []
        for i in range(k):
            result.append(sorted_arr[i])
        
        # Sort again to have output in ascending order
        return sorted(result)


## Approach 2: Binary Search + Sliding Window
#################################################
# Time: O(log(N)+k)
# - The initial binary search to find where we should start our window costs
#   O(log(N)). Our sliding window initially starts with size 0 and we expand it
#   one by one until it is of size k, thus it costs O(k) to expand the window.

# Space: O(1)
# - We only use integer variables left and right that are O(1) regardless of
#   input size. Space used for the output is not counted towards the space
#   complexity.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]


## Approach 3: Binary Search To Find The Left Bound
#######################################################
# Time: O(log(N−k)+k)
# - Although finding the bounds only takes O(log(N−k)) time from the binary
#   search, it still costs us O(k) to build the final output.
# - Both the Java and Python implementations require O(k) time to build the
#   result. However, it is worth noting that if the input array were given as
#   a list instead of an array of integers, then the Java implementation could
#   use the ArrayList.subList() method to build the result in O(1) time. If
#   this were the case, the Java solution would have an (extremely fast)
#   overall time complexity of O(log(N−k)).

# Space: O(1)
# - Again, we use a constant amount of space for our pointers, and space used for the output does not count towards the space complexity.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


