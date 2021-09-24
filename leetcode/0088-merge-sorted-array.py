##
#### Merge Sorted Array (easy)
##################################

# You are given two integer arrays nums1 and nums2, sorted in
# non-decreasing order, and two integers m and n, representing
# the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1. To accommodate this,
# nums1 has a length of m + n, where the first m elements denote the
# elements that should be merged, and the last n elements are set to 0
# and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the
# underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1.
# The 0 is only there to ensure the merge result can fit in nums1.

# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

################################################################################

## 3 pointer start from end
###############################
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, j = m - 1, n - 1

        for k in range(n + m - 1, -1, -1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1


## 3 pointer start from beginning
#####################################
# time: O(n) - iterate through list atleast once
# space: O(n) - copy of nums1 used --> O(m) --> O(n)
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return

        nums1_copy = nums1[:m]
        i = j = k = 0

        while i < len(nums1_copy) and j < len(nums2):
            if nums1_copy[i] < nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < len(nums1_copy) and j >= len(nums2):
            nums1[k] = nums1_copy[i]
            i += 1
            k += 1

        while j < len(nums2) and i >= len(nums1_copy):
            nums1[k] = nums2[j]
            j += 1
            k += 1


# 3 pointer from beginning refactored
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1_copy = nums1[:m]
        i = j = k = 0

        for k in range(n + m):
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1


## sorting
##############################
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, j = m, 0
        
        while i < m + n and j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
            
        nums1.sort()

## Tests
############

# (nums1, nums2, m, n)
test1 = ([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3)  # [1, 2, 2, 3, 5, 6]
test2 = ([1], [], 1, 0)  # [1]
test3 = ([0], [1], 0, 1)  # [1]


def test(*args):
    solution = Solution()
    count = 1

    def run():
        for test in args:
            nums1, nums2, m, n = test

            solution.merge(nums1, m, nums2, n)

            nonlocal count
            print(f"test {count}")
            count += 1
            print(nums1)

    return run()


test(test1, test2, test3)


## LeetCode Solutions
#########################

## Approach 1: Merge Sort
#############################
# time: O(n log(n)) - O(n + m) to combine arrays and O(x log(x)) to sort
#                     O((n + m) log(n + m)) --> O(n log(n))
# space: O(n) - built in sort usually uses O(n) space
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]

        # Sort nums1 list in-place.
        nums1.sort()


## Approach 2: Three Pointers (Start from Beginning)
########################################################
# time: O(n) --> O(n + m)
# space: O(m) - use an additional array of length m
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0

        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


## Approach 3: Three Pointers (Start From the End)
######################################################
# time: O(n) --> O(n + m)
# space: O(1) - no additional space used
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


## Tests
############

# (nums1, nums2, m, n)
test1 = ([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3)  # [1, 2, 2, 3, 5, 6]
test2 = ([1], [], 1, 0)  # [1]
test3 = ([0], [1], 0, 1)  # [1]


def test(*args):
    solution = Solution()
    count = 1

    def run():
        for test in args:
            nums1, nums2, m, n = test

            solution.merge(nums1, m, nums2, n)

            nonlocal count
            print(f"test {count}")
            count += 1
            print(nums1)

    return run()


test(test1, test2, test3)
