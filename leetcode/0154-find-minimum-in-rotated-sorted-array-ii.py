##
#### Find Minimum in Rotated Sorted Array II (hard)
#######################################################

# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

#       [4,5,6,7,0,1,4] if it was rotated 4 times.
#       [0,1,4,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums that may contain duplicates, return the
# minimum element of this array.

# You must decrease the overall operation steps as much as possible.

# Example 1:
# Input: nums = [1,3,5]
# Output: 1

# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
 
# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
 
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array,
#            but nums may contain duplicates. Would this affect the runtime
#            complexity? How and why?

################################################################################


## modified binary search
##############################
# case 1: nums[mid] < nums[right] -> target is to left of mid
# case 2: nums[mid] > nums[right] -> target is to right of mid
# case 3: nums[mid] == nums[right] -> decrement right by one

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) >> 1
            
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
                
        return nums[left]


## 
##############################
class Solution:
    def findMin(self, nums: list[int]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findMin([1,3,5]), 1)
        self.assertEqual(Solution().findMin([2,2,2,0,1]), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Variant of Binary Search
###########################################
# Time: O(log_(N)) - On average.
# - Where N is the length of the array, since in general it is a binary search
#   algorithm. However, in the worst case where the array contains identical
#   elements (i.e. case #3 nums[pivot]==nums[high]), the algorithm would
#   deteriorate to iterating each element, as a result, the time complexity
#   becomes O(N).

# Space: O(1) - It's a constant space solution.
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low = 0
        high = len(nums)-1
        while high > low:
            pivot = low + (high - low) // 2
            # risk of overflow: pivot = (low + high) // 2
            # Case 1):
            if nums[pivot] < nums[high]:
                high = pivot 
                # alternative: high = pivot - 1
                # too aggressive to move the `high` index,
                # it won't work for the test case of [3, 1, 3]
            # Case 2):
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            # Case 3):
            else:
                high -= 1
        # the 'low' and 'high' index converge to the inflection point.
        return nums[low]


