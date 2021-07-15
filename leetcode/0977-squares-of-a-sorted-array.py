##
#### Squares of a Sorted Array (easy)
#########################################

# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
 
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
 
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
  
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 
# Follow up: Squaring each element and sorting the new array is very
# trivial, could you find an O(n) solution using a different approach?

################################################################################


## brute force
##################
class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        return sorted([num ** 2 for num in nums])


## O(n) solution
####################
class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        pass


## Tests
############

test1 = [-4, -1, 0, 3, 10]      # [0,1,9,16,100]
test2 = [-7, -3, 2, 3, 11]      # [4,9,9,49,121]

solution = Solution()
print(solution.sorted_squares(test1))
print(solution.sorted_squares(test2))
  

## LeetCode Solutions
#########################

## Approach 1: Sort
#######################
# time: 
# space: 

## Approach 2: Two Pointer
##############################
# time: 
# space: 

