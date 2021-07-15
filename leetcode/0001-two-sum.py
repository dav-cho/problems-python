##
#### Two Sum (easy)
#######################

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that
# is less than O(n2) time complexity?

##############################################################################

## 1: Brute Force
#####################
class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        pass


## 2: Two-pass Hash Table
#############################
class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        pass


## 3: One-pass Hash Table
#############################
class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        pass


def twoSum(nums: list[int], target: int) -> list[int]:
    compliments = {}
    for index, value in enumerate(nums):
        compliment = target - value
        if compliment in compliments:
            return [compliments[compliment], index]
        compliments[value] = index


## Approach 1: Brute Force
#############################
# time: O(n^2)
# space: O(1)

## Approach 2: Two-pass Hash Table
######################################
# time: O(n)
# space: O(n)

## Approach 3: One-pass Hash Table
######################################
# time: O(n)
# space: O(n)


twoSum1 = twoSum([2, 7, 11, 15], 9)  # [0, 1]
print("~ twoSum1", twoSum1)

twoSum2 = twoSum([3, 2, 4], 6)  # [1, 2]
print("~ twoSum2", twoSum2)

twoSum3 = twoSum([3, 3], 6)  # [0, 1]
print("~ twoSum3", twoSum3)
