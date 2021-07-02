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

# naive
# ------
# slice last k elements from array and slice front
# concatenate in reverse order
#
# time - O(N) --> must loop through atleast once
# space - O(N + M) --> O(N) --> use two new arrays
def rotate(nums: list[int], k: int) -> None:
    k %= len(nums)
    front = nums[:-k]
    back = nums[-k:]
    result = back + front
    for i in range(len(result)):
        nums[i] = result[i]


# Approach 1: Brute Force
# ----------------------
# rotate all elements in the array in k steps by rotating elements
# by 1 unit each step
#
# time - O(N x K) --> O(N) - all elements are only moved k times (must loop
# through atleast once)
# space - O(1) --> no extra space used
def rotate(nums: list[int], k: int) -> None:
    # speed up rotation and eliminate unecessary rotations
    # also works for edge cases where k > length of array
    k %= len(nums)

    for i in range(k):
        # save the value of the last element
        previous = nums[-1]
        for j in range(len(nums)):
            # swap last element with current element
            nums[j], previous = previous, nums[j]


# Approach 2: Using Extra Array
# ----------------------------
# place every element at correct position in new array
# then copy new array into nums
# time - O(N + M) --> O(N) - one pass to place numbers in new array and another
# to copy the array into nums
# space - O(N) --> needs another array of the same size
def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    a = [0] * n

    for i in range(n):
        a[(i + k) % n] = nums[i]

    # nums[:] = a
    nums = a


# Approach 3: Using Cyclic Replacements
# ------------------------------------
#
def rotate(nums: list[int], k: int) -> None:
    length = len(nums)
    k %= length

    start = count = 0

    while count < length:
        current, previous = start, nums[start]

        while True:
            next_index = (current + k) % length
            nums[next_index], previous = previous, nums[next_index]
            current = next_index
            count += 1

            if start == current:
                break

        start += 1


rotate1 = rotate([1, 2, 3, 4, 5, 6, 7], 3)  # [5,6,7,1,2,3,4]
rotate2 = rotate([-1, -100, 3, 99], 2)  # [3,99,-1,-100]
print(rotate1)
print(rotate2)
