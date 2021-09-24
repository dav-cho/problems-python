##
#### Remove Duplicates from Sorted Array (easy)
###################################################

# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element
# appears only once. The relative order of the elements should
# be kept the same.

# Since it is impossible to change the length of the array in some
# languages, you must instead have the result be placed in the first
# part of the array nums. More formally, if there are k elements after
# removing the duplicates, then the first k elements of nums should
# hold the final result. It does not matter what you leave beyond
# the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this
# by modifying the input array in-place with O(1) extra memory.

# Custom Judge:
# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two
#              elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k
# (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first
#              five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k
# (hence they are underscores).

# Constraints:
# 0 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

################################################################################

## two pointers
##############################
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                
        return k


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicates([1,1,2]), 2)
        # nums = [1,2,_]
        self.assertEqual(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5)
        # nums = [0,1,2,3,4,_,_,_,_,_]


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Two Pointers
##############################
# Time: O(n) - Assume that n is the length of array. Each of i and j traverses
#              at most n steps.
# Space: O(1)

## Java
#public int removeDuplicates(int[] nums) {
#    if (nums.length == 0) return 0;
#    int i = 0;
#    for (int j = 1; j < nums.length; j++) {
#        if (nums[j] != nums[i]) {
#            i++;
#            nums[i] = nums[j];
#        }
#    }
#    return i + 1;
#}


