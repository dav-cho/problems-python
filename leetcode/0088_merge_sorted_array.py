##
#### 88. Merge Sorted Array (easy)
######################################


## 3 pointer start from end
###############################

## iterative
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


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


## recursive
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if not n:
            return

        if m > 0 and nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            self.merge(nums1, m - 1, nums2, n)
        else:
            nums1[m + n - 1] = nums2[n - 1]
            self.merge(nums1, m, nums2, n - 1)


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
