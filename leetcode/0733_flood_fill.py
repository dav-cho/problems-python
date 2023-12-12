##
#### 733. Flood Fill (easy)
###############################


## dfs
##############################
class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, newColor: int
    ) -> list[list[int]]:
        rows = len(image)
        cols = len(image[0])

        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(row, col):
            if image[row][col] == color:
                image[row][col] = newColor

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for x, y in directions:
                    if not 0 <= row + x < rows or not 0 <= col + y < cols:
                        continue

                    dfs(row + x, col + y)

        dfs(sr, sc)
        return image


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        )
        self.assertEqual(
            solution.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2), [[2, 2, 2], [2, 2, 2]]
        )


if __name__ == "__main__":
    unittest.main()
