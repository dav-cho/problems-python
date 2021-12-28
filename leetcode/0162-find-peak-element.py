##
#### Find Peak Element (medium)
########################################

# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If
# the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
#              number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
#              element is 2, or index number 5 where the peak element is 6.
 
# Constraints:
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

################################################################################


## binary search - iterative
##############################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
                
        return right


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
                
        return left


## binary search - recursive
##############################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        def search(left, right):
            if left == right:
                return left
            
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                return search(left, mid)
            
            return search(mid + 1, right)
        
        return search(0, len(nums) - 1)


## linear search
##############################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
            
        return len(nums) - 1


## 
##############################
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findPeakElement([1,2,3,1]), 2)
        self.assertIn(Solution().findPeakElement([1,2,1,3,5,6,4]), [1, 5])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Linear Scan
##############################
# Time: O(n) - We traverse the nums array of size n only once.
# Space: O(1) - Constant extra space is used.

## Java
#public class Solution {
#    public int findPeakElement(int[] nums) {
#        for (int i = 0; i < nums.length - 1; i++) {
#            if (nums[i] > nums[i + 1])
#                return i;
#        }
#        return nums.length - 1;
#    }
#}


## Approach 2: Recursive Binary Search
##########################################
# Time: O(log_2(n))
# - We reduce the search space in half at every step. Thus, the total search
#   space will be consumed in log_2(n) steps. Here, n refers to the size of
#   numsnums array.

# Space: O(log_2(n))
# - We reduce the search space in half at every step. Thus, the total search
#   space will be consumed in log_2(n) steps. Thus, the depth of recursion tree
#   will go upto log_2(n).

## Java
#public class Solution {
#    public int findPeakElement(int[] nums) {
#        return search(nums, 0, nums.length - 1);
#    }
#    public int search(int[] nums, int l, int r) {
#        if (l == r)
#            return l;
#        int mid = (l + r) / 2;
#        if (nums[mid] > nums[mid + 1])
#            return search(nums, l, mid);
#        return search(nums, mid + 1, r);
#    }
#}


## Approach 3: Iterative Binary Search
##########################################
# Time: O(log_2(n))
# - We reduce the search space in half at every step. Thus, the total search
#   space will be consumed in log_2(n) steps. Here, n refers to the size of
#   nums array.

# Space: O(1)
# - Constant extra space is used.

## Java
#public class Solution {
#    public int findPeakElement(int[] nums) {
#        int l = 0, r = nums.length - 1;
#        while (l < r) {
#            int mid = (l + r) / 2;
#            if (nums[mid] > nums[mid + 1])
#                r = mid;
#            else
#                l = mid + 1;
#        }
#        return l;
#    }
#}


