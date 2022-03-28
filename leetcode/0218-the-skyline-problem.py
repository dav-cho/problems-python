##
#### 218. The Skyline Problem (hard)
########################################


## divide and conquer
##############################
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        left = self.getSkyline(buildings[: n // 2])
        right = self.getSkyline(buildings[n // 2 :])

        return self.merge_skylines(left, right)

    def merge_skylines(self, left, right):
        def update_output(x, y):
            if not res or res[-1][0] != x:
                res.append([x, y])
            else:
                res[-1][1] = y

        def append_skyline(p, lst, n, y, curr_y):
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_left, n_right = len(left), len(right)
        p_left = p_right = 0
        curr_y = left_y = right_y = 0
        res = []

        while p_left < n_left and p_right < n_right:
            point_left, point_right = left[p_left], right[p_right]
            if point_left[0] < point_right[0]:
                x, left_y = point_left
                p_left += 1
            else:
                x, right_y = point_right
                p_right += 1

            max_y = max(left_y, right_y)
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        append_skyline(p_left, left, n_left, left_y, curr_y)
        append_skyline(p_right, right, n_right, right_y, curr_y)

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.getSkyline(
                [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
            ),
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
        )
        self.assertEqual(solution.getSkyline([[0, 2, 3], [2, 5, 3]]), [[0, 3], [5, 0]])


if __name__ == "__main__":
    unittest.main()
