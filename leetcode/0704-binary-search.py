##
#### Binary Search (easy)
########################################

# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 
# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

################################################################################


## binary search
##############################
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot = left + (right - left) // 2
            
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
                
        return -1


## first attempt
##############################
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def helper(left, right):
            if left > right:
                return -1
            
            mid = (left + right) // 2
            
            if nums[mid] < target:
                return helper(mid + 1, right)
            elif nums[mid] > target:
                return helper(left, mid - 1)
            else:
                return mid
            
            return -1
            
        return helper(0, len(nums) - 1)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        stack = [(left, right)]
        
        while stack:
            left, right = stack.pop()
            mid = (left + right) // 2
            
            if left > right:
                continue
            if nums[mid] < target:
                stack.append((mid + 1, right))
            elif nums[mid] > target:
                stack.append((left, mid - 1))
            else:
                return mid
            
        return -1


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
# Time: O(logN)
# - Let's compute time complexity with the help of master theorem
#   T(N) = aT(N/b) + Θ(N^d). The equation represents dividing the problem up
#   into a subproblems of size N/b in Θ(N^d) time. Here at step there is only
#   one subproblem a = 1, its size is a half of the initial problem b = 2, and
#   all this happens in a constant time d = 0. That means that log_b(a) = d and
#   hence we're dealing with case 2 that results in
#   O(n^(log_b(a))log^(d+1)N) = O(logN) time complexity.
# Space: O(1) - Since it's a constant space solution.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


