##
#### 119. Pascal's Triangle II (easy)
#########################################


# f(i, j) = f(i - 1, j - 1) + f (i - 1, j)
# recursive base case:
#       f(i, j) = 1 where j = 1 or j = i


## brute force recursion
##############################
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = []
        for i in range(rowIndex + 1):
            row.append(self.get_num(rowIndex, i))

        return row

    def get_num(self, row, col):
        if row == 0 or col == 0 or row == col:
            return 1

        return self.get_num(row - 1, col - 1) + self.get_num(row - 1, col)


## dynamic programming
##############################
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        return row


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]

        return row


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]

        return row


## math (combinatorics)
##############################
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        return [math.comb(rowIndex, i) for i in range(rowIndex + 1)]


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = []
        for i in range(rowIndex + 1):
            row.append(math.comb(rowIndex, i))

        return row


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.getRow(3), [1, 3, 3, 1])
        self.assertEqual(solution.getRow(0), [1])
        self.assertEqual(solution.getRow(1), [1, 1])


if __name__ == "__main__":
    unittest.main()
