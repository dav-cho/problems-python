##
#### Find First and Last Position of Element in Sorted Array (medium)
#########################################################################

# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
 
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

################################################################################


## binary search
##############################
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    if is_first:
                        if mid == left or nums[mid - 1] < target:
                            return mid
                        
                        right = mid - 1
                    else:
                        if mid == right or nums[mid + 1] > target:
                            return mid
                        
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return -1
        
        lower_bound = find_bound(True)
        
        if lower_bound == -1:
            return [-1, -1]
        
        upper_bound = find_bound(False)
        
        return [lower_bound, upper_bound]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    if is_first:
                        if mid == left or nums[mid - 1] < target:
                            return mid
                        
                        right = mid - 1
                    else:
                        if mid == right or nums[mid + 1] > target:
                            return mid
                        
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return -1
        
        lower_bound = find_bound(True)
        
        if lower_bound == -1:
            return [-1, -1]
        
        upper_bound = find_bound(False)
        
        return [lower_bound, upper_bound]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lower_bound = self.find_bound(nums, target, True)
        
        if lower_bound == -1:
            return [-1, -1]
        
        upper_bound = self.find_bound(nums, target, False)
        
        return [lower_bound, upper_bound]
    
    def find_bound(self, nums, target, is_first):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if is_first:
                    if mid == left or nums[mid - 1] < target:
                        return mid

                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid

                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


## Discuss Solutions
##############################
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        def search(left, right):
            if nums[left] == target == nums[right]:
                return [left, right]
            
            if nums[left] <= target <= nums[right]:
                mid = (left + right) // 2
                L, R = search(left, mid), search(mid + 1, right)
                
                return max(L, R) if -1 in L + R else [L[0], R[1]]
            
            return [-1, -1]
        
        return search(0, len(nums) - 1)


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        def search(left, right):
            if nums[left] == target == nums[right]:
                return [left, right]
            
            if nums[left] <= target <= nums[right]:
                mid = (left + right) // 2
                left, right = search(left, mid), search(mid + 1, right)
                
                return max(left, right) if -1 in left + right else [left[0], right[1]]
            
            return [-1, -1]
        
        return search(0, len(nums) - 1)


## 
##############################
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().searchRange([5,7,7,8,8,10], 8), [3,4])
        self.assertEqual(Solution().searchRange([5,7,7,8,8,10], 6), [-1,-1])
        self.assertEqual(Solution().searchRange([], 0), [-1,-1])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Binary Search
##############################
# Time: O(logN)
# - Considering there are N elements in the array. This is because binary
#   search takes logarithmic time to scan an array of N elements. Why? Because
#   at each step we discard half of the array we are scanning and hence, we're
#   done after a logarithmic number of steps. We simply perform binary search
#   twice in this case.

# Space: O(1)
# - Since we only use space for a few variables and our result array, all of
#   which require constant space.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
        
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            
            if nums[mid] == target:
                
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    
                    # Search on the right side for the bound.
                    begin = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


