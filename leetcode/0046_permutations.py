##
#### 46. Permutations (medium)
##################################


## backtracking
##############################
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        res = []

        def backtrack(first=0):
            if first == N:
                res.append(nums[:])

            for i in range(first, N):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

            return res

        return backtrack()


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()

        return res


## iterative
##############################
from collections import deque


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)

        if N == 1:
            return [nums]
        if N == 2:
            return [list(nums), list(nums)[::-1]]

        nums = deque(nums)
        res = deque()

        for _ in range(N):
            num = nums.popleft()
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)

            res += perms
            nums.append(num)

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.permute([1, 2, 3]),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )
        self.assertEqual(solution.permute([0, 1]), [[0, 1], [1, 0]])
        self.assertEqual(solution.permute([1]), [[1]])


if __name__ == "__main__":
    unittest.main()
