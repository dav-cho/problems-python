##
#### Search a 2D Matrix II (medium)
#######################################

# Write an efficient algorithm that searches for a target value in an m x n
# integer matrix. The matrix has the following properties:

# - Integers in each row are sorted in ascending from left to right.
# - Integers in each column are sorted in ascending from top to bottom.

# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109

################################################################################

## brute force
##############################
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
            
        return False


## binary search
##############################
class Solution:
    def binary_search(self, matrix, target, start, vertical):
        low = start
        high = len(matrix[0]) - 1 if vertical else len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if vertical:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True
            
        return False
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        
        for i in range(min(len(matrix), len(matrix[0]))):
            horizontal_search = self.binary_search(matrix, target, i, False)
            vertical_search = self.binary_search(matrix, target, i, True)
            if horizontal_search or vertical_search:
                return True
            
        return False


class Solution:
    def binary_search(self, matrix, target, start, vertical):
        low = start
        high = len(matrix[0]) - 1 if vertical else len(matrix) - 1
        
        while high >= low:
            mid = (low + high) // 2
            if vertical:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True
                    
        return False
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
            
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def binary_search(start, vertical):
            low = start
            high = len(matrix[0]) - 1 if vertical else len(matrix) - 1
            while low <= high:
                mid = (low + high) // 2
                if vertical:
                    if matrix[start][mid] < target:
                        low = mid + 1
                    elif matrix[start][mid] > target:
                        high = mid - 1
                    else:
                        return True
                else:
                    if matrix[mid][start] < target:
                        low = mid + 1
                    elif matrix[mid][start] > target:
                        high = mid - 1
                    else:
                        return True
                    
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            horizontal_search = binary_search(i, False)
            vertical_search = binary_search(i, True)
            if horizontal_search or vertical_search:
                return True
            
        return False


## divide and concquer
##############################
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def search_recursive(left, up, right, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right - left) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
                
            return search_recursive(left, row, mid - 1, down) or \
                   search_recursive(mid + 1, up, right, row - 1)
        
        return search_recursive(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


## search space reduction
##############################
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        
        height = len(matrix)
        width = len(matrix[0])
        row = height - 1
        col = 0
        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
            
        return False


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        height = len(matrix)
        width = len(matrix[0])
        row = height - 1
        col = 0
        while row >= 0 and col < width:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        
        return False


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5), True)
        self.assertEqual(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(nm) - Becase we perform a constant time operation for each element of
#               an n×m element matrix, the overall time complexity is equal to
#               the size of the matrix.
# Space: O(1) - The brute force approach does not allocate more additional space
#               than a handful of pointers, so the memory footprint is constant.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        
        return False


## Approach 2: Binary Search
################################
# Time: O(log(n!))
# - It's not super obvious how O(log(n!)) time complexity arises from this
#   algorithm, so let's analyze it step-by-step. The asymptotically-largest
#   amount of work performed is in the main loop, which runs for min(m,n)
#   iterations, where m denotes the number of rows and n denotes the number of
#   columns. On each iteration, we perform two binary searches on array slices
#   of length m−i and n−i. Therefore, each iteration of the loop runs in
#   O(log(m−i)+log(n−i)) time, where i denotes the current iteration. We can
#   simplify this to O(2⋅log(n−i))=O(log(n−i)) by seeing that, in the worst
#   case, n≈m. To see why, consider what happens when mn≪m (without loss of
#   generality); n will dominate m in the asymptotic analysis. By summing the
#   runtimes of all iterations, we get the following expression:
#       (1): O(log(n)+log(n−1)+log(n−2)+…+log(1))
# - Then, we can leverage the log multiplication rule log(a)+log(b)=log(ab)) to
#   rewrite the complexity as: 
#       (2): O(log(n)+log(n−1)+log(n−2)+…+log(1)) = O(log(n⋅(n−1)⋅(n−2)⋅…⋅1))
#                                                 = O(log(1⋅…⋅(n−2)⋅(n−1)⋅n))
#                                                 = O(log(n!))
# - Because this time complexity is fairly uncommon, it is worth thinking about
#   its relation to the usual analyses. For one, log(n!)=O(nlogn). To see why,
#   recall step 1 from the analysis above; there are n terms, each no greater
#   than log(n). Therefore, the asymptotic runtime is certainly no worse than
#   that of an O(nlogn) algorithm.

# Space: O(1)
# - Because our binary search implementation does not literally slice out copies
#   of rows and columns from matrix, we can avoid allocating
#   greater-than-constant memory.

class Solution:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical: # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        
        return False


## Approach 3: Divide and Conquer
#####################################
# Time: O(nlogn)
# - First, for ease of analysis, assume that n≈m, as in the analysis of approach
#   2. Also, assign x=n^2=|matrix|; this will make the master method easier to
#   apply. Now, let's model the runtime of the divide & conquer approach as a
#   recurrence relation: T(x)=2⋅T(x/4)+sqrt(x)
# - The first term (2⋅T(x/4)) arises from the fact that we recurse on two
#   submatrices of roughly one-quarter size, while sqrt(x) comes from the time
#   spent seeking along a O(n)-length column for the partition point. After
#   binding the master method variables (a=2;b=4;c=0.5) we notice that a=c.
#   Therefore, this recurrence falls under case 2 of the master method, and the
#   following falls out:
#       T(x) = O(x^c ⋅logx)
#            = O(x^0.5 ⋅logx)
#            = O((n^2)^0.5 ⋅log(n^2))
#            = O(n⋅log(n^2))
#            = O(2n⋅logn)
#            = O(n⋅logn)
# - Extension: what would happen to the complexity if we binary searched for the
#   partition point, rather than used a linear scan?

# Space: O(logn)
# - Although this approach does not fundamentally require greater-than-constant
#   addition memory, its use of recursion means that it will use memory
#   proportional to the height of its recursion tree. Because this approach
#   discards half of matrix on each level of recursion (and makes two recursive
#   calls), the height of the tree is bounded by \log nlogn.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right-left) // 2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return search_rec(left, row, mid - 1, down) or \
                   search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


## Approach 4: Search Space Reduction
#########################################
# Time: O(n+m)
# - The key to the time complexity analysis is noticing that, on every iteration
#   (during which we do not return true) either row or col is is
#   decremented/incremented exactly once. Because row can only be decremented m
#   times and col can only be incremented n times before causing the while loop
#   to terminate, the loop cannot run for more than n+mn+m iterations. Because
#   all other work is constant, the overall time complexity is linear in the
#   sum of the dimensions of the matrix.

# Space: O(1)
# - Because this approach only manipulates a few pointers, its memory footprint
#   is constant.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False


