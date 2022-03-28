##
#### 658. Find K Closest Elements (medium)
##############################################


from bisect import bisect_left


## binary search to find left bound
#######################################
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1

        return arr[left : left + k]


## binary search + sliding window
#####################################
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        if len(arr) == k:
            return arr

        left = bisect_left(arr, x) - 1
        right = left + 1

        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue

            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1 : right]


## sort w/ custom comparator
##############################
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        sorted_arr = sorted(arr, key=lambda num: abs(x - num))
        res = [sorted_arr[i] for i in range(k)]

        return sorted(res)


##
##############################
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4]
        )
        self.assertEqual(
            Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1), [1, 2, 3, 4]
        )


if __name__ == "__main__":
    unittest.main()
