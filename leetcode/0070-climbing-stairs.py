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
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0, 1, 2] + [None] * (n - 2)
        
        for i in range(3, n + 1):
            memo[i] = memo[i - 2] + memo[i - 1]
            
        return memo[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1, 2] + [None] * (n - 2)
        
        for i in range(2, n):
            memo[i] = memo[i - 2] + memo[i - 1]
            
        return memo[n - 1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        memo = [None] * (n + 1)
        memo[1], memo[2] = 1, 2
        
        for i in range(3, n + 1):
            memo[i] = memo[i - 2] + memo[i - 1]
            
        return memo[n]


## recursion w/ memoization
##############################

from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def helper(i):
            if i in memo:
                return memo[i]
            elif i > n:
                return 0
            elif i == n:
                return 1
            
            memo[i] = helper(i + 1) + helper(i + 2)
            
            return memo[i]
        
        return helper(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def helper(i):
            if i in memo:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1
            
            memo[i] = helper(i + 1) + helper(i + 2)
            
            return memo[i]
        
        return helper(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * (n + 2)
        
        def helper(i):
            if memo[i]:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1
            
            memo[i] = helper(i + 1) + helper(i + 2)
            
            return memo[i]
        
        return helper(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict()
        
        def helper(i, n):
            if i in memo:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1
            
            memo[i] = helper(i + 1, n) + helper(i + 2, n)
            
            return memo[i]
        
        return helper(0, n)


## fibonacci number
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        a, b = 1, 2
        
        for i in range(3, n + 1):
            c = a + b
            a, b = b, c
            
        return b


## brute force (TLE)
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i):
            if i > n:
                return 0
            if i == n:
                return 1
            
            return helper(i + 1) + helper(i + 2)
        
        return helper(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            
            return helper(i + 1, n) + helper(i + 2, n)
        
        return helper(0, n)


## fibonacci formula
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        pass


## binets method
##############################
class Solution:
    def climbStairs(self, n: int) -> int:
        pass


## Tests
############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(2), 2)
        self.assertEqual(solution.climbStairs(3), 3)

        self.assertEqual(solution.climbStairs(4), 5)
        self.assertEqual(solution.climbStairs(10), 89)
        self.assertEqual(solution.climbStairs(20), 10946)


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


