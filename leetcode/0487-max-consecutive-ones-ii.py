##
#### Max Consecutive Ones II (medium)
#########################################

# Given a binary array nums, return the maximum number of consecutive
# 1's in the array if you can flip at most one 0.
 
# Example 1:
# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the maximum number
# of consecutive 1s. After flipping, the maximum number of
# consecutive 1s is 4.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 4

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
 
# Follow up: What if the input numbers come in one by one as an
# infinite stream? In other words, you can't store all numbers coming
# from the stream as it's too large to hold in memory.
# Could you solve it efficiently?

################################################################################


## sliding window - two pointers
class Solution:
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        left = right = mx = zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1

                left += 1

            mx = max(mx, right - left + 1)
            right += 1

        return mx


## Tests
############

test1 = [1, 0, 1, 1, 0]     # 4
test2 = [1, 0, 1, 1, 0, 1]  # 4
test3 = [1, 1, 0, 1]        # 4

solution = Solution()
print(solution.find_max_consecutive_ones(test1))
print(solution.find_max_consecutive_ones(test2))
print(solution.find_max_consecutive_ones(test3))


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# time: O(n^2) - nested loops make a quadratic solution
# space: O(1) - no additional space used
# Check every possible consecutive sequence.
# Count how many 0's are in each sequence.
# If our sequence has one or fewer 0's, check if that's the
# longest consecutive sequence of 1's.
# Interview Tip: Often times the interviewer doesn't need to see you code
# the brute force solution. State the brute force approach out loud and
# discuss his/her expectations. Either way, communicating proactively will
# give you major bonus points.
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        longest_sequence = 0
        for left in range(len(nums)):
            num_zeroes = 0
            for right in range(left, len(nums)):   # check every consecutive sequence
                if num_zeroes == 2:
                    break
                if nums[right] == 0:               # count how many 0's
                    num_zeroes += 1
                if num_zeroes <= 1:                 # update answer if it's valid
                    longest_sequence = max(longest_sequence, right - left + 1)
        return longest_sequence


## Approach 2: Sliding Window
#################################
# time: O(n) - both pointers only move forward a max of n steps
# space: O(1) - no additional space used
# While our window is in bounds of the array:
# - Add the rightmost element to our window
# - Check if our window is invalid. If so, contract the window until valid.
# - Update our the longest sequence we've seen so far
# - Continue to expand our window
# Valid State = one or fewer 0's in our current sequence
# Invalid State = two 0's in our current sequence
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        longest_sequence = 0
        left, right = 0, 0
        num_zeroes = 0

        # while our window is in bounds
        while right < len(nums):
            # add the right most element into our window
            if nums[right] == 0:
                num_zeroes += 1

            # if our window is invalid, contract our window
            while num_zeroes == 2:
                if nums[left] == 0:    
                    num_zeroes -= 1
                left += 1

            # update our longest sequence answer
            longest_sequence = max(longest_sequence, right - left + 1)
            right += 1   # expand our window

        return longest_sequence


lc_solution = Solution()
print(lc_solution.findMaxConsecutiveOnes(test1))
print(lc_solution.findMaxConsecutiveOnes(test2))
print(lc_solution.findMaxConsecutiveOnes(test3))

