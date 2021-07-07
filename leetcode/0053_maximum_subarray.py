##
#### Maximum Subarray (easy)
#########################

# Given an integer array nums, find the contiguous
# subarray (containing at least one number) which has
# the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# Constraints:
# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105

# Follow up: If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach,
# which is more subtle.

##########################################################################


class Solution:
    def maxSubArray(nums: list[int]) -> int:
        pass


## LeetCode Solutions
#########################

import math

## Approach 1: Optimized Brute Force
########################################
# time: O(n) --> because of nested loop
# space: O(1) --> no additional memory needed
# find all possible subarrays and compare the sums of each subarray

## Intuition

# This algorithm doesn't reliably run under the time limit here on LeetCode.
# We'll still look briefly at it though, as in an interview scenario it would
# be a great start if you're struggling to come up with a better approach.

# Calculate the sum of all subarrays, and keep track of the best one.
# To actually generate all subarrays would take O(N^3) time, but with a
# little optimization, we can achieve brute force in O(N^2) time.
# The trick is to recognize that all of the subarrays starting at a
# particular value will share a common prefix.

## Algorithm

# 1. Initialize a variable maxSubarray = -infinity to keep track of
#    the best subarray. We need to use negative infinity, not 0, because
#    it is possible that there are only negative numbers in the array.
# 2. Use a for loop that considers each index of the array as a starting point.
# 3. For each starting point, create a variable currentSubarray = 0.
#    Then, loop through the array from the starting index, adding each
#    element to currentSubarray. Every time we add an element it represents
#    a possible subarray - so continuously update maxSubarray to contain
#    the maximum out of the currentSubarray and itself.
# 4. Return maxSubarray.
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray


## Approach 2: Dynamic Programming
######################################
# time: O(n) --> where N is length of nums - we iterate through nums exactly once
# space: O(1) --> onlyever use 2 variables: current_subarray and max_subarray
# - whenever asked to find the max or min of something, consider dynamic programming
# - this particular solution uses Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


## Approach 3: Divide and Conquer (Advanced)
################################################
# time: O(n log(n)) --> where N is length of nums - first call of helper function loops
# through entire array splits the array in half with each recursive call
# space: O(log(n)) --> extra space needed for the recursive stack - base case
# (empty array) occurs after log N calls
# - takes more time and space, but is good to know as divide and conquer is
# an extremely common type of algorithm.
# - uses recursion
# - if we split input in half, the max subarray would use:
#    - elements from just the left side
#    - elements from just the right side
#    - elements from both sides
# - thus, the answer is simply the largest of:
#    - max subarray from left side
#    - max subarray from the right side
#    - max subarray that can use elements both sides
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)

        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)


test = Solution()
maxSubArray1 = test.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # 6
maxSubArray2 = test.maxSubArray([1])  # 1
maxSubArray3 = test.maxSubArray([5, 4, -1, 7, 8])  # 23
print("~ maxSubArray1", maxSubArray1)
print("~ maxSubArray2", maxSubArray2)
print("~ maxSubArray3", maxSubArray3)
