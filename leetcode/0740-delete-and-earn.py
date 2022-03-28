##
#### 740. Delete and Earn (medium)
########################################


from collections import Counter


## reduce to house robber
##############################
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        points = [0] * (max(counts) + 1)

        for num in counts:
            points[num] += num * counts[num]

        prev = curr = 0

        for val in points:
            prev, curr = curr, max(curr, prev + val)

        return curr


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        points = {num: num * counts[num] for num in counts}
        prev = curr = 0

        for num in range(max(points) + 1):
            prev, curr = curr, max(curr, prev + points.get(num, 0))

        return curr


## dp
##############################
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        prev = None
        avoid = using = 0

        for k in sorted(counts):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * counts[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * counts[k] + avoid

            prev = k

        return max(avoid, using)


##
##############################
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().deleteAndEarn([3, 4, 2]), 6)
        self.assertEqual(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]), 9)


if __name__ == "__main__":
    unittest.main()
