##
#### Contains Duplicate (easy)
##################################

# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

#############################################################################

# naive
# ------
# nested loops
#
# time  - O(N^2) --> nested loops
# space - O(1) --> never used any extra space
# def contains_duplicate(nums: list[int]) -> bool:
#     for i, num in enumerate(nums):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False


# better
# ------
# hash map
def contains_duplicate(nums: list[int]) -> bool:
    hash_table = set()

    for num in nums:
        if num in hash_table:
            return True
        hash_table.add(num)

    return False


# Approach 2: Sorting
# ------------------
# if there are any duplicate integers, they will be consecutive after sorting
# sorting is often a good preprocessing step
# after sorting, we can sweep the sorted array to find if there are any
# two consecutive duplicate elements
#
# time - O(N log N) --> sorting is O(N log N) and sweeping is O(N)
# space - O(1) --> space depends on which sorting implementation, which usually,
# costs O(1) auxiliary space if heapsort is used
# *note: sorting modified the original array which is generally not good practice
# unless explicitly stated to do so - you can make a copy of nums and
# operate on the copy instead
# def contains_duplicate(nums: list[int]) -> bool:
#     nums.sort()

#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i + 1]:
#             return True

#     return False

# Approach 3: Hash Table
# def contains_duplicate(nums: list[int]) -> bool:
#     hash_table = set()

#     for num in nums:
#         if num in hash_table:
#             return True

#         hash_table.add(num)

#     return False


contains_duplicate1 = contains_duplicate([1, 2, 3, 1])  # true
contains_duplicate2 = contains_duplicate([1, 2, 3, 4])  # false
contains_duplicate3 = contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  # true
print(contains_duplicate1)
print(contains_duplicate2)
print(contains_duplicate3)
