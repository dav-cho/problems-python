##
#### Two Sum (easy)
#######################

# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

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

################################################################################

## brute force
##############################
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


## two-pass hash
##############################
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            seen[num] = i

        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen and seen[comp] != i:
                return [i, seen[comp]]


## one-pass hash
##############################
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]

            seen[num] = i


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(solution.twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(n^2) - For each element, we try to find its complement by looping
#                through the rest of the array which takes O(n) time. Therefore,
#                the time complexity is O(n^2).
# Space: O(1) - The space required does not depend on the size of the input
#               array, so only constant space is used.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


## Approach 2: Two-pass Hash Table
######################################
# Time: O(n) - We traverse the list containing nn elements exactly twice. Since
#              the hash table reduces the lookup time to O(1), the overall time
#              complexity is O(n).
# Space: O(n) - The extra space required depends on the number of items stored
#               in the hash table, which stores exactly n elements.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


## Approach 3: One-pass Hash Table
######################################
# Time: O(n) - We traverse the list containing nn elements only once. Each
#              lookup in the table costs only O(1) time.
# Space: O(n) - The extra space required depends on the number of items stored
#               in the hash table, which stores at most n elements.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
