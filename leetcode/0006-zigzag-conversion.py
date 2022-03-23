##
#### Zigzag Conversion (medium)
########################################

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a
# number of rows:

# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
 
# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

################################################################################


## 
##############################
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass


## 
##############################
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass


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
        
        res = ''
        for row in zigzag:
            res += ''.join(row)

        return res


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ['' for _ in range(numRows)]

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
        
        return ''.join(res)


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

        res = ''
        for row in zigzag:
            res += ''.join(row)

        return res


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = ['' for _ in range(numRows)]
        row = 0
        for char in s:
            res[row] += char

            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            row += step

        return ''.join(res)


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


## LeetCode Solutions
#########################

## Approach 1: 
##############################
# Time: 
# Space: 


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


