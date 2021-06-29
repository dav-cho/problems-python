##
#### Move Zeroes (easy)
###########################

# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?

########################################################################


## naive
# def move_zeroes(nums: list[int]) -> None:
#     pass


# Approach 1: Space Sub-Optimal
# ----------------------------
# def move_zeroes(nums: list[int]) -> None:
#     # initialize zeroes count
#     num_zeroes = 0

#     # count all zeroes
#     for num in nums:
#         num_zeroes += 1 if num == 0 else num_zeroes

#     # new array with non zero numbers, keeping the same order
#     result = [num for num in nums if num != 0]

#     # using the count of zeroes, append zeroes to result
#     while num_zeroes > 0:
#         result.append(0)
#         num_zeroes -= 1

#     # replace all values in nums with result
#     for i in range(len(nums)):
#         nums[i] = result[i]


# Approach 2: Space Optimal, Operation Sub-Optimal
# ------------------------------------------------
# loop through once, moving all non zero elements to the front of the array
# while keeping track of the last non zero index + 1
# once first loop is done, replace remaining elements with zeroes, using
# last non zero index as start index
# def move_zeroes(nums: list[int]) -> None:
#     last_non_zero_index = 0

#     for index, num in enumerate(nums):
#         if num is not 0:
#             nums[last_non_zero_index] = nums[index]
#             last_non_zero_index += 1
#     for i in range(last_non_zero_index, len(nums)):
#         nums[i] = 0


# Approach 3: Optimal
# ------------------
# last approach is not optimal since you have to loop through once for
# something like [0, 0, 0, ...., 0, 1]
# realization: if current element is non zero, its correct position can be
# at best it's current position or one before. Since the current position
# will be occupied by a zero or non zero, we fill the position with a zero
# so it doesn't have to be revisited later
# 1. all elements before the slow pointer (last non zero index) are non zeroes
# 2. all elements between current and slow pointer are zeroes
# when we encounter a non zero element, we swap elements at both pointers
# then advance both pointers. If it's a zero, we just advance current pointer
def move_zeroes(nums: list[int]) -> None:
    last_non_zero_index = 0

    for current, num in enumerate(nums):
        if num != 0:
            nums[current] = 0
            nums[last_non_zero_index] = num
            last_non_zero_index += 1
    print(nums)


move_zeroes1 = move_zeroes([0, 1, 0, 3, 12])  # [1, 3, 12, 0, 0]
move_zeroes2 = move_zeroes([0])  # [0]
print(move_zeroes1)
print(move_zeroes2)
