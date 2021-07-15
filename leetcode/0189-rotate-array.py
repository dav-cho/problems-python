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

## naive
############
class Solution:
    def rotate(nums: list[int], k: int) -> None:
        k %= len(nums)
        front = nums[:-k]
        back = nums[-k:]
        result = back + front
        for i in range(len(result)):
            nums[i] = result[i]


## Approach 1: Brute Force
##############################
# time: O(N)
# space: O(1)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        pass


## Approach 2: Using Extra Array
####################################
# time: O(N)
# space: O(N)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        pass


## Approach 3: Using Cyclic Replacements
############################################
# time: O(n)
# space: O(n)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        pass


## Approach 4: Use Reverse
##############################
# time: O(n)
# space: O(1)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        pass


test = Solution()
rotate1 = test.rotate([1, 2, 3, 4, 5, 6, 7], 3)  # [5,6,7,1,2,3,4]
rotate2 = test.rotate([-1, -100, 3, 99], 2)  # [3,99,-1,-100]
print(rotate1)
print(rotate2)


## LeetCode Solutions
#########################


## Approach 1: Brute Force
##############################
# time: O(N x K) --> O(N) - all elements are only moved k times (must loop
# through atleast once)
# space: O(1) --> no extra space used
#
# rotate all elements in the array in k steps by rotating elements
# by 1 unit each step
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]


## Approach 2: Using Extra Array
####################################
# time: O(N + M) --> O(N) - one pass to place numbers in new array and another
# to copy the array into nums
# space: O(N) --> needs another array of the same size
#
# place every element at correct position in new array
# then copy new array into nums
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a


## Approach 3: Using Cyclic Replacements
############################################
# time: O(n) - one pass used to put the numbers in the new array and another pass
#              to copy the new array to original one
# space: O(n) - another array of same size is used.
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
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


## Approach 4: Use Reverse
##############################
# time: O(n) - n elements are reversed a total of three times
# space: O(1) - no extra space is used
class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


test = Solution()
rotate1 = test.rotate([1, 2, 3, 4, 5, 6, 7], 3)  # [5,6,7,1,2,3,4]
rotate2 = test.rotate([-1, -100, 3, 99], 2)  # [3,99,-1,-100]
print(rotate1)
print(rotate2)
