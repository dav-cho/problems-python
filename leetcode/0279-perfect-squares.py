##
#### Perfect Squares (medium)
#################################

# Given an integer n, return the least number of perfect square numbers that
# sum to n.

# A perfect square is an integer that is the square of an integer; in other
# words, it is the product of some integer with itself. For example, 1, 4, 9,
# and 16 are perfect squares while 3 and 11 are not.

# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# Constraints:
# 1 <= n <= 104

################################################################################

## 
######################
class Solution:
    def numSquares(self, n: int) -> int:
        pass


## dynamic programming
##########################
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(0, int(n ** 0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[-1]


## Tests
#############


## LeetCode Solutions
#########################

## Approach 1: Brute-force Enumeration [Time Limit Exceeded]
################################################################
# Time: 
# Space: 
class Solution(object):
    def numSquares(self, n):
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)


## Approach 2: Dynamic Programming
######################################
# Time: O(n * sqrt(n)) - In main step, we have a nested loop, where the outer
#                        loop is of nn iterations and in the inner loop it takes
#                        at maximum sqrt(n) 
# Space: O(n) - We keep all the intermediate sub-solutions in the array dp[].
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]


## Approach 3: Greedy Enumeration
#####################################
# Time: O(n^(h/2))
# O(sqrt(n^h+1) - 1) = O(n^(h/2)) where h is the maximal number of recursion
# that could happen. As one might notice, the above formula actually resembles
# the formula to calculate the number of nodes in a complete N-ary tree. Indeed,
# the trace of recursive calls in the algorithm form a N-ary tree, where N is
# the number of squares in square_nums, i.e. sqrt(n). In the worst case, we
# might have to traverse the entire tree to find the solution.

# Space: O(sqrt(n))
# We keep a list of square_nums, which is of sqrt(n) size. In addition, we
# would need additional space for the recursive call stack. But as we will
# learn later, the size of the call track would not exceed 4.
class Solution:
    def numSquares(self, n):
        
        def is_divided_by(n, count):
            """
                return: true if "n" can be decomposed into "count" number of perfect square numbers.
                e.g. n=12, count=3:  true.
                     n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums
            
            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
    
        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count


## Approach 4: Greedy + BFS (Breadth-First Search)
######################################################
# Time: O(n^(h/2))
# O((sqrt(n^(h+1)) - 1) / (sqrt(n) - 1)) = O(n^(h/2)) where h is the height of
# the N-ary tree. One can see the detailed explanation on the previous
# Approach #3.

# Space: O(sqrt(n)^h)
# Which is also the maximal number of nodes that can appear at the level h. As
# one can see, though we keep a list of square_nums, the main consumption of
# the space is the queue variable, which keep track of the remainders to visit
# for a given level of N-ary tree.
class Solution:
    def numSquares(self, n):

        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
        level = 0
        queue = {n}
        while queue:
            level += 1
            #! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:    
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level


## Approach 5: Mathematics
##############################
# Time: O(sqrt(n)) - In the main loop, we check if the number can be decomposed
#                    into the sum of two squares, which takes O(sqrt(n))
#                    iterations. In the rest of cases, we do the check in
#                    constant time.
# Space: O(1) - The algorithm consumes a constant space, regardless the size of
#               the input number.
class Solution:
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq*sq == n

    def numSquares(self, n: int) -> int:
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3
