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

# Approach 1: Optimized Brute Force
# --------------------------------
# find all possible subarrays and compare the sums of each subarray
# time - O(N) --> because of nested loop
# space - O(1) --> no additional memory needed

# import math


# def maxSubArray(nums: list[int]) -> int:
#     # initialize max to negative infinity (all values in the array can be negative)
#     max_subarray = -math.inf

#     # loop through each element in the array
#     for i in range(len(nums)):
#         current_subarray = 0
#         #loop through again to get all possible subarrays and their sums
#         for j in range(i, len(nums)):
#             current_subarray += nums[j]
#             max_subarray = max(max_subarray, current_subarray)
#     return max_subarray


# Approach 2: Dynamic Programming
# ------------------------------
# - whenever asked to find the max or min of something, consider dynamic programming
# - this particular solution uses Kadane's Algorithm
# time - O(N) --> where N is length of nums - we iterate through nums exactly once
# space - O(1) --> only ever use 2 variables: current_subarray and max_subarray


def maxSubArray(nums: list[int]) -> int:
    # initialize two variables both starting at 1st element
    current_subarray = max_subarray = nums[0]

    # iterate through array starting from 2nd element (1st was used to initialize)
    for num in nums[1:]:
        # if current_subarray is negative, throw it away
        # otherwise, keep adding to it
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)
    return max_subarray


# Approach 3: Divide and Conquer (Advanced)
# ----------------------------------------
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
# time - O(N log N) --> where N is length of nums - first call of helper function loops
# through entire array splits the array in half with each recursive call
# space - O(log N) --> extra space needed for the recursive stack - base case
# (empty array) occurs after log N calls

# import math


# def maxSubArray(nums: list[int]) -> int:
#     # helper function to find max subarray
#     def find_max_subarray(nums, left, right):
#         if left > right:
#             return -math.inf

#         mid = (left + right) // 2
#         current_sum = max_left_sum = max_right_sum = 0

#         # iterate from the middle to beginning
#         for i in range(mid - 1, left - 1, -1):
#             current_sum += nums[i]
#             max_left_sum = max(max_left_sum, current_sum)

#         # reset current_sum then iterate from middle to end
#         current_sum = 0
#         for i in range(mid + 1, right + 1):
#             current_sum += nums[i]
#             max_right_sum = max(max_right_sum, current_sum)

#         # max combined sum uses middle delement and max sub from each half
#         max_combined_sum = nums[mid] + max_left_sum + max_right_sum

#         # use recursion to find the best subarray possible from both halves
#         left_half = find_max_subarray(nums, left, mid - 1)
#         right_half = find_max_subarray(nums, mid + 1, right)

#         # the largest of the three is the answer for any given input array
#         return max(max_combined_sum, left_half, right_half)

#     # call the helper function with the entire input
#     return find_max_subarray(nums, 0, len(nums) - 1)


maxSubArray1 = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # 6
maxSubArray2 = maxSubArray([1])  # 1
maxSubArray3 = maxSubArray([5, 4, -1, 7, 8])  # 23
print("~ maxSubArray1", maxSubArray1)
print("~ maxSubArray2", maxSubArray2)
print("~ maxSubArray3", maxSubArray3)
