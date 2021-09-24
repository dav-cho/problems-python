##
#### Rotate Array (medium)
##############################

# Given an array, rotate the array to the right by k steps,
# where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

# Follow up:
# Try to come up with as many solutions as you can. There are
# at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

################################################################################

## brute force(TLE)
##############################
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]


## extra array
##############################
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a


## cyclic replacements
##############################
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            curr, prev = start, nums[start]
            while True:
                next_idx = (curr + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1

                if curr == start:
                    break
            start += 1


## reverse
##############################
class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.rotate([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])
        self.assertEqual(solution.rotate([-1,-100,3,99], 2), [3,99,-1,-100])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(n * k) - All the numbers are shifted by one step(O(n)) k times.
# Space: O(1) - No extra space is used.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]


## Approach 2: Using Extra Array
####################################
# Time: O(n) - One pass is used to put the numbers in the new array. And another
#              pass to copy the new array to the original one.
# Space: O(n) - Another array of the same size is used.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a


## Approach 3: Using Cyclic Replacements
############################################
# Time: O(n) - Only one pass is used.
# Space: O(1) - Constant extra space is used.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1


## Approach 4: Using Reverse
################################
# Time: O(n) - n elements are reversed a total of three times.
# Space: O(1) - No extra space is used.
class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
