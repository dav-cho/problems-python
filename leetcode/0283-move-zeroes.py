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

## Approach 1: Space Sub-Optimal
####################################
# time: O(n) - since we create the ans array to store results
# space: O(n)
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


## Approach 2: Space Optimal, Operation Sub-Optimal
#######################################################
# time: O(1)
# space: O(n) - total operations (array writes) is n (total # of elements)
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        for j in range(i, len(nums)):
            nums[j] = 0


## Approach 3: Optimal
##########################
# time: O(1)
# space: O(n) - total # of operations are optimal because total num of
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                curr = nums[j]
                nums[j] = 0
                nums[i] = curr
                i += 1


## Tests
############
test = Solution()
move_zeroes1 = test.moveZeroes([0, 1, 0, 3, 12])  # [1, 3, 12, 0, 0]
move_zeroes2 = test.moveZeroes([0])  # [0]
print(move_zeroes1)
print(move_zeroes2)


## LeetCode Solutions
#########################


## Approach 1: Space Sub-Optimal
####################################
# time: O(n) - since we create the ans array to store results
# space: O(n)
class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        # initialize zeroes count
        num_zeroes = 0

        # count all zeroes
        for num in nums:
            num_zeroes += 1 if num == 0 else num_zeroes

        # new array with non zero numbers, keeping the same order
        result = [num for num in nums if num != 0]

        # using the count of zeroes, append zeroes to result
        while num_zeroes > 0:
            result.append(0)
            num_zeroes -= 1

        # replace all values in nums with result
        for i in range(len(nums)):
            nums[i] = result[i]


## C++
# void moveZeroes(vector<int>& nums) {
#     int n = nums.size();

#     // Count the zeroes
#     int numZeroes = 0;
#     for (int i = 0; i < n; i++) {
#         numZeroes += (nums[i] == 0);
#     }

#     // Make all the non-zero elements retain their original order.
#     vector<int> ans;
#     for (int i = 0; i < n; i++) {
#         if (nums[i] != 0) {
#             ans.push_back(nums[i]);
#         }
#     }

#     // Move all zeroes to the end
#     while (numZeroes--) {
#         ans.push_back(0);
#     }

#     // Combine the result
#     for (int i = 0; i < n; i++) {
#         nums[i] = ans[i];
#     }
# }


## Approach 2: Space Optimal, Operation Sub-Optimal
#######################################################
# time: O(1)
# space: O(n) - total operations (array writes) is n (total # of elements)
# loop through once, moving all non zero elements to the front of the array
# while keeping track of the last non zero index + 1
# once first loop is done, replace remaining elements with zeroes, using
# last non zero index as start index
def move_zeroes(nums: list[int]) -> None:
    last_non_zero_index = 0

    for index, num in enumerate(nums):
        if num is not 0:
            nums[last_non_zero_index] = nums[index]
            last_non_zero_index += 1
    for i in range(last_non_zero_index, len(nums)):
        nums[i] = 0


## C++
# void moveZeroes(vector<int>& nums) {
#     int lastNonZeroFoundAt = 0;
#     // If the current element is not 0, then we need to
#     // append it just in front of last non 0 element we found.
#     for (int i = 0; i < nums.size(); i++) {
#         if (nums[i] != 0) {
#             nums[lastNonZeroFoundAt++] = nums[i];
#         }
#     }
#  	// After we have finished processing new elements,
#  	// all the non-zero elements are already at beginning of array.
#  	// We just need to fill remaining array with 0's.
#     for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
#         nums[i] = 0;
#     }
# }


## Approach 3: Optimal
##########################
# time: O(1)
# space: O(n) - total # of operations are optimal because total num of
#               operations is number of non-0 elements. This gives us a
#               much better best case than appraoch 2. However, worst case
#               is the same.
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
class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        last_non_zero_index = 0

        for current, num in enumerate(nums):
            if num != 0:
                nums[current] = 0
                nums[last_non_zero_index] = num
                last_non_zero_index += 1
        print(nums)


## C++
# void moveZeroes(vector<int>& nums) {
#     for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
#         if (nums[cur] != 0) {
#             swap(nums[lastNonZeroFoundAt++], nums[cur]);
#         }
#     }
# }
