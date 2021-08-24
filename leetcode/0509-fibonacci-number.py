##
#### Fibonacci Number (easy)
################################

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
# Constraints:
# 0 <= n <= 30

################################################################################

# recursive
# bottom-up tabulation
# top-down memoization
# iterative bottom up
# matrix exponentiation
# math (golden ratio)

## recursive
##############################
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        return self.fib(n - 2) + self.fib(n - 1)


## bottom-up tabulation
##############################
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        cache = [0] * (n + 1)
        cache[1] = 1
        for i in range(2, n + 1):
            cache[i] = cache[i - 2] + cache[i - 1]
            
        return cache[n]


## memoized recursive
##############################
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def recursive_fib(n):
            if n in cache:
                return cache[n]
            
            if n < 2:
                result = n
            else:
                result = recursive_fib(n - 2) + recursive_fib(n - 1)
                
            cache[n] = result
            return result
        
        return recursive_fib(n)


class Solution:
    def __init__(self):
        self.cache = {0: 0, 1: 1}
        
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.fib(n - 2) + self.fib(n - 1)
        return self.cache[n]


## iterative bottom-up
##############################
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        a, b, c = 0, 1, 0
        for _ in range(2, n + 1):
            c = a + b
            a, b = b, c
            
        return c


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        a, b, c = 0, 1, 0
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
            
        return c


## TODO: matrix exponentiation
##############################
class Solution:
    def fib(self, n: int) -> int:
        pass


## math
##############################
class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        
        return int(round((golden_ratio ** n) / (5 ** 0.5)))


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursion
############################
# Time: O(2^N)
# This is the slowest way to solve the Fibonacci Sequence because it takes
# exponential time. The amount of operations needed, for each level of
# recursion, grows exponentially as the depth approaches N.

# Space: O(N)
# We need space proportional to N to account for the max size of the stack, in
# memory. This stack keeps track of the function calls to fib(N). This has the
# potential to be bad in cases that there isn't enough physical memory to handle
# the increasingly growing stack, leading to a StackOverflowError. The Java docs
# have a good explanation of this, describing it as an error that occurs because
# an application recurses too deeply.

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


## Approach 2: Bottom-Up Approach using Tabulation
######################################################
# Time: O(N) - Each number, starting at 2 up to and including N, is visited,
#              computed and then stored for O(1) access later on.
# Space: O(N) - The size of the data structure is proportional to N.

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[N]


## Approach 3: Top-Down Approach using Memoization
######################################################
# Time: O(N) - Each number, starting at 2 up to and including N, is visited,
#              computed and then stored for O(1) access later on.
# Space: O(N) - The size of the stack in memory is proportional to N. Also, the
#               memoization hash table is used, which occupies O(N) space.

class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]


## Approach 4: Iterative Bottom-Up Approach
###############################################
# Time: O(N)
# Each value from 2 to N is computed once. Thus, the time it takes to find the
# answer is directly proportional to N where N is the Fibonacci Number we are
# looking to compute.

# Space: 
# This requires 1 unit of space for the integer N and 3 units of space to store
# the computed values (current, prev1, and prev2) for every loop iteration. The
# amount of space used is independent of NN, so this approach uses a constant
# amount of space.

class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        current = 0
        prev1 = 1
        prev2 = 0

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current


## Aprroach 5: Matrix Exponentiation
########################################
# Time: O(logN) - By halving the N value in every matrixPower's call to
#                   itself, we are halving the work needed to be done.
# Space: O(logN) - The size of the stack in memory is proportional to the
#                   function calls to matrixPower plus the memory used to
#                   account for the matrices which use constant space.

class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        A = [[1, 1], [1, 0]]
        self.matrix_power(A, N - 1)

        return A[0][0]

    def matrix_power(self, A: List[List[int]], N: int):
        if (N <= 1):
            return A

        self.matrix_power(A, N // 2)
        self.multiply(A, A)
        B = [[1, 1], [1, 0]]

        if (N % 2 != 0):
            self.multiply(A, B)

    def multiply(self, A: List[List[int]], B: List[List[int]]) -> None:
        x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

        A[0][0] = x
        A[0][1] = y
        A[1][0] = z
        A[1][1] = w


## Approach 6: Math
#######################
# Time: O(logN) - We do not use loops or recursion, so the time required
#                   equals the time spent performing the calculation using
#                   Binet's formula. However, raising the golden_ratio to the
#                   power of N requires O(logN) time.
# Space: O(1) - The space used is the space needed to create the variable to
#               store the golden ratio.

class Solution:
    def fib(self, N: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** N) / (5 ** 0.5)))


