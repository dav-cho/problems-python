##
#### Diagonal Traverse (medium)
###################################

# Given an m x n matrix mat, return an array of all the
# elements of the array in a diagonal order.

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# Example 2:
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105

################################################################################


## diagonals and reverse
############################
class Solution:
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
        
        N = len(mat)
        M = len(mat[0])
        
        result, intermediate = [], []
        
        for d in range(N + M - 1):
            intermediate.clear()
            
            r = 0 if d < M else d - M + 1
            c = d if d < M else M - 1
            
            while r < N and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
                
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
                
        return result


## sum of indices
#####################
class Solution:
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        idx_sums = {}

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in idx_sums:
                    idx_sums[i + j] = [mat[i][j]]
                else:
                    idx_sums[i + j].append(mat[i][j])

        result = []

        for sum in idx_sums.items():
            if sum[0] % 2 == 0:
                result.extend(sum[1][::-1])
            else:
                result.extend(sum[1])

        return result


## TODO: walking
##############
class Solution:
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        # next up = [row - 1][col + 1]
        # next down = [row + 1][col - 1]

        N, M = len(mat), len(mat[0])
        row = col = 0
        up = True
        result = []
        
        while row < N and col < M:
            result.append(mat[row][col])
            
            next_row = row + (-1 if up else 1)
            next_col = col + (1 if up else -1)
            
            if next_row < 0 or next_row == N or next_col < 0 or next_col == M:
                if up:
                    row += (col == M - 1)
                    col += (col < M - 1)
                else:
                    col += (row == N - 1)
                    row += (row < N - 1)
                    
                up = not(up)
                
            else:
                row = next_row
                col = next_col
                
        return result 


class Solution:
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        # next up   = [row - 1][col + 1]
        # next down = [row + 1][col - 1]

        pass


## Tests
############

test1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
test2 = [
    [1,   2,   3,  4],
    [5,   6,   7,  8],
    [9,  10,  11, 12],
    [13, 14,  15, 16]
]

solution = Solution()
print(solution.find_diagonal_order(test1))
    # [1, 2, 4, 7, 5, 3, 6, 8, 9]
#print(solution.find_diagonal_order(test2))


## LeetCode Solutions
#########################

## Approach 1: Diagonal Iteration and Reversal
##################################################
# time: O(n * m) - considering a matrix with n rows and m columns
# space: O(min(n, m)) - extra space is occupied by itermediate arrays we use
#                       for storing diagonal elements
# 1. Initialize a result array that we will eventually return.
# 2. We would have an outer loop that will go over each of the diagonals
#    one by one. As mentioned before, the elements in the first row and
#    the last column would actually be the heads of their corresponding
#    diagonals.
# 3. We then have an inner while loop that iterates over all the elements
#    in the diagonal. We can calculate the number of elements in the
#    corresponding diagonal by doing some math but we can simply iterate
#    until one of the indices goes out of bounds.
# 4. For each diagonal we will need a new list or dynamic array like
#    data structure since we don't know what size to allocate. Again,
#    we can do some math and calculate the size of that particular diagonal
#    and allocate memory; but it's not necessary for this explanation.
# 5. For odd numbered diagonals, we simply need to add the elements in our
#    intermediary array, in reverse order to the final result array.
class Solution:
    
    def findDiagonalOrder(self, matrix: list[list[int]]) -> list[int]:
        
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []
        
        # Variables to track the size of the matrix
        N, M = len(matrix), len(matrix[0])
        
        # The two arrays as explained in the algorithm
        result, intermediate = [], []
        
        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        for d in range(N + M - 1):
            
            # Clear the intermediate array everytime we start
            # to process another diagonal
            intermediate.clear()
            
            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            
            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            
            # Reverse even numbered diagonals. The
            # article says we have to reverse odd 
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result


## Approach 2: Simulation
#############################
# time: 
# space: 
# 1. Initialize a boolean variable called direction which will tell us whether
#    the current diagonal is an upwards or downwards going. Based on the
#    current direction and the tail, we will determine the head of the next
#    diagonal. Initially the direction would be 1 which would indicate up.
#    We will keep alternating this value from one iteration to the next.
# 2. Assuming we know the head of a diagonal, say matrix[i][j]matrix[i][j],
#    we will use the direction to progress along the diagonal and process
#    its elements.
#       - For an upwards going diagonal, the next element in the diagonal
#       - would be matrix[i - 1][j + 1]
#       - For a downwards going diagonal, the next element would be
#       - matrix[i + 1][j - 1]
# 3. We keep processing the elements of the current dagonal until
#    we go out of the boundaries of the matrix.
# 4. Now, given that we know the tail of the diagonal
#    (the last node before we went out of bounds), let's see how we can
#    find the next head. Note that in the following pseudocode,
#    the direction is for the current diagonal and we are trying to find
#    the head of the next diagonal. So, if the direction is up,
#    it means the next diagonal would be going down and vice-versa.
class Solution:
    
    def findDiagonalOrder(self, matrix: list[list[int]]) -> list[int]:
        
        # Check for an empty matrix
        if not matrix or not matrix[0]:
            return []
        
        # The dimensions of the matrix
        N, M = len(matrix), len(matrix[0])
        
        # Incides that will help us progress through 
        # the matrix, one element at a time.
        row, column = 0, 0
        
        # As explained in the article, this is the variable
        # that helps us keep track of what direction we are
        # processing the current diaonal
        direction = 1
        
        # Final result array that will contain all the elements
        # of the matrix
        result = []
        
        # The uber while loop which will help us iterate over all
        # the elements in the array.
        while row < N and column < M:
            
            # First and foremost, add the current element to 
            # the result matrix. 
            result.append(matrix[row][column])
            
            # Move along in the current diagonal depending upon
            # the current direction.[i, j] -> [i - 1, j + 1] if 
            # going up and [i, j] -> [i + 1][j - 1] if going down.
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)
            
            # Checking if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head. 
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
                
                # If the current diagonal was going in the upwards
                # direction.
                if direction:
                    
                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    row += (column == M - 1)
                    column += (column < M - 1)
                else:
                    
                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    column += (row == N - 1)
                    row += (row < N - 1)
                    
                # Flip the direction
                direction = 1 - direction        
            else:
                row = new_row
                column = new_column
                        
        return result


## Sum of Indices (discuss)
##################################
# 1. Diagonals are defined by the sum of indicies in a 2 dimensional array
# 2. The snake phenomena can be achieved by reversing every other
#    diagonal level, therefore check if divisible by 2
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        d={}
		#loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
				#if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
				#If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
		# we're done with the pass, let's build our answer array
        ans= []
		#look at the diagonal and each diagonal's elements
        for entry in d.items():
			#each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
			#snake time, look at the diagonal level
            if entry[0] % 2 == 0:
				#Here we append in reverse order because its an even numbered level/diagonal. 
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans



