##
#### Remove Element (easy)
##############################

# Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

# Since it is impossible to change the length of the array
# in some languages, you must instead have the result be placed
# in the first part of the array nums. More formally, if there
# are k elements after removing the duplicates, then the first
# k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this
# by modifying the input array in-place with O(1) extra memory.

# Custom Judge:
# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.
# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2,
#              with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k
# (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first
#              five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k
# (hence they are underscores).

# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

########################################################################

## Approach 1: Two Pointers
###############################
# time:
# space:
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


## Approach 2: Two Pointers - when elements to remove are rare
##################################################################
# time:
# space:
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, length = 0, len(nums)

        while i < length:
            if nums[i] == val:
                nums[i] = nums[length - 1]
                length -= 1
            else:
                i += 1

        return length


## Tests
############

test1 = ([3, 2, 2, 3], 3)  # 2, [2,2,_,_]
test2 = ([0, 1, 2, 2, 3, 0, 4, 2], 2)  # 5, [0,1,4,0,3,_,_,_]
test3 = ([1], 1)  # 0, []
test4 = ([2], 3)  # 1, [2]
test5 = ([3, 3], 3)  # 0, []
test6 = ([], 0)  # 0, []
test7 = ([3, 3], 5)  # 2, [3, 3]
test8 = ([2, 2, 3], 2)  # 1, [3]
test9 = ([0, 4, 4, 0, 4, 4, 4, 0, 2], 4)  # 4, [0, 2, 0, 0]


def test(*args):
    solution = Solution()
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            print("before:", *test)

            result = solution.removeElement(*test)
            count += 1

            print("after:", test[0][:result])
            print("return:", result)

        print("FINISHED")

    return run()


test(test1, test2, test3, test4, test5, test6, test7, test8, test9)

## LeetCode Solutions
#########################

## Approach 1: Two Pointers
###############################
# time: O(n) - both i and j traverse at most 2n steps
# space: O(1) - no extra space used
## Java
# public int removeElement(int[] nums, int val) {
#     int i = 0;
#     for (int j = 0; j < nums.length; j++) {
#         if (nums[j] != val) {
#             nums[i] = nums[j];
#             i++;
#         }
#     }
#     return i;
# }

## Approach 2: Two Pointers - when elements to remove are rare
##################################################################
# time: O(n) - both i and n traverse at most n steps. In this approach,
#              the number of assignments operations is equal to number of
#              elements to remove, so it is more efficient if elements
#              to remove are rare
# space: O(1)
## Java
# public int removeElement(int[] nums, int val) {
#     int i = 0;
#     int n = nums.length;
#     while (i < n) {
#         if (nums[i] == val) {
#             nums[i] = nums[n - 1];
#             // reduce array size by one
#             n--;
#         } else {
#             i++;
#         }
#     }
#     return n;
# }
