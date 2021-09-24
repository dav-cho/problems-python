##
#### Single Number (easy)
########################################

# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears
# only once.

################################################################################

## bit manipulation
##############################
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0

        for num in nums:
            x ^= num

        return x


## math
##############################
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)


## hash table
##############################
from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = Counter(nums)

        for num, count in counts.items():
            if count == 1:
                return num


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([2,2,1]), 1)
        self.assertEqual(solution.singleNumber([4,1,2,1,2]), 4)
        self.assertEqual(solution.singleNumber([1]), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: List operation
#################################
# Time: O(n^2) - We iterate through nums, taking O(n) time. We search the whole
#                list to find whether there is duplicate number, taking O(n)
#                time. Because search is in the for loop, so we have to multiply
#                both time complexities which is O(n^2).
# Space: O(n) - We need a list of size n to contain elements in nums.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


## Approach 2: Hash Table
##############################
# Time: O(n⋅1)=O(n) - Time complexity of for loop is O(n). Time complexity of
#                     hash table(dictionary in python) operation pop is O(1).
# Space: O(n) - The space required by hash_table is equal to the number of
#               elements in nums.
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i


## Approach 3: Math
##############################
# Time: O(n+n)=O(n) - Sum will call next to iterate through nums. We can see it
#                     as sum(list(i, for i in nums)) which means the time
#                     complexity is O(n) because of the number of elements(n)
#                     in nums.
# Space: O(n+n)=O(n) - Set needs space for the elements in nums.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


## Approach 4: Bit Manipulation
###################################
# Time: O(n) - We only iterate through nums, so the time complexity is the
#              number of elements in nums.
# Space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

# For anyone who didn't understood why this works here is an explanation. This
# XOR operation works because it's like XORing all the numbers by itself. So if
# the array is {2,1,4,5,2,4,1} then it will be like we are performing this
# operation:
# ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.
# Hence picking the odd one out ( 5 in this case).

# A better explanation why this technique works-
# Let's say we have an array - [2,1,4,5,2,4,1].
# What we are doing is essentially this-
# => 0 ^ 2 ^ 1 ^ 4 ^ 5 ^ 2 ^ 4 ^ 1
# => 0^ 2^2 ^ 1^1 ^ 4^4 ^5 (Rearranging, taking same numbers together)
# => 0 ^ 0 ^ 0 ^ 0 ^ 5
# => 0 ^ 5
# => 5 :)


