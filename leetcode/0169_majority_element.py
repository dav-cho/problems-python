##
#### Majority Element (easy)
################################

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more
# than ⌊n / 2⌋ times. You may assume that the majority
# element always exists in the array.


# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1

# Follow-up: Could you solve the problem in linear time and in O(1) space?

##############################################################################

from collections import Counter


def majorityElement(nums: list[int]) -> int:
    count = Counter(nums)

    for num in count:
        if count[num] > len(nums) // 2:
            return num


# def majorityElement(nums: list[int]) -> int:
#     threshold = len(nums) // 2
#     seen = {}

#     for num in nums:
#         if num in seen:
#             seen[num] += 1
#         else:
#             seen[num] = 1

#     for num in seen:
#         if seen[num] > threshold:
#             return num


## Approach 1: Brute Force
##############################
# time: O(n^2) - nested loops
# space: O(1) - no additional space
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num


## Approach 2: HashMap
##########################
# time: O(n) - iterate over nums once and HashMap is constant time
# space: O(n) - nums array of length n will have a majority element occupying at
#               minimum n/2 + 1 indices. therefore, n - ([n/2] + 1) indices
#               occupied by distinct, non majority elements (+1 for majority
#               element itself), leaving us with at most
#               n - [n/2] distinct elements in the HashMap

# count the occurrences and return the max element
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


## Approach 3: Sorting
##########################
# time: O(n log(n)) - optimal
# space: O(1) or O(n) - O(1) if sorting in place is allowed
#                     - O(n) if we sort a copy of nums
# if elements are sorted in monotonically increasing (or decreasing) order,
# the majority element can be found at index [n/2] (and [n/2] + 1, if n i even).
# sort nums and return element in question
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


## Approach 4: Randomization
################################
# time: O(infinity)
# space: O(1)
import random


class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


test1 = [3, 2, 3]  # 3
test2 = [2, 2, 1, 1, 1, 2, 2]  # 2


def test(*args):
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = majorityElement(test)
            print(f"~ test {count}")
            print(f"result {count}: {result}")

    return run()


test(test1, test2)
