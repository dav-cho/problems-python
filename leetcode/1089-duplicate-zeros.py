##
#### Duplicate Zeros (easy)
###############################

# Given a fixed length array arr of integers, duplicate
# each occurrence of zero, shifting the remaining
# elements to the right.

# Note that elements beyond the length of the
# original array are not written.

# Do the above modifications to the input array in place,
# do not return anything from your function.

# Example 1:
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function,
# the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function,
# the input array is modified to: [1,2,3]

# Note:
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9

##########################################################################


## nested loops
###################
# time: O(n^2)
# space: O(1)
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                for j in range(len(arr) - 1, i, -1):
                    arr[j] = arr[j - 1]

                arr[i + 1] = 0
                i += 2

            else:
                i += 1


## two pass
###############
# time: O(n)
# space: O(1)
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeroes, i, last = 0, 0, len(arr) - 1

        while i <= last:
            if arr[i] == 0:
                if i == last:
                    arr[-1] = 0
                    last -= 1
                    break

                zeroes += 1
                last -= 1

            i += 1

        for j in range(last, -1, -1):
            if arr[j] == 0:
                arr[j + zeroes] = 0
                zeroes -= 1
                arr[j + zeroes] = 0
            else:
                arr[j + zeroes] = arr[j]


## Tests
############

test1 = [1, 0, 2, 3, 0, 4, 5, 0]
test2 = [1, 2, 3]
test3 = [8, 4, 5, 0, 0, 0, 0, 7]
test4 = [1, 5, 2, 0, 6, 8, 0, 6, 0]
#        0  1  2  3  4  5  6  7  8

solution = Solution()

solution.duplicateZeros(test1)
print(test1)  # [1,0,0,2,3,0,0,4]

solution.duplicateZeros(test2)
print(test2)  # [1,2,3]

solution.duplicateZeros(test3)
print(test3)  # [8, 4, 5, 0, 0, 0, 0, 0]

solution.duplicateZeros(test4)
print(test4)  # [1, 5, 2, 0, 0, 6, 8, 0, 0]

## LeetCode Solutions
#########################


## Approach 1: Two Pass, O(1) Space
#######################################
# time: O(n) - where n is number of elements in array
# space: O(1) - no extra space used
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    arr[length_] = 0  # For this zero we copy without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]


## Tests
############

test1 = [1, 0, 2, 3, 0, 4, 5, 0]
test2 = [1, 2, 3]
test3 = [8, 4, 5, 0, 0, 0, 0, 7]
#        0  1  2  3  4  5  6  7

solution = Solution()

print("LeetCode")
solution.duplicateZeros(test1)
print(test1)  # [1,0,0,2,3,0,0,4]

solution.duplicateZeros(test2)
print(test2)  # [1,2,3]

solution.duplicateZeros(test3)
print(test3)  # [8, 4, 5, 0, 0, 0, 0, 0]
