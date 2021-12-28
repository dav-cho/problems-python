##
#### Two Sum II - Input array is sorted (easy)
##################################################

# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= first < second <= numbers.length.

# Return the indices of the two numbers, index1 and index2, as an integer array
# [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.
 
# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

################################################################################

## best - two pointer
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            if curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1


## two pointer
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            if curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1


## one-pass hash
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [seen[comp], i + 1]

            seen[num] = i + 1


## two-pass hash
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(numbers):
            seen[num] = i
        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [i + 1, seen[comp] + 1]

## brute force
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]


## first attempt - one pass hash
####################################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [seen[comp], i + 1]

            seen[num] = i + 1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2,7,11,15], 9), [1,2])
        self.assertEqual(solution.twoSum([2,3,4], 6), [1,3])
        self.assertEqual(solution.twoSum([-1,0], -1), [1,2])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Two Pointers
###############################
# Time: O(n) - The input array is traversed at most once. Thus the time
#              compexity is O(n)
# Space: O(1) - We only use additional space to store two indices and the sum,
#               so the space complexity is O(1).

## C++
#class Solution {
#public:
#    vector<int> twoSum(vector<int>& numbers, int target) {
#        int low = 0;
#        int high = numbers.size() - 1;
#        while (low < high) {
#            int sum = numbers[low] + numbers[high];
#                          
#            if (sum == target) {
#                return {low + 1, high + 1};
#            } else if (sum < target) {
#                ++low;
#            } else {
#                --high;
#            }
#        }
#        // In case there is no solution, return {-1, -1}.
#        return {-1, -1};
#    }
#};


