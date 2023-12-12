##
#### 77. Combinations (medium)
##################################


## backtracking
##############################
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                res.append(curr[:])

            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        res = []
        backtrack()
        return res


## lexicogrpahic
##############################
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = list(range(1, k + 1)) + [n + 1]
        res, j = [], 0
        while j < k:
            res.append(nums[:k])
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        # self.assertEqual(solution.combine(4, 2), [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]])
        # self.assertEqual(solution.combine(1, 1), [[1]])


if __name__ == "__main__":
    unittest.main()
