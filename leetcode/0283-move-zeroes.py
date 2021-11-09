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


## *best
##############################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1


## operation sub-optimal, space sub-optimal
###############################################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zeroes = nums.count(0)
        res = []
        
        for num in nums:
            if num != 0:
                res.append(num)
                
        while zeroes:
            res.append(0)
            zeroes -= 1
            
        for i in range(len(nums)):
            nums[i] = res[i]

        return nums


## space optimal
##############################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
                
        for i in range(k, len(nums)):
            nums[i] = 0

        return nums


## optimal
##############################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1

        return nums


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1

        return nums


## first attempt
##############################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        
        for i in range(k, len(nums)):
            nums[i] = 0

        return nums


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.moveZeroes([0,1,0,3,12]), [1,3,12,0,0])
        self.assertEqual(solution.moveZeroes([0]), [0])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: (Space Sub-Optimal) [Accepted]
#################################################
# Time: O(n) - However, the total number of operations are sub-optimal. We can
#              achieve the same result in less number of operations.
#            - If asked in an interview, the above solution would be a good
#              start. You can explain the interviewer(not code) the above and
#              build your base for the next Optimal Solution.
# Space: O(n) - Since we are creating the "ans" array to store results.

## C++
#void moveZeroes(vector<int>& nums) {
#    int n = nums.size();
#
#    // Count the zeroes
#    int numZeroes = 0;
#    for (int i = 0; i < n; i++) {
#        numZeroes += (nums[i] == 0);
#    }
#
#    // Make all the non-zero elements retain their original order.
#    vector<int> ans;
#    for (int i = 0; i < n; i++) {
#        if (nums[i] != 0) {
#            ans.push_back(nums[i]);
#        }
#    }
#
#    // Move all zeroes to the end
#    while (numZeroes--) {
#        ans.push_back(0);
#    }
#
#    // Combine the result
#    for (int i = 0; i < n; i++) {
#        nums[i] = ans[i];
#    }
#}


## Approach 2: (Space Optimal, Operation Sub-Optimal) [Accepted]
####################################################################
# Time: O(n) - However, the total number of operations are still sub-optimal.
#              The total operations (array writes) that code does is n (Total
#              number of elements).
# Space: O(1) - Only constant space is used.

## C++
#void moveZeroes(vector<int>& nums) {
#    int lastNonZeroFoundAt = 0;
#    // If the current element is not 0, then we need to
#    // append it just in front of last non 0 element we found. 
#    for (int i = 0; i < nums.size(); i++) {
#        if (nums[i] != 0) {
#            nums[lastNonZeroFoundAt++] = nums[i];
#        }
#    }
# 	// After we have finished processing new elements,
# 	// all the non-zero elements are already at beginning of array.
# 	// We just need to fill remaining array with 0's.
#    for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
#        nums[i] = 0;
#    }
#}


## Approach 3: (Optimal) [Accepted]
#######################################
# Time: O(n) - However, the total number of operations are optimal. The total
#              operations (array writes) that code does is Number of non-0
#              elements.This gives us a much better best-case (when most of the
#              elements are 0) complexity than last solution. However, the
#              worst-case (when all elements are non-0) complexity for both the
#              algorithms is same.
# Space: O(1) - Only constant space is used.

## C++
#void moveZeroes(vector<int>& nums) {
#    for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
#        if (nums[cur] != 0) {
#            swap(nums[lastNonZeroFoundAt++], nums[cur]);
#        }
#    }
#}


