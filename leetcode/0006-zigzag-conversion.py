##
#### 6. Zigzag Conversion (medium)
########################################

##
##############################
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass


## first attempt
##############################
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [[] for _ in range(numRows)]

        row = 0
        up = numRows - 2
        for char in s:
            if row < numRows:
                zigzag[row].append(char)
                row += 1
            else:
                if up > 0:
                    zigzag[up].append(char)
                    up -= 1
                else:
                    zigzag[0].append(char)
                    row = 1
                    up = numRows - 2

        res = ""
        for row in zigzag:
            res += "".join(row)

        return res


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ["" for _ in range(numRows)]

        row = 0
        up = numRows - 2
        for char in s:
            if row < numRows:
                res[row] += char
                row += 1
            else:
                if up > 0:
                    res[up] += char
                    up -= 1
                else:
                    res[0] += char
                    row = 1
                    up = numRows - 2

        return "".join(res)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [[] for _ in range(numRows)]
        row = 0
        for char in s:
            zigzag[row].append(char)

            if row == 0:
                down = True
            if row == numRows - 1:
                down = False

            if down:
                row += 1
            else:
                row -= 1

        res = ""
        for row in zigzag:
            res += "".join(row)

        return res


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = ["" for _ in range(numRows)]
        row = 0
        for char in s:
            res[row] += char

            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            row += step

        return "".join(res)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(Solution().convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(Solution().convert("A", 1), "A")


if __name__ == "__main__":
    unittest.main()
