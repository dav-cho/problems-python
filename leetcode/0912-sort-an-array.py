##
#### 912. Sort an Array (medium)
########################################


## merge sort
##############################
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])

        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        p_left = p_right = 0
        while p_left < len(left) and p_right < len(right):
            if left[p_left] < right[p_right]:
                res.append(left[p_left])
                p_left += 1
            else:
                res.append(right[p_right])
                p_right += 1

        res += left[p_left:]
        res += right[p_right:]

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.sortArray([5, 2, 3, 1]), [1, 2, 3, 5])
        self.assertEqual(solution.sortArray([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])


if __name__ == "__main__":
    unittest.main()
