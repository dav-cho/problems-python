##
#### Search Insert Position (easy)
######################################

# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0

# Example 5:
# Input: nums = [1], target = 0
# Output: 0
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

################################################################################

## attempt 1 (not O(log(n)))
##############################
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
            
        return len(nums)


## binary search
##############################
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        
        return left


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert([1,3,5,6], 5), 2)
        self.assertEqual(solution.searchInsert([1,3,5,6], 2), 1)
        self.assertEqual(solution.searchInsert([1,3,5,6], 7), 4)
        self.assertEqual(solution.searchInsert([1,3,5,6], 0), 0)
        self.assertEqual(solution.searchInsert([1], 0), 0)

        self.assertEqual(solution.searchInsert([1,3], 2), 1)
        self.assertEqual(solution.searchInsert([1,3], 3), 1)
        self.assertEqual(solution.searchInsert([1,3,5], 5), 2)
        self.assertEqual(solution.searchInsert([1,2,3,4,5,10], 2), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Binary Search
################################
# Time: O(logN)
# Let us compute the time complexity with the help of master theorem:
# aT(N/b) + Θ(N^d). The equation represents dividing the problem up into a
# subproblems of size Θ(N/d) time. Here at each step there is only one
# subproblem i.e. a = 1, its size is a half of the initial problem i.e. b = 2,
# and all this happens in a constant time i.e. d = 0. As a result, log_ba=d and
# hence we're dealing with case 2 that results in
# O(n^log_b(a)*log^(d + 1)*N) = O(logN) time complexity.

# Space: O(1)
# Since it's a constant space solution.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left


