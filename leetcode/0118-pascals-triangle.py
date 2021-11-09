##
#### Pascal's Triangle (easy)
########################################

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]
 
# Constraints:
# 1 <= numRows <= 30

################################################################################

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


## 
##############################
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pass


## 
##############################
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pass


## 
##############################
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        self.assertEqual(Solution().generate(1), [[1]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Dynamic Programming
######################################
# Time: O(numRows^2)
# - Although updating each value of triangle happens in constant time, it is
#   performed O(numRows^2) times. To see why, consider how many overall loop
#   iterations there are. The outer loop obviously runs numRowsnumRows times,
#   but for each iteration of the outer loop, the inner loop runs rowNum times.
#   Therefore, the overall number of triangle updates that occur is
#   1 + 2 + 3 + ... + numRows, which, according to Gauss' formula, is
#   numRows(numRows + 1) / 2 = (numRows^2 + numRows) / 2
#                            = (numRows^2 / 2) + (numRows / 2) 
#                            = O(numRows^2)

# Space: O(numRows^2)
# - Because we need to store each number that we update in triangle, the space
#   requirement is the same as the time complexity.

class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


