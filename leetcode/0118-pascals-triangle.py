##
#### 118. Pascal's Triangle (easy)
########################################


## dynamic programming
##############################
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []

        for row in range(numRows):
            curr = [None for _ in range(row + 1)]
            curr[0] = curr[-1] = 1

            for i in range(1, len(curr) - 1):
                prev_row = res[row - 1]
                curr[i] = prev_row[i - 1] + prev_row[i]

            res.append(curr)

        return res


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []

        for row in range(numRows):
            curr = [None for _ in range(row + 1)]
            curr[0] = curr[-1] = 1

            for i in range(1, row):
                curr[i] = res[-1][i - 1] + res[-1][i]

            res.append(curr)

        return res


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []

        for row in range(numRows):
            curr = [None for _ in range(row + 1)]
            curr[0] = curr[-1] = 1

            for i in range(1, row):
                prev_row = res[row - 1]
                curr[i] = prev_row[i - 1] + prev_row[i]

            res.append(curr)

        return res


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []

        for row in range(numRows):
            curr = [None for _ in range(row + 1)]
            curr[0] = curr[-1] = 1

            for i in range(1, row):
                curr[i] = res[row - 1][i - 1] + res[row - 1][i]

            res.append(curr)

        return res


## offset sum of previous row
#################################
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]

        for i in range(1, numRows):
            a = [0] + res[-1]
            b = res[-1] + [0]
            res.append([a[i] + b[i] for i in range(len(a))])

        return res


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]

        for row in range(1, numRows):
            res += [list(map(lambda a, b: a + b, [0] + res[-1], res[-1] + [0]))]

        return res


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        def generate_next_row():
            a = [0] + res[-1]
            b = res[-1] + [0]

            return [a[i] + b[i] for i in range(len(a))]

        res = [[1]]

        for row in range(1, numRows):
            res.append(generate_next_row())

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().generate(5),
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        )
        self.assertEqual(Solution().generate(1), [[1]])


if __name__ == "__main__":
    unittest.main()
