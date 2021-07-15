##
#### Valid Mountain Array (easy)
####################################

# Given an array of integers arr, return true if
# and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true

# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

###################################################################


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        i, last = 0, len(arr) - 1

        while i < last and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == last:
            return False

        while i < last and arr[i] > arr[i + 1]:
            i += 1

        return i == last


## Tests
############

test1 = [2, 1]  # False
test2 = [3, 5, 5]  # False
test3 = [0, 3, 2, 1]  # True

tests = [test1, test2, test3]


def test(*args):
    solution = Solution()
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            print(test)

            result = solution.validMountainArray(test)

            print(result)

    return run()


test(*tests)


## LeetCode Solutions
#########################

## Approach 1: One Pass
###########################
# time: O(n) - where n is length of array
# space: O(1) - no additional space used
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False

        # walk down
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1
