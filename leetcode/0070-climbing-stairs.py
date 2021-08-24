##
#### Climbing Stairs (easy)
###############################

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
# 1 <= n <= 45

###########################################################################


## dynamic programming
##########################
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        cache = [0] * (n + 1)
        cache[1] = 1; cache[2] = 2
        
        for i in range(3, n + 1):
            cache[i] = cache[i - 2] + cache[i - 1]
            
        return cache[n]


## recursive
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)


# [time limit exceeded]
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb(0, n)
    
    def climb(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        
        return self.climb(i + 1, n) + self.climb(i + 2, n)


## memoized recursive
##############################
class Solution:
    def __init__(self):
        self.cache = {1: 1, 2: 2, 3: 3}
        
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return self.cache[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)

        def climb(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            if cache[i] > 0:
                return cache[i]
            
            cache[i] = climb(i + 1, n) + climb(i + 2, n)
            return cache[i]
        
        return climb(0, n)


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        
        def helper(n):
            if n in cache:
                return cache[n]
            
            if n < 4:
                result = n
            else:
                result = helper(n - 2) + helper(n - 1)
                
            cache[n] = result
            return result
        
        return helper(n)


## iterative
################
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        a, b = 1, 2
        for i in range(3, n + 1):
            c = a + b
            a, b = b, c
            
        return b


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        
        a, b, c = 2, 3, 0
        for _ in range(4, n + 1):
            c = a + b
            a, b = b, c
            
        return c


## iterative memoized
##############################
class Solution:
    def __init__(self):
        self.cache = {1: 1, 2: 2, 3: 3}
        
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        for i in range(3, n + 1):
            self.cache[i] = self.cache[i - 2] + self.cache[i - 1]
            
        return self.cache[n]


## Tests
############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(2), 2)
        self.assertEqual(solution.climbStairs(3), 3)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(2^n) - Size of recursion tree will be 2^n.
# Space: O(n) - The depth of the recursion tree can go upto n.

## Java
#public class Solution {
#    public int climbStairs(int n) {
#        return climb_Stairs(0, n);
#    }
#    public int climb_Stairs(int i, int n) {
#        if (i > n) {
#            return 0;
#        }
#        if (i == n) {
#            return 1;
#        }
#        return climb_Stairs(i + 1, n) + climb_Stairs(i + 2, n);
#    }
#}


## Approach 2: Recursion with Memoization
#############################################
# Time: O(n) - Size of recursion tree can go upto n.
# Space: O(n) - The depth of recursion tree can go upto n.

## Java
#public class Solution {
#    public int climbStairs(int n) {
#        int memo[] = new int[n + 1];
#        return climb_Stairs(0, n, memo);
#    }
#    public int climb_Stairs(int i, int n, int memo[]) {
#        if (i > n) {
#            return 0;
#        }
#        if (i == n) {
#            return 1;
#        }
#        if (memo[i] > 0) {
#            return memo[i];
#        }
#        memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);
#        return memo[i];
#    }
#}


## Approach 3: Dynamic Programming
######################################
# Time: O(n) - Single loop upto n.
# Space: O(n) - dp array of size nn is used.

## Java
#public class Solution {
#    public int climbStairs(int n) {
#        if (n == 1) {
#            return 1;
#        }
#        int[] dp = new int[n + 1];
#        dp[1] = 1;
#        dp[2] = 2;
#        for (int i = 3; i <= n; i++) {
#            dp[i] = dp[i - 1] + dp[i - 2];
#        }
#        return dp[n];
#    }
#}


## Approach 4: Fibonacci Number
###################################
# Time: O(n) - Single loop upto n is required to calculate nth fibonacci number.
# Space: O(1) - O(1). Constant space is used.

## Java
#public class Solution {
#    public int climbStairs(int n) {
#        if (n == 1) {
#            return 1;
#        }
#        int first = 1;
#        int second = 2;
#        for (int i = 3; i <= n; i++) {
#            int third = first + second;
#            first = second;
#            second = third;
#        }
#        return second;
#    }
#}


## Approach 5: Binets Method
################################
# Time: O(log(n)) - Traversing on logn bits.
# Space: O(1) - Constant space is used.

## Java
# public class Solution {
#    public int climbStairs(int n) {
#        int[][] q = {{1, 1}, {1, 0}};
#        int[][] res = pow(q, n);
#        return res[0][0];
#    }
#    public int[][] pow(int[][] a, int n) {
#        int[][] ret = {{1, 0}, {0, 1}};
#        while (n > 0) {
#            if ((n & 1) == 1) {
#                ret = multiply(ret, a);
#            }
#            n >>= 1;
#            a = multiply(a, a);
#        }
#        return ret;
#    }
#    public int[][] multiply(int[][] a, int[][] b) {
#        int[][] c = new int[2][2];
#        for (int i = 0; i < 2; i++) {
#            for (int j = 0; j < 2; j++) {
#                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
#            }
#        }
#        return c;
#    }
#}


## Approach 6: Fibonacci Formula
####################################
# Time: O(log(n)). pow method takes logn time.
# Space: O(1). Constant space is used.

## Java
#public class Solution {
#    public int climbStairs(int n) {
#        double sqrt5=Math.sqrt(5);
#        double fibn=Math.pow((1+sqrt5)/2,n+1)-Math.pow((1-sqrt5)/2,n+1);
#        return (int)(fibn/sqrt5);
#    }
#}


